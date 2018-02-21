from odoo import models, fields

class Juguetes(models.Model):
	_name = 'juguetes.juguetes'
	codigo  = fields.Char('Codigo', required=True)
	nombre = fields.Char('Nombre', required=True)
	precio = fields.Float('Precio', required=True)
	stock = fields.Integer('Stock',required=True)
	
	def name_get(self):
		res=[]
		for record in self:
			name = record.nombre
			res.append((record.id, name))
		return res