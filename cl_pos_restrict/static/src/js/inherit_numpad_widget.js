/** @odoo-module **/

import { Order, Orderline, PosGlobalState} from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';

const PosBackSpaceBtnRestrict = (PosGlobalState) => class PosBackSpaceBtnRestrict extends PosGlobalState {
    //@override
    async _processData(loadedData) {
        await super._processData(...arguments);
        this.visibleBackspaceBtn = loadedData['visibleBackspaceBtn']
    }
}

Registries.Model.extend(PosGlobalState, PosBackSpaceBtnRestrict)