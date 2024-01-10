# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    visible_backspace_btn = fields.Boolean()


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_data_process(self, loaded_data):
        res = super(PosSession, self)._pos_data_process(loaded_data)
        loaded_data['visibleBackspaceBtn'] = self.config_id.visible_backspace_btn
        return res
