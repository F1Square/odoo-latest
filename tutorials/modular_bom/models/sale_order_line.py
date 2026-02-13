from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    modular_value_ids = fields.One2many(
        'sale.order.line.modular.value',
        'sale_line_id',
        string='Modular Values'
    )
    
    def action_open_modular_values_wizard(self):
        self.ensure_one()
        # Ensure all modular types from the product have a corresponding value record
        existing_types = self.modular_value_ids.mapped('modular_type_id')
        missing_types = self.product_id.modular_type_ids - existing_types
        if missing_types:
            self.write({
                'modular_value_ids': [
                    (0, 0, {'modular_type_id': m_type.id, 'value': 1.0})
                    for m_type in missing_types
                ]
            })
        
        return {
            'name': 'Set modular type values',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.line',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('modular_bom.view_set_modular_values_form').id,
        }

    def action_confirm_modular_values(self):
        return {'type': 'ir.actions.act_window_close'}

class SaleOrderLineModularValue(models.Model):
    _name = 'sale.order.line.modular.value'
    _description = 'Sale Order Line Modular Value'

    sale_line_id = fields.Many2one('sale.order.line', string='Sale Line', ondelete='cascade')
    modular_type_id = fields.Many2one('modular.type', string='Modular Type', required=True)
    value = fields.Float(string='Value', default=1.0)
