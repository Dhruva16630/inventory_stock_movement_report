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
        "stock.picking.type",
        string="Picking Type",
        readonly = True
    )
    
    warehouse = fields.Many2one(
        "res.partner",
        string="Warehouse",
        readonly = True
    )
    
    
    def init(self):
        tools.drop_view_if_exists(
            self.env.cr,
            self._table
        )
        
        self.env.cr.execute("""
            CREATE VIEW inventory_stock_movement_report AS(
                SELECT
                    sm.id AS id,
                    pp.id AS product,
                    pt.categ_id AS product_category,
                    sm.product_uom_qty AS qty,
                    sl.id AS source_location,
                    sld.id AS destination_location,
                    sm.reference AS reference,
                    sm.date AS scheduled_date,
                    sm.state AS state,
                    spt.id AS picking_type,
                    sw.id AS warehouse
                    
                FROM stock_move sm
                
                JOIN product_product pp
                    ON pp.id = sm.product_id
                
                JOIN product_template pt
                    ON pt.id = pp.product_tmpl_id
                
                JOIN stock_location sl
                    ON sl.id = sm.location_id
                    
                JOIN stock_location sld 
                    ON sld.id = sm.location_dest_id
                
                JOIN stock_picking sp 
                    ON sp.id = sm.picking_id
                
                JOIN stock_picking_type spt
                    ON spt.id = sp.picking_type_id
                
                JOIN stock_warehouse sw
                    ON sw.id = sm.warehouse_id
            )
        """)