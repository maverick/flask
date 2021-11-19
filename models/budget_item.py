from app import db

from models.budget_item_status import BudgetItemStatus

class BudgetItem(db.Model):
    id                    = db.Column('id', db.Integer, primary_key=True)
    budget_id             = db.Column('budget_id', db.Integer, db.ForeignKey('budget.id'))
    budget_item_status_id = db.Column('budget_item_status_id', db.SmallInteger, db.ForeignKey('budget_item_status.id'))
    budget_item_status    = db.relationship('BudgetItemStatus')
    project_task_id       = db.Column('project_task_id', db.Integer, default=0)
    name                  = db.Column('name', db.String(128), nullable=False)
    request_amount        = db.Column('request_amount', db.Numeric(8,2))
    granted_amount        = db.Column('granted_amount', db.Numeric(8,2))

class BudgetItemFull(BudgetItem):
    latest_funding_date   = db.Column('latest_funding_date', db.DateTime, nullable=False)
    funding_source_id     = db.Column('funding_source_id', db.Integer, default=0)
    funded_date           = db.Column('funded_date', db.DateTime, nullable=False)
    approved_by_id        = db.Column('approved_by_id',db.Integer, default=0)
    approved_date         = db.Column('approved_date',db.DateTime, nullable=True)

    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)