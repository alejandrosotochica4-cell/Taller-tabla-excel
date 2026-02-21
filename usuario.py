class Usuario:
    def __init__(self, ID,nombre,Tipo_usuario):
        self.ID = ID
        self.nombre = nombre
        self.Tipo_usuario = Tipo_usuario

    def get_ID(self):
        return self.ID
    
    def set_ID(self, nuevo_ID):
        self.ID = nuevo_ID

    def get_nombre(self):
        return self.nombre 
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_tipo_usuario(self):
        return self.Tipo_usuario
    
    def set_tipo_usuario(self, nuevo_tipo_usuario):
        self.Tipo_usuario = nuevo_tipo_usuario

    def mostar_info(self):
        print(f"ID: {self.ID}")
        print(f"nombre: {self.nombre}")
        print(f"tipo_usuario: {self.Tipo_usuario}")