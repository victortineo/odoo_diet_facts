# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.product.models import product_template

class Restaurants(models.Model):
    _name = 'dietfacts.restaurant'
    name = fields.Char(string='Nome', required=True)
    description = fields.Char(string='Descrição', required=True)

class Facts(models.Model):
    _name = 'dietfacts.facts'
    name = fields.Char(string='facts', required=True)
    foods = fields.Many2many('dietfacts.foods', string='Foods', ondelete='set null')
    quantity = fields.Float(string='Quantidade', required=True, digits=(3, 2), help="Quantidade de g/mg no alimento")

class Foods(models.Model):
    _name = 'dietfacts.foods'
    name = fields.Char(string='Nome', required=True)
    restaurant = fields.Many2one('dietfacts.restaurant', string='Restaurantes', ondelete='set null')
    facts = fields.One2many('dietfacts.facts', 'id', string='Facts')
