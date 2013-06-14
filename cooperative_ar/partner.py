#! -*- coding: utf8 -*-
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Partner']

class Partner(ModelSQL, ModelView):
    "cooperative_ar"
    __name__ = "cooperative.partner"
    file = fields.Integer('File')
    party = fields.Many2One('party.party', 'Party')
    company = fields.Many2One('company.company', 'Company')
    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    dni = fields.Char('DNI')
    nationality = fields.Selection([('argentina', 'Argentina'), ('chile', 'Chile'), ('colombia', 'Colombia'), ], 'Nationality')
    marital_status = fields.Selection([('soltero', 'Soltero'), ('casado', 'Casado'), ('viudito', 'Viudito'), ], 'Marital Status')
    incorporation_date = fields.Date('Incorporation Date')
    vacation_days = fields.Integer('Vacation Days')
    vacation = fields.One2Many('cooperative.partner.vacation', 'partner', 'Vacation')
    meeting = fields.Many2Many('cooperative.partner-meeting', 'partner', 'meeting', 'Meeting')

