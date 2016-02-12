"""alter url column name

Revision ID: 315f4581606
Revises: 55036b575b2
Create Date: 2016-02-12 18:06:35.765301

"""

# revision identifiers, used by Alembic.
revision = '315f4581606'
down_revision = '55036b575b2'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_table('url')
    op.create_table(
        'url',
        sa.Column('url_id', sa.Integer, primary_key=True),
        sa.Column('classname', sa.String(300), nullable=False),
        sa.Column('href', sa.String(500), nullable=False),
        sa.Column('title', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('url')
    op.create_table(
        'url',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(300), nullable=False)
    )
