class Pin:
    OUT = 1
    def __init__(self, n, mode): self.n = n; self.v = 0
    def value(self, v=None):
        if v is None: return self.v
        self.v = v; print(f"  [GPIO {self.n} = {v}]")
