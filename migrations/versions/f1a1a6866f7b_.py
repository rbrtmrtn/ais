"""empty message

Revision ID: f1a1a6866f7b
Revises: 5963d86b0ff5
Create Date: 2017-07-12 16:00:21.541357

"""

# revision identifiers, used by Alembic.
revision = 'f1a1a6866f7b'
down_revision = '5963d86b0ff5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service_area_point', sa.Column('seg_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service_area_point', 'seg_id')
    ### end Alembic commands ###
