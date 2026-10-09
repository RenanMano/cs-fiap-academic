def area_triangulo(b, h):
    return (b * h) / 2

def area_circunferencia(r):
    return 3.141593 * r ** 2

def perimetro_retangulo(b, h):
    return 2 * (b + h)

def area_trapezio(B, b, h):
    return ((B + b) * h) / 2

print(area_triangulo(2, 14))          # base 2 cm, altura 14 cm
print(area_circunferencia(r=10))      # raio 10 mm (argumento nomeado)
print(perimetro_retangulo(12, 4))     # base 12 m, altura 4 m
print(area_trapezio(B=5, b=3, h=4))   # bases 5 m e 3 m, altura 4 m
