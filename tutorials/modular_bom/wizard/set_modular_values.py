from odoo import models, fields, api

class SetModularValuesWizard(models.TransientModel):
    _name = 'set.modular.values.wizard'
    _description = 'Set Modular Type Values'

    sale_line_id = fields.Many2one('sale.order.line', string='Sale Line')
    line_ids = fields.One2many('set.modular.values.line.wizard', 'wizard_id', string='Values')

    def action_confirm(self):
        self.ensure_one()
        # Clear existing values on the sale line
        self.sale_line_id.modular_value_ids.unlink()
        # Create new values
        vals = []
        for line in self.line_ids:
            vals.append((0, 0, {
                'modular_type_id': line.modular_type_id.id,
                'value': line.value
            }))
        self.sale_line_id.write({'modular_value_ids': vals})
        return {'type': 'ir.actions.act_window_close'}

class SetModularValuesLineWizard(models.TransientModel):
    _name = 'set.modular.values.line.wizard'
    _description = 'Set Modular Type Value Line'

    wizard_id = fields.Many2one('set.modular.values.wizard', string='Wizard')
    modular_type_id = fields.Many2one('modular.type', string='Modular Type', readonly=True)
    value = fields.Float(string='Value', default=1.0)
