from odoo import models, fields, tools

class InventoryStockMovementReport(models.Model):
    _name = "inventory.stock.movement.report"
    _description = "Inventory Stock Movement Report"
    _auto = False