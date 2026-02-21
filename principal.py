from parqueadero import Parqueadero
from usuario import Usuario
from carro import Carro

obj_usuario = Usuario("37444080","Alejandro","cliente")
obj_parqueadero = Parqueadero("4", "19/02/2026", "05:45", "07:45", "ocupado")
obj_carro = Carro("H3E-56G", "sedan", "Rojo")

obj_parqueadero.acumular_info(obj_usuario, obj_carro)
obj_parqueadero.mostrar_tabla()