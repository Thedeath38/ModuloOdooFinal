from odoo import models, fields

class Juguetes(models.Model):
	_name = 'juguetes.empleados'
	codigo  = fields.Char('Codigo', required=True)
	nombre = fields.Char('Nombre', required=True)
	dni = fields.Char('DNI', required=False)
	telefono = fields.Integer('Telefono',required=False)
	direccion = fields.Char('Direccion',required=False)
	def name_get(self):
		res=[]
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res
