from datetime import datetime, time

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InventoryStockMovementRportWizard(models.TransientModel):
    _name = "inventory.stock.movement.report.wizard"
    _description ="Inventory Stock Movement Report Wizard"
    
    from_date = fields.Date(
        string="From Date",
        required = True
    )
    
    to_date = fields.Date(
        string="To Date",
        required = True
    )
    
    @api.constrains("from_date", "to_date")
    def _check_dates(self):
        for record in self:
            if record.from_date > record.to_date:
                raise ValidationError(
                    "From Date cannot be later than To Date."
                )

    def action_generate_report(self):
        self.ensure_one()

        from_datetime = datetime.combine(
            self.from_date,
            time.min,
        )

        to_datetime = datetime.combine(
            self.to_date,
            time.max,
        )

        return {
            "type": "ir.actions.act_window",
            "name": "Stock Movement Report",
            "res_model": "inventory.stock.movement.report",
            "view_mode": "list,graph,pivot",
            "domain": [
                ("scheduled_date", ">=", from_datetime),
                ("scheduled_date", "<=", to_datetime),
            ],
        }