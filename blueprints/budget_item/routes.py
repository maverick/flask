from flask import Blueprint, request
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError

from app import db

from models.budget      import Budget
from models.budget_item import BudgetItem, BudgetItemFull

from schemas.budget_item import BudgetItemSchema, BudgetItemFullSchema

budget_item_bp = Blueprint('budget_item_bp', __name__)

budget_item_schema = BudgetItemSchema(many=True)
budget_item_full_schema = BudgetItemFullSchema(many=False)

@budget_item_bp.route('<int:budget_id>/item', methods=['GET'])
def list_items(budget_id):
    try:
        rows = BudgetItem.query.filter(BudgetItem.budget_id == budget_id).all()
    except NoResultFound:
        return { "message": "No Such Budget."}, 404

    return {
        "data": budget_item_schema.dump(rows),
        "count": len(rows)
    }


@budget_item_bp.route('<int:budget_id>/item', methods=['POST'])
def create_item(budget_id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400

    json_data['budget_id'] = budget_id
    try:
        data = budget_item_full_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 422

    budget = Budget.query.filter(Budget.id == budget_id).first()
    if budget is None:
        return {"message": "Invalid Budget Id"}, 422

    budget_item = BudgetItemFull(data)
    db.session.add(budget_item)
    db.session.commit()

    return {
        "message": "record created",
        "data": budget_item_full_schema.dump(BudgetItem.query.get(budget_item.id))
    }


@budget_item_bp.route('<int:budget_id>/item/<int:item_id>', methods=['GET'])
def get_item(budget_id, item_id):
    try:
        row = BudgetItemFull.query.filter(BudgetItemFull.budget_id == budget_id and BudgetItemFull.id == item_id).first()
    except NoResultFound:
        return { "message": "No Such Budget Item"}, 404

    return budget_item_full_schema.dump(row)


@budget_item_bp.route('<int:budget_id>/item/<int:item_id>', methods=['PUT'])
def update_item(budget_id, item_id):
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400

    json_data['budget_id'] = budget_id
    try:
        data = budget_item_full_schema.load(json_data, partial=True)
    except ValidationError as err:
        return err.messages, 422

    row = BudgetItemFull.query.filter(BudgetItemFull.budget_id == budget_id and BudgetItemFull.id == item_id).first()
    if row is None:
        return {"message": "Invalid Budget Id"}, 422

    for key,value in data.items():
        setattr(row,key,value)

    db.session.commit()

    return {
        "message": "record updated",
        "data": budget_item_full_schema.dump(BudgetItem.query.get(row.id))
    }


@budget_item_bp.route('<int:budget_id>/item/<int:item_id>', methods=['DELETE'])
def remove_item(budget_id, item_id):
    try:
        budget_item = BudgetItem.query.filter(BudgetItem.budget_id == budget_id and BudgetItem.id == item_id).first()
    except NoResultFound:
        return { "message": "No Such Budget Item"}, 404

    db.session.delete(budget_item)
    db.session.commit()

    return {
        "message": "record deleted"
    }