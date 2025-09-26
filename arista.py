class Arista:
    def __init__(self, origen, destino, attrs=None, dirigida=False):
        self.origen = str(origen)
        self.destino = str(destino)
        self.attrs = dict(attrs) if attrs else {}
        self.dirigida = dirigida

    def __repr__(self):
        arrow = "->" if self.dirigida else "--"
        return f"Arista({self.origen} {arrow} {self.destino}, attrs={self.attrs})"


