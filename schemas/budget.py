from marshmallow import Schema, fields

class BudgetSchema(Schema):
    id               = fields.Int(dump_only=True)
    project_id       = fields.Int()
    budget_status_id = fields.Int()
    name             = fields.Str()
    created_by_id    = fields.Int()
    creation_date    = fields.DateTime()
    approved_by_id   = fields.Int()
    approved_date    = fields.DateTime()