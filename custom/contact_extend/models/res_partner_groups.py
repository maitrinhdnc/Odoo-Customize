from odoo import models, fields, api


class ResPartnerGroups(models.Model):
    _name = 'res.partner.groups'
    _description = 'Contact Groups'

    name = fields.Char(required=True)
    code = fields.Char(size=3, required=True)
    state_id = fields.Many2one('res.country.state')
    country_id = fields.Many2one('res.country', related='state_id.country_id')
    contact_count = fields.Integer(compute='_compute_contact_count',
                                   store=True)
    partner_ids = fields.One2many('res.partner', 'group_id', string='Partners')

    @api.depends('partner_ids')
    def _compute_contact_count(self):
        for group in self:
            group.contact_count = self.env['res.partner'].search_count(
                [('group_id', '=', group.id)])
