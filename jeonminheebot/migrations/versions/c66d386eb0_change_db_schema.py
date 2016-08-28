"""change db schema

Revision ID: c66d386eb0
Revises: 315f4581606
Create Date: 2016-08-28 21:33:48.208991

"""

# revision identifiers, used by Alembic.
revision = 'c66d386eb0'
down_revision = '315f4581606'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_table('url')

    op.create_table(
        'url',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(300), nullable=False),
        sa.Column('href', sa.String(500), nullable=False)
    )


def downgrade():
    op.drop_table('url')
    op.create_table(
        'url',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(300), nullable=False)
    )
