from marshmallow import Schema, fields

from schemas.budget_item_status import BudgetItemStatusSchema

class BudgetItemSchema(Schema):
    id                    = fields.Int(dump_only=True)
    budget_id             = fields.Int()
    budget_item_status_id = fields.Int()
    budget_item_status    = fields.Nested(BudgetItemStatusSchema,only=("name",), many=False, dump_only=True)
    project_task_id       = fields.Int()
    name                  = fields.Str(required=True)
    request_amount        = fields.Number()
    granted_amount        = fields.Number()

class BudgetItemFullSchema(BudgetItemSchema):
    latest_funding_date   = fields.DateTime(required=True)
    funding_source_id     = fields.Int()
    funded_date           = fields.DateTime()
    approved_by_id        = fields.Int()
    approved_date         = fields.DateTime()