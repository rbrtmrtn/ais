"""Add indexes to dor/pwd parcel_ids and opa account_num

Revision ID: fa0da524430f
Revises: 7935034cef61
Create Date: 2017-03-24 10:41:05.528151

"""

# revision identifiers, used by Alembic.
revision = 'fa0da524430f'
down_revision = '7935034cef61'

from alembic import op

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_dor_parcel_parcel_id'), 'dor_parcel', ['parcel_id'], unique=False)
    op.create_index(op.f('ix_opa_property_account_num'), 'opa_property', ['account_num'], unique=False)
    op.create_index(op.f('ix_pwd_parcel_parcel_id'), 'pwd_parcel', ['parcel_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pwd_parcel_parcel_id'), table_name='pwd_parcel')
    op.drop_index(op.f('ix_opa_property_account_num'), table_name='opa_property')
    op.drop_index(op.f('ix_dor_parcel_parcel_id'), table_name='dor_parcel')
    ### end Alembic commands ###
