from odoo import models, api, fields


class FieldsRequired(models.Model):
    _inherit = "ir.model.fields"

    property_required = fields.Boolean(string="Required", compute="_is_required", store="True")

    @api.depends("required")
    def _is_required(self):
        for record in self:
            if record.required:
                record.property_required = True
            else:
                record.property_required = False




