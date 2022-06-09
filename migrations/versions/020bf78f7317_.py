"""empty message

Revision ID: 020bf78f7317
Revises: fa1b4f23ed6f
Create Date: 2022-06-06 23:57:22.187196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '020bf78f7317'
down_revision = 'fa1b4f23ed6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.String(length=500), nullable=True))
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###