from marshmallow import Schema, fields

class BudgetItemStatusSchema(Schema):
    id         = fields.Int(dump_only=True)
    name       = fields.Str()
    sort_order = fields.Int