class Pizzeria:
	def __init__(self,pedidos=[],pizzas=[],clientes=[]):
		self.pedidos=pedidos
		self.pizzas=pizzas
		self.clientes=clientes
	def cargarPedido(self):
		"""metodo para cargar un pedido"""

	def cargarPizza(self):
		"""metodo para cargar pizzas"""
	def cargarCliente(self):
		"""metodo para cargar cliente"""


class Pizza:
	mediana=0.1
	grande=0.15
	piedra=0.05
	molde=0.03
	parrilla=0.03
	def __init__(self,nombre,ingredientes,porciones,tipo,precio):
		self.nombre=nombre
		self.ingredientes=ingredientes
		self.porciones=porciones
		self.tipo=tipo
		self.precio=precio
	def calcularPrecio(self):
		"""metodo para calcular el precio de la pizza segun el tipo y el tama;o"""


import datetime
class Pedido:
	def __init__(self,numero,cliente,fechaHora,horaEst,detalle=[],total=0):
		self.numero=numero
		self.cliente=cliente
		self.fechaHora=fechaHora
		self.horaEst=horaEst
		self.detalle=detalle
		self.total=total
	def calcularPrecio(self):
		"""calcular el total del pedido"""
	def pedidosPorPeriodo(self,fechaIni,fechaFin):
		"""metodo para alistar los pedidos de un periodo determinado"""


class DetallePedido:
	def __init__(self,cant,pizza,subtotal=0):
		self.cant=cant
		self.pizza=pizza
		self.subtotal=subtotal
	def calcularSubtotal(self):
		"""metodo para calcular el subtotal del detalle en base a la cantidad y precio de las pizzas"""

class Cliente:
	def __init__(self,nombre,telefono="",direccion=""):
		self.nombre=nombre
		self.telefono=telefono
		self.direccion=direccion
