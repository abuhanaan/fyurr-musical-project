"""empty message

Revision ID: fa1b4f23ed6f
Revises: 5b81c1ed49e8
Create Date: 2022-06-04 18:13:08.485749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa1b4f23ed6f'
down_revision = '5b81c1ed49e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.drop_column('Venue', 'genre')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genre', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
