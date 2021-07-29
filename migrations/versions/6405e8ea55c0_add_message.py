"""add message

Revision ID: 6405e8ea55c0
Revises: 268068105b91
Create Date: 2021-07-27 09:44:50.307851

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6405e8ea55c0'
down_revision = '268068105b91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('is_checked', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'is_checked')
    # ### end Alembic commands ###
