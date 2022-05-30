from odoo import models, fields, api
from odoo.osv import expression


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_number = fields.Char(string='Task number', required=True, readonly=True, default='New', copy=False)

    @api.model
    def create(self, vals):
        if vals.get('task_number', ('New')) == ('New'):
            vals['task_number'] = self.env['ir.sequence'].next_by_code('project.task') or ('New')
        result = super(ProjectTask, self).create(vals)
        return result

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, (f'[{record.task_number}] {record.name} - {record.project_id.name}')))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if not args[0][2]:
            args = []
        domain = args + ['|', ('name', operator, name), ('task_number', operator, name)]
        return super(ProjectTask, self).search(domain, limit=limit).name_get()

    def post_hook(self):
        for record in self.search([]):
            record.task_number = self.env['ir.sequence'].next_by_code(
                'project.task')
