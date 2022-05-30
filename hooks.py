from odoo import api, SUPERUSER_ID


def _task_number_post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["project.task"].post_hook()
