"""Update Migration

Revision ID: 85b92d90901b
Revises: 3472ce625862
Create Date: 2022-05-17 10:57:39.726934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85b92d90901b'
down_revision = '3472ce625862'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
