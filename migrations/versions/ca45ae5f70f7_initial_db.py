"""Initial DB

Revision ID: ca45ae5f70f7
Revises: 
Create Date: 2020-08-15 21:50:16.851255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca45ae5f70f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('diputy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('dni', sa.String(length=20), nullable=True),
    sa.Column('sex', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'lastname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diputy')
    # ### end Alembic commands ###