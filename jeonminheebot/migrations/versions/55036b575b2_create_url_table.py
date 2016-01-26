"""create url table

Revision ID: 55036b575b2
Revises: 
Create Date: 2016-01-27 04:19:52.506373

"""

# revision identifiers, used by Alembic.
revision = '55036b575b2'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'url',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(300), nullable=False)
    )


def downgrade():
    op.drop_table('url')
