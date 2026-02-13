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
        related='bom_line_id.modular_type_id',
        string='Module Type',
        store=True,
        readonly=True
    )
