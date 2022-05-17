"""Update Migration

Revision ID: 3472ce625862
Revises: eb11f4f62298
Create Date: 2022-05-17 10:56:29.616780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3472ce625862'
down_revision = 'eb11f4f62298'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
