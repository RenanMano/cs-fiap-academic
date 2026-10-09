#!/usr/bin/env python3
"""Gera SVGs estatísticos (paleta Knowledge Atelier) a partir dos dados dos slides.
Os valores (contagens, quartis) são calculados com numpy/pandas, não desenhados à mão."""
import math, os, sys
import numpy as np

BG, FG, MUTED, GRID, PANEL = '#0D1117', '#F8FAFC', '#CBD5E1', '#30363D', '#161B22'
C1, C2, C3 = '#FF781F', '#FF4500', '#E60000'
FONT = 'Fira Code, Consolas, monospace'


def head(w, h, title, desc):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-labelledby="t d">',
            f'<title id="t">{title}</title>', f'<desc id="d">{desc}</desc>',
            '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FF781F"/>'
            '<stop offset=".5" stop-color="#FF4500"/><stop offset="1" stop-color="#E60000"/></linearGradient></defs>',
            f'<rect width="{w}" height="{h}" rx="18" fill="{BG}"/>', f'<rect width="{w}" height="6" rx="3" fill="url(#g)"/>',
            f'<g font-family="{FONT}">']


def text(x, y, s, size=13, fill=FG, anchor='middle', weight='400'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'


def fmt(v):
    v = float(v)
    return str(int(v)) if v == int(v) else f'{v:.2f}'.rstrip('0').rstrip('.').replace('.', ',')


def axes(x0, y0, w, h, ymax, step, ylabel):
    out = []
    for k in range(0, int(ymax) + 1, step):
        y = y0 - h * k / ymax
        out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + w}" y2="{y:.1f}" stroke="{GRID}"/>')
        out.append(text(x0 - 8, y + 4, str(k), 11, MUTED, 'end'))
    out.append(f'<line x1="{x0}" y1="{y0}" x2="{x0 + w}" y2="{y0}" stroke="{MUTED}"/>')
    out.append(f'<text x="{x0 - 38}" y="{y0 - h / 2:.1f}" font-size="12" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 {x0 - 38} {y0 - h / 2:.1f})">{ylabel}</text>')
    return out


def pie(cx, cy, r, labels, values, colors):
    out, tot, a0 = [], sum(values), -math.pi / 2
    for lab, v, c in zip(labels, values, colors):
        a1 = a0 + 2 * math.pi * v / tot
        large = 1 if a1 - a0 > math.pi else 0
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        out.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} Z" fill="{c}" stroke="{BG}" stroke-width="2"/>')
        am = (a0 + a1) / 2
        out.append(text(cx + 0.62 * r * math.cos(am), cy + 0.62 * r * math.sin(am) + 5, f'{100 * v / tot:.2f}%'.replace('.', ','), 14, FG, weight='700'))
        out.append(text(cx + 1.18 * r * math.cos(am), cy + 1.18 * r * math.sin(am) + 5, f'{lab} ({v})', 13, MUTED))
        a0 = a1
    return out


def bars(x0, y0, w, h, labels, values, ymax, step, ylabel, color=C1):
    out = axes(x0, y0, w, h, ymax, step, ylabel)
    n = len(values); bw = w / n * 0.55
    for i, (lab, v) in enumerate(zip(labels, values)):
        cx = x0 + w * (i + 0.5) / n; bh = h * v / ymax
        out.append(f'<rect x="{cx - bw / 2:.1f}" y="{y0 - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{color}" rx="3"/>')
        out.append(text(cx, y0 - bh - 6, fmt(v), 12, FG, weight='700'))
        out.append(text(cx, y0 + 18, lab, 12, MUTED))
    return out


def hist(x0, y0, w, h, edges, counts, ymax, step, ylabel, xlabel):
    out = axes(x0, y0, w, h, ymax, step, ylabel)
    lo, hi = edges[0], edges[-1]
    X = lambda v: x0 + w * (v - lo) / (hi - lo)
    for a, b, c in zip(edges[:-1], edges[1:], counts):
        bh = h * c / ymax
        out.append(f'<rect x="{X(a):.1f}" y="{y0 - bh:.1f}" width="{X(b) - X(a):.1f}" height="{bh:.1f}" fill="{C1}" stroke="{BG}" stroke-width="2"/>')
        out.append(text((X(a) + X(b)) / 2, y0 - bh - 6, str(int(c)), 12, FG, weight='700'))
    for e in edges:
        out.append(text(X(e), y0 + 18, fmt(e), 12, MUTED))
    out.append(text(x0 + w / 2, y0 + 38, xlabel, 12, MUTED))
    return out


def box_stats(data):
    d = np.asarray(data, float)
    q1, q2, q3 = np.percentile(d, [25, 50, 75])
    iqr = q3 - q1; li, ls = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    inside = d[(d >= li) & (d <= ls)]
    return dict(q1=q1, q2=q2, q3=q3, li=li, ls=ls, wlo=inside.min(), whi=inside.max(),
                out=sorted(d[(d < li) | (d > ls)]))


def boxplot(x0, y_top, w, h, data, vmin, vmax, step, annotate=True, color=C1):
    """Boxplot vertical. Retorna (elementos, estatísticas)."""
    s = box_stats(data)
    Y = lambda v: y_top + h * (vmax - v) / (vmax - vmin)
    out = []
    k = vmin
    while k <= vmax + 1e-9:
        out.append(f'<line x1="{x0 - 40}" y1="{Y(k):.1f}" x2="{x0 + w + 40}" y2="{Y(k):.1f}" stroke="{GRID}"/>')
        out.append(text(x0 - 48, Y(k) + 4, fmt(k), 11, MUTED, 'end'))
        k += step
    cx = x0 + w / 2
    out.append(f'<line x1="{cx}" y1="{Y(s["whi"]):.1f}" x2="{cx}" y2="{Y(s["q3"]):.1f}" stroke="{MUTED}" stroke-width="2"/>')
    out.append(f'<line x1="{cx}" y1="{Y(s["q1"]):.1f}" x2="{cx}" y2="{Y(s["wlo"]):.1f}" stroke="{MUTED}" stroke-width="2"/>')
    for v in (s['whi'], s['wlo']):
        out.append(f'<line x1="{cx - w / 4}" y1="{Y(v):.1f}" x2="{cx + w / 4}" y2="{Y(v):.1f}" stroke="{MUTED}" stroke-width="2"/>')
    out.append(f'<rect x="{x0}" y="{Y(s["q3"]):.1f}" width="{w}" height="{max(Y(s["q1"]) - Y(s["q3"]), 1):.1f}" fill="{color}" fill-opacity=".85" stroke="{FG}" stroke-width="1.5"/>')
    out.append(f'<line x1="{x0}" y1="{Y(s["q2"]):.1f}" x2="{x0 + w}" y2="{Y(s["q2"]):.1f}" stroke="{FG}" stroke-width="3"/>')
    for v in s['out']:
        out.append(f'<circle cx="{cx}" cy="{Y(v):.1f}" r="5" fill="none" stroke="{C3}" stroke-width="2"/>')
    if annotate:
        xa = x0 + w + 54
        raw = [('máximo (bigode)', s['whi']), ('Q3', s['q3']), ('mediana (Q2)', s['q2']), ('Q1', s['q1']), ('mínimo (bigode)', s['wlo'])]
        labs = []
        for lab, v in raw:
            if labs and labs[-1][1] == v:
                labs[-1] = (labs[-1][0] + ' = ' + lab, v)
            else:
                labs.append((lab, v))
        used = []
        for lab, v in labs:
            y = Y(v) + 4
            while any(abs(y - u) < 16 for u in used):
                y += 16
            used.append(y)
            out.append(text(xa, y, f'{lab}: {fmt(v)}', 12, FG, 'start'))
    return out, s


def save(path, parts, w, h, title, desc):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write('\n'.join(head(w, h, title, desc) + parts + ['</g>', '</svg>']) + '\n')
    print('ok', path)


def normal_curve(x0, y0, w, h, mu, sigma, shade, ticks, label_fmt=fmt, color=C1):
    """Curva normal de mu-4σ a mu+4σ; shade = lista de (a, b, cor) para áreas sombreadas."""
    from statistics import NormalDist
    nd = NormalDist(mu, sigma)
    lo, hi = mu - 4 * sigma, mu + 4 * sigma
    X = lambda v: x0 + w * (v - lo) / (hi - lo)
    pk = nd.pdf(mu)
    Y = lambda v: y0 - h * nd.pdf(v) / pk
    out = []
    for a, b, c in shade:
        a, b = max(a, lo), min(b, hi)
        pts = [f'{X(a):.1f},{y0}'] + [f'{X(a + (b - a) * k / 80):.1f},{Y(a + (b - a) * k / 80):.1f}' for k in range(81)] + [f'{X(b):.1f},{y0}']
        out.append(f'<polygon points="{" ".join(pts)}" fill="{c}" fill-opacity=".85"/>')
    pts = ' '.join(f'{X(lo + (hi - lo) * k / 200):.1f},{Y(lo + (hi - lo) * k / 200):.1f}' for k in range(201))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{FG}" stroke-width="2"/>')
    out.append(f'<line x1="{x0}" y1="{y0}" x2="{x0 + w}" y2="{y0}" stroke="{MUTED}"/>')
    for t in ticks:
        out.append(f'<line x1="{X(t):.1f}" y1="{y0}" x2="{X(t):.1f}" y2="{y0 + 5}" stroke="{MUTED}"/>')
        out.append(text(X(t), y0 + 20, label_fmt(t), 12, MUTED))
    return out, X, Y


def plot_axes(x0, y0, w, h, xr, yr, xticks, yticks):
    """Eixos cartesianos com grade. Retorna (elementos, X, Y)."""
    X = lambda v: x0 + w * (v - xr[0]) / (xr[1] - xr[0])
    Y = lambda v: y0 + h - h * (v - yr[0]) / (yr[1] - yr[0])
    out = []
    for t in xticks:
        out.append(f'<line x1="{X(t):.1f}" y1="{y0}" x2="{X(t):.1f}" y2="{y0 + h}" stroke="{GRID}"/>')
        out.append(text(X(t), y0 + h + 16, fmt(t), 11, MUTED))
    for t in yticks:
        out.append(f'<line x1="{x0}" y1="{Y(t):.1f}" x2="{x0 + w}" y2="{Y(t):.1f}" stroke="{GRID}"/>')
        out.append(text(x0 - 6, Y(t) + 4, fmt(t), 11, MUTED, 'end'))
    if xr[0] <= 0 <= xr[1]:
        out.append(f'<line x1="{X(0):.1f}" y1="{y0}" x2="{X(0):.1f}" y2="{y0 + h}" stroke="{MUTED}"/>')
    if yr[0] <= 0 <= yr[1]:
        out.append(f'<line x1="{x0}" y1="{Y(0):.1f}" x2="{x0 + w}" y2="{Y(0):.1f}" stroke="{MUTED}"/>')
    return out, X, Y


def curve(f, X, Y, xa, xb, color, n=300, yr=None, width=2.5, dash=None):
    pts, segs = [], []
    for k in range(n + 1):
        x = xa + (xb - xa) * k / n
        try:
            y = f(x)
        except ZeroDivisionError:
            y = None
        if y is None or (yr and not (yr[0] - 1e-9 <= y <= yr[1] + 1e-9)):
            if len(pts) > 1: segs.append(pts)
            pts = []
            continue
        pts.append(f'{X(x):.1f},{Y(y):.1f}')
    if len(pts) > 1: segs.append(pts)
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return [f'<polyline points="{" ".join(s)}" fill="none" stroke="{color}" stroke-width="{width}"{d}/>' for s in segs]
