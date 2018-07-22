"""add cate

Revision ID: 03c047cb6cb2
Revises: 5e9aaad2401f
Create Date: 2018-07-20 10:24:33.550260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03c047cb6cb2'
down_revision = '5e9aaad2401f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('is_default', sa.Boolean(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shop_id'], ['seller_shop.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu_category')
    # ### end Alembic commands ###
