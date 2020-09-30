# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from datetime import datetime
import calendar

class AccountCheckInherit(models.Model):
    _inherit = 'account.check'

    dias_restantes = fields.Integer(compute='_get_dias_restantes', string="Días Restantes")

    @api.depends('payment_date')
    def _get_dias_restantes(self):
        for record in self:
            if record.payment_date:
                payment_date = record.payment_date
                fecha_hoy = datetime.now().strftime('%Y-%m-%d')
                numero_de_dias = (
                        fields.Date.from_string(payment_date) -
                        fields.Date.from_string(fecha_hoy)).days
                if numero_de_dias > 0:
                    record.dias_restantes = numero_de_dias
                else:
                    record.dias_restantes = numero_de_dias
