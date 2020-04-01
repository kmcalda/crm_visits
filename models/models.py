from odoo import models, fields

class Visits(models.Model):
    _name = 'visits.menu'

    customer_name = fields.Char(string='Customer name')