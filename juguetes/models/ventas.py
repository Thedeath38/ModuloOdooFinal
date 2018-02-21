from odoo import models, fields, api

class Juguetes(models.Model):
	_name = 'juguetes.ventas'
	vcodigo  = fields.Integer('Codigo', required=True)
	vempleado = fields.Many2one('juguetes.empleados', 'Empleado')
	vjuguete = fields.Many2one('juguetes.juguetes', 'Juguete')
	vcliente = fields.Many2one('juguetes.clientes', 'Cliente')
	vtotal = fields.Float('Total')
	vpagado = fields.Boolean('pagada')
	
	@api.one
	def pagado(self):
		self.vpagado=True
		return True