from odoo import models, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def _get_move_raw_values(self, product, product_uom_qty, product_uom, operation_id=False, bom_line=False):
        res = super()._get_move_raw_values(product, product_uom_qty, product_uom, operation_id, bom_line)
        if bom_line and bom_line.modular_type_id and self.sale_line_id:
            modular_value = self.sale_line_id.modular_value_ids.filtered(
                lambda v: v.modular_type_id == bom_line.modular_type_id
            )[:1]
            if modular_value:
                res['product_uom_qty'] = res.get('product_uom_qty', product_uom_qty) * modular_value.value
            res['modular_type_id'] = bom_line.modular_type_id.id
        return res
