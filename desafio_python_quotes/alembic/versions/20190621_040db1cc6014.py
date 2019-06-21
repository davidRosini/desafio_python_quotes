"""init

Revision ID: 040db1cc6014
Revises: 
Create Date: 2019-06-21 01:27:34.167843

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '040db1cc6014'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.Text(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.Column('page', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_history_session'))
    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history_session')
    # ### end Alembic commands ###
