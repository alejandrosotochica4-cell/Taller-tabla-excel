class Carro:
    def __init__(self, placa_carro, tipo_carro, color_carro):
        self.placa_carro = placa_carro
        self.tipo_carro = tipo_carro
        self.color_carro = color_carro
        
    def get_placa_carro(self):
        return self.placa_carro
    
    def set_placa_carro(self, nueva_placa_carro):
        self.placa_carro = nueva_placa_carro

    def get_tipo_carro(self):
        return self.tipo_carro
    
    def set_tipo_carro(self, nuevo_tipo_carro):
        self.tipo_carro = nuevo_tipo_carro

    def get_color_carro(self):
        return self.color_carro
    
    def set_color_carro(self, nuevo_color_carro):
        self.color_carro = nuevo_color_carro

    
  
    def mostrar_info(self):
        print(f"placa_carro es: {self.placa_carro}")
        print(f"tipo_carro es: {self.placa_carro}")
        print(f"color_carro es: {self.color_carro}")
        
        