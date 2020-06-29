
class Coordenada:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    
    def distancia_euclidiana(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5