from app import db

class Budget(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    project_id = db.Column('project_id', db.Integer, default=0)
    budget_status_id = db.Column('budget_status_id', db.SmallInteger, default=0)
    name = db.Column('name', db.String(128), nullable=False)
    created_by_id = db.Column('created_by_id', db.Integer, default=0)
    creation_date = db.Column('creation_date', db.DateTime, server_default=db.func.current_timestamp())
    approved_by_id = db.Column('approved_by_id', db.Integer, default=0)
    approved_date = db.Column('approved_date', db.DateTime, nullable=True)