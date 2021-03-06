"""create shop table

Revision ID: 5e9aaad2401f
Revises: 6db7b9f38d12
Create Date: 2018-07-19 18:02:49.189740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e9aaad2401f'
down_revision = '6db7b9f38d12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seller_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('shop_name', sa.String(length=32), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('shop_logo', sa.String(length=128), nullable=True),
    sa.Column('shop_rating', sa.Float(), nullable=True),
    sa.Column('is_brand', sa.Boolean(), nullable=True),
    sa.Column('is_ontime', sa.Boolean(), nullable=True),
    sa.Column('is_bird', sa.Boolean(), nullable=True),
    sa.Column('is_bao', sa.Boolean(), nullable=True),
    sa.Column('is_fp', sa.Boolean(), nullable=True),
    sa.Column('is_zun', sa.Boolean(), nullable=True),
    sa.Column('start_cost', sa.Float(), nullable=True),
    sa.Column('send_cost', sa.Float(), nullable=True),
    sa.Column('notice', sa.String(length=210), nullable=True),
    sa.Column('discount', sa.String(length=210), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['seller_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seller_shop')
    # ### end Alembic commands ###
