from app import db

class BudgetItemStatus(db.Model):
    id         = db.Column('id', db.SmallInteger, primary_key=True)
    name       = db.Column('name', db.String(128), nullable=False)
    sort_order = db.Column('sort_order', db.SmallInteger, nullable=False)