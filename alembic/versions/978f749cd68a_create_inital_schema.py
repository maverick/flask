"""create inital schema

Revision ID: 978f749cd68a
Revises: 
Create Date: 2021-11-16 21:12:42.022088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import DefaultGenerator, ForeignKey, MetaData, Table


# revision identifiers, used by Alembic.
revision = '978f749cd68a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Anything named *_id should be a foreign key back to its respect object.
    # They're only here to foster conversation about the schema as a whole 
    # and because leaving them out seemed like an obvious miss.
    budget = op.create_table(
        'budget',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('project_id', sa.Integer, default=0),           
        sa.Column('budget_status_id',sa.SmallInteger, default=0),
        sa.Column('name',sa.String(128), nullable=False),
        sa.Column('created_by_id',sa.Integer, default=0),
        sa.Column('creation_date',sa.DateTime, server_default=sa.func.current_timestamp()),
        sa.Column('approved_by_id',sa.Integer, default=0),        
        sa.Column('approved_date',sa.DateTime, nullable=True)
    )

    budget_item_status = op.create_table(
        'budget_item_status',
        sa.Column('id',sa.SmallInteger, primary_key=True),
        sa.Column('name',sa.String(128), nullable=False),
        sa.Column('sort_order',sa.SmallInteger, nullable=False)
    )

    op.bulk_insert(
        budget_item_status,
        [
            {'id': 1, 'name': 'New',              'sort_order': 1},
            {'id': 2, 'name': 'Quotes Requested', 'sort_order': 2},
            {'id': 3, 'name': 'Quote Accepted',   'sort_order': 3},
            {'id': 4, 'name': 'Funds Requested',  'sort_order': 4},
            {'id': 5, 'name': 'Funds Rejected',   'sort_order': 5},
            {'id': 6, 'name': 'Funds Pending',    'sort_order': 6},
            {'id': 7, 'name': 'Funds Acquired',   'sort_order': 7},
        ]
    )

    budget_item = op.create_table(
        'budget_item',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('budget_id', sa.Integer, ForeignKey('budget.id')),
        sa.Column('budget_item_status_id', sa.SmallInteger, ForeignKey('budget_item_status.id')),
        sa.Column('project_task_id', sa.Integer),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('request_amount', sa.Numeric(8,2)),
        sa.Column('granted_amount', sa.Numeric(8,2), nullable=True),
        sa.Column('latest_funding_date', sa.DateTime, nullable=False),
        sa.Column('funding_source_id', sa.Integer),
        sa.Column('funded_date', sa.DateTime, nullable=True),
        sa.Column('approved_by_id',sa.Integer, nullable=True),        
        sa.Column('approved_date',sa.DateTime, nullable=True)
    )

    # ...and then we'll need a child table to hold the quotes from the vendors for each budget item.

    # Sample data
    op.bulk_insert(
        budget,
        [
            {
                'id': 1, 
                'project_id': 4, 
                'budget_status_id': 5, 
                'name': 'Example Budget', 
                'created_by_id': 21,
                'created_date': '2021-11-01 14:23:00'
            }
        ]
    )

    op.bulk_insert(
        budget_item,
        [
            {
                'id': 1, 
                'budget_id': 1,
                'budget_item_status_id': 2,
                'project_task_id': 3,
                'name': 'Earthwork',
                'request_amount': 10000,
                'granted_amount': None,
                'latest_funding_date': '2022-01-01 00:00:00',
                'funding_source_id': 7,
                'funded_date': None,
                'approved_by_id': None,
                'approved_date': None
            },
            {
                'id': 2, 
                'budget_id': 1,
                'budget_item_status_id': 1,
                'project_task_id': 4,
                'name': 'Foundation',
                'request_amount': 10000,
                'granted_amount': None,
                'latest_funding_date': '2022-02-01 00:00:00',
                'funding_source_id': 7,
                'funded_date': None,
                'approved_by_id': None,
                'approved_date': None
            }
        ]
    )

def downgrade():
    pass
