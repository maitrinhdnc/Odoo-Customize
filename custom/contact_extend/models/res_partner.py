from odoo import models, fields, api
from odoo.exceptions import ValidationError  # type: ignore


class ResPartner(models.Model):
    _inherit = "res.partner"

    group_id = fields.Many2one("res.partner.groups", string="Group")

    def write(self, vals):
        user_has_contact_user_group = self.env.user.has_group(
            'contact_extend.group_contact_user')
        user_has_contact_manager_group = self.env.user.has_group(
            'contact_extend.group_contact_manager')

        if user_has_contact_user_group and not user_has_contact_manager_group:
            for record in self:
                current_state_id = vals.get("state_id", record.state_id.id)

                if record.group_id:
                    group_state_id = record.group_id.state_id.id
                    if current_state_id != group_state_id:
                        raise ValidationError(
                            "Users in the Contact Users group can only edit "
                            " res.partner records if state_id matches the "
                            "state_id of the group's state.")
                else:
                    raise ValidationError(
                        "This record does not belong to any group, so it "
                        "cannot be edited by users in the Contact Users group."
                    )

        result = super(ResPartner, self).write(vals)
        return result

