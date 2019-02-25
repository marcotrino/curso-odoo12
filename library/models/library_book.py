# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    _name= "library.book"

    name = fields.Char(string="Book", required=False, )
    description = fields.Text(string="Description", required=False, )
