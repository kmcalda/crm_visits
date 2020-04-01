from odoo import models, fields, api
import requests


class Visits(models.Model):
    _name = 'visits.menu'
    _rec_name = 'customer_name'

    customer_name = fields.Char('Customer name')
    geo_latitude = fields.Float('Lattitude', digits=(3, 6), readonly=True)
    geo_longitude = fields.Float('Longitude', digits=(3, 6), readonly=True)

    @api.constrains('customer_name')
    def geolocation_function(self):
        lat, long = requests.get('http://ipinfo.io').json()['loc'].split(",")
        for geo in self:
            if geo.customer_name:
                geo.geo_latitude, geo.geo_longitude = float(lat),float(long)
