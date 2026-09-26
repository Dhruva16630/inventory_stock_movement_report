from odoo import models, fields, tools

class InventoryStockMovementReport(models.Model):
    _name = "inventory.stock.movement.report"
    _description = "Inventory Stock Movement Report"
    _auto = False
    
    # fields are grouped in according to tables names
    
    # stock.move(base model)
    qty = fields.Float(
        string="Quantity",
        readonly = True
    )
    
    # stock.picking
    source_location = fields.Many2one(
        "stock.location",
        string="Source Location",
        readonly = True
    )
    
    destination_location = fields.Many2one(
        "stock.location",
        string="Destination Location",
        readonly = True
    )
    
    reference = fields.Char(
        string="Reference",
        readonly = True
    )
    
    scheduled_date = fields.Datetime(
        string="Scheduled Date",
        readonly = True
    )
    
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('waiting', 'Waiting Another Operation'),
            ('confirmed', 'Waiting'),
            ('assigned', 'Ready'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ],
        string="State",
        readonly = True
    )
    
    picking_type = fields.Many2one(
        "stock.package.type",
        string="Picking Type",
        readonly = True
    )
    
    warehouse = fields.Many2one(
        "res.partner",
        string="Warehouse",
        readonly = True
    )
    
    # -----------------
    product = fields.Many2one(
        "product.product",
        string="Product",
        readonly = True
    )
    
    product_category = fields.Many2one(
        "product.category",
        string="Product Category",
        readonly = True
    )