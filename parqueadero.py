class Parqueadero:
    def __init__(self, puesto, fecha_entrada, hora_entrada, hora_salida, estado):
        self.puesto = puesto
        self.fecha_entrada = fecha_entrada
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
        self.estado = estado
        self.texto_tabla = ""

    def get_puesto(self):
        return self.puesto
    
    def set_puesrto(self, nuevo_puesto):
        self.puesto = nuevo_puesto
    
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_fecha_entrada(self, nueva_fecha_entrada):
        self.fecha_entrada = nueva_fecha_entrada

    def get_hora_entrada(self):
        return self.hora_entrada
    
    def set_hora_entrda(self, nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada

    def get_hora_salida(self):
        return self.hora_salida 
    
    def set_hora_salida(self, nueva_hora_salida):
        self.hora_salida = nueva_hora_salida

    def get_estado(self):
        return self.estado
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def get_texto_tabla(self):
        return self.texto_tabla
    
    def set_texto_tabla(self, nueva_texto_tabla):
        self.texto_tabla = nueva_texto_tabla

    def mostrar_info(self):
        print(f"puesto: {self.puesto}")
        print(f"fecha_entrada: {self.fecha_entrada}")
        print(f"hora_entrada: {self.hora_entrada}")
        print(f"hora_salida: {self.hora_salida}")
        print(f"estado: {self.estado}")
        print(f"texto_tabla: {self.texto_tabla}")

    def acumular_info(self, obj_usuario, obj_carro):
        self.texto_tabla+=f"ID: {obj_usuario.get_ID()}\nNombre: { obj_usuario.get_nombre()}\ntipo usuario: {obj_usuario.get_tipo_usuario()}\nPlaca Carro: {obj_carro.get_placa_carro()}\nTipo Caro: {obj_carro.get_tipo_carro()}\nColor Carro: {obj_carro.get_color_carro()}\nPuesto: {self.puesto}\nFecha entrada: {self.fecha_entrada}\nHora entrada: {self.hora_entrada}\nHora salida: {self.hora_salida}\nEstado: {self.estado}"
 
    def mostrar_tabla(self):
        print(self.texto_tabla)

    
