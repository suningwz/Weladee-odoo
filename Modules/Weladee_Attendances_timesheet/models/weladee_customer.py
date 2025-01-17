# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging
_logger = logging.getLogger(__name__)

from odoo import osv
from odoo import models, fields, api

class weladee_partner(models.Model):
    _inherit = 'res.partner'

    weladee_id = fields.Char(string="Weladee ID",copy=False)
    name_thai = fields.Char(string='Name(thai)')
    customer_rank = fields.Integer(default=0, copy=False)