from odoo import models, fields

class MrpBomLine(models.Model):
    _inherit = 'mrp.bom.line'

    modular_type_id = fields.Many2one(
        'modular.type',
        string='Module Type'
    )

class StockMove(models.Model):
    _inherit = 'stock.move'

    modular_type_id = fields.Many2one(
        'modular.type',
        string='Module Type'
    )
