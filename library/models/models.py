# -*- coding: utf-8 -*-

from odoo import models, fields, api

class library(models.Model):
     _name = 'library.library'

     name = fields.Char()

     description = fields.Text()

