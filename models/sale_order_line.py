from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_number = fields.Integer(string="Sequence", compute="_compute_line_number")

    def _compute_line_number(self):
        for index, rec in enumerate(self, start=1):
            rec.order_number = index

