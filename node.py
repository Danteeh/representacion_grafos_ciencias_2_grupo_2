class Nodo:
    def __init__(self, id, attrs=None):
        self.id = str(id)
        self.attrs = dict(attrs) if attrs else {}

    def __repr__(self):
        return f"Nodo({self.id}, attrs={self.attrs})"


