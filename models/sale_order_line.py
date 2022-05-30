from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_line_number = fields.Integer(string="Sequence", compute="_compute_line_number", store=True)

    # Реализация George
    @api.depends('order_id.order_line', 'sequence')
    def _compute_line_number(self):
        orders = self.mapped('order_id')
        for order in orders:
            number = 1
            for rec in order.order_line.sorted(key=lambda r: r.sequence):
                rec.order_line_number = number
                number += 1


# Моя реализация
'''
@api.depends("order_id.order_line")
def _compute_line_number(self):
    iteration = 0
    line_number = 1
    for sale_order_line in self:
        if iteration == 0:  # Первая итерация
            # Первая строка равна одному
            sale_order_line.order_line_number = line_number
            # сохраняем текущую строку в качестве предыдущей для последующих итераций
            prev_sale_order_line = sale_order_line
            iteration = 1

            # Проверяем принадлежат ли текущая и предыдущая строки к одному заказу
        elif sale_order_line.order_id == prev_sale_order_line.order_id:
            line_number += 1
            sale_order_line.order_line_number = line_number
            prev_sale_order_line = sale_order_line

            # Начало нового заказа
        else:
            line_number = 1
            sale_order_line.order_line_number = line_number
            prev_sale_order_line = sale_order_line

'''
