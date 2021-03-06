"""inital migration

Revision ID: e270c833a1bc
Revises: None
Create Date: 2017-04-20 20:11:59.650312

"""

# revision identifiers, used by Alembic.
revision = 'e270c833a1bc'
down_revision = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_low_suffix', sa.Text(), nullable=True),
    sa.Column('address_low_frac', sa.Text(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_num', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.Text(), nullable=True),
    sa.Column('zip_4', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_error',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_name', sa.Text(), nullable=True),
    sa.Column('source_address', sa.Text(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('level', sa.Text(), nullable=True),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address_1', sa.Text(), nullable=True),
    sa.Column('relationship', sa.Text(), nullable=True),
    sa.Column('address_2', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_parcel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('parcel_source', sa.Text(), nullable=True),
    sa.Column('parcel_row_id', sa.Integer(), nullable=True),
    sa.Column('match_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('opa_account_num', sa.Text(), nullable=True),
    sa.Column('match_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_street',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('seg_side', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_low_suffix', sa.Text(), nullable=True),
    sa.Column('address_low_frac', sa.Text(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_num', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.Text(), nullable=True),
    sa.Column('zip_4', sa.Text(), nullable=True),
    sa.Column('usps_bldgfirm', sa.Text(), nullable=True),
    sa.Column('usps_type', sa.Text(), nullable=True),
    sa.Column('election_block_id', sa.Text(), nullable=True),
    sa.Column('election_precinct', sa.Text(), nullable=True),
    sa.Column('street_code', sa.Integer(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('seg_side', sa.Text(), nullable=True),
    sa.Column('pwd_parcel_id', sa.Text(), nullable=True),
    sa.Column('dor_parcel_id', sa.Text(), nullable=True),
    sa.Column('opa_account_num', sa.Text(), nullable=True),
    sa.Column('opa_owners', sa.Text(), nullable=True),
    sa.Column('opa_address', sa.Text(), nullable=True),
    sa.Column('info_residents', sa.Text(), nullable=True),
    sa.Column('info_companies', sa.Text(), nullable=True),
    sa.Column('pwd_account_nums', sa.Text(), nullable=True),
    sa.Column('li_address_key', sa.Text(), nullable=True),
    sa.Column('voters', sa.Text(), nullable=True),
    sa.Column('geocode_type', sa.Text(), nullable=True),
    sa.Column('geocode_x', sa.Float(), nullable=True),
    sa.Column('geocode_y', sa.Float(), nullable=True),
    sa.Column('geocode_street_x', sa.Float(), nullable=True),
    sa.Column('geocode_street_y', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('address_summary_sort_idx', 'address_summary', ['street_name', 'street_suffix', 'street_predir', 'street_postdir', 'address_low', 'address_high', 'unit_num'], unique=False, postgresql_using='btree')
    op.create_index(op.f('ix_address_summary_dor_parcel_id'), 'address_summary', ['dor_parcel_id'], unique=False)
    op.create_index(op.f('ix_address_summary_opa_account_num'), 'address_summary', ['opa_account_num'], unique=False)
    op.create_index(op.f('ix_address_summary_pwd_parcel_id'), 'address_summary', ['pwd_parcel_id'], unique=False)
    op.create_table('address_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('key', sa.Text(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('linked_address', sa.Text(), nullable=True),
    sa.Column('linked_path', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('address_zip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('usps_id', sa.Text(), nullable=True),
    sa.Column('match_type', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curb_id', sa.Integer(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dor_parcel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parcel_id', sa.Text(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_low_suffix', sa.Text(), nullable=True),
    sa.Column('address_low_frac', sa.Text(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_num', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('source_object_id', sa.Integer(), nullable=True),
    sa.Column('source_address', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dor_parcel_parcel_id'), 'dor_parcel', ['parcel_id'], unique=False)
    op.create_table('dor_parcel_error',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectid', sa.Integer(), nullable=True),
    sa.Column('mapreg', sa.Text(), nullable=True),
    sa.Column('stcod', sa.Integer(), nullable=True),
    sa.Column('house', sa.Integer(), nullable=True),
    sa.Column('suf', sa.Text(), nullable=True),
    sa.Column('stex', sa.Text(), nullable=True),
    sa.Column('stdir', sa.Text(), nullable=True),
    sa.Column('stnam', sa.Text(), nullable=True),
    sa.Column('stdes', sa.Text(), nullable=True),
    sa.Column('stdessuf', sa.Text(), nullable=True),
    sa.Column('unit', sa.Text(), nullable=True),
    sa.Column('level', sa.Text(), nullable=True),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dor_parcel_error_polygon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('objectid', sa.Integer(), nullable=True),
    sa.Column('mapreg', sa.Text(), nullable=True),
    sa.Column('stcod', sa.Integer(), nullable=True),
    sa.Column('house', sa.Integer(), nullable=True),
    sa.Column('suf', sa.Text(), nullable=True),
    sa.Column('stex', sa.Text(), nullable=True),
    sa.Column('stdir', sa.Text(), nullable=True),
    sa.Column('stnam', sa.Text(), nullable=True),
    sa.Column('stdes', sa.Text(), nullable=True),
    sa.Column('stdessuf', sa.Text(), nullable=True),
    sa.Column('unit', sa.Text(), nullable=True),
    sa.Column('shape', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=2272), nullable=True),
    sa.Column('reasons', sa.Text(), nullable=True),
    sa.Column('reason_count', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('geocode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('geocode_type', sa.Integer(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('multiple_seg_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('parent_address', sa.Text(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('parcel_source', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='LINESTRING', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('opa_property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_num', sa.Text(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_low_suffix', sa.Text(), nullable=True),
    sa.Column('address_low_frac', sa.Text(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_num', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('source_address', sa.Text(), nullable=True),
    sa.Column('tencode', sa.Text(), nullable=True),
    sa.Column('owners', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_opa_property_account_num'), 'opa_property', ['account_num'], unique=False)
    op.create_table('parcel_curb',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parcel_source', sa.Text(), nullable=True),
    sa.Column('parcel_row_id', sa.Text(), nullable=True),
    sa.Column('curb_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pwd_parcel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parcel_id', sa.Integer(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_low_suffix', sa.Text(), nullable=True),
    sa.Column('address_low_frac', sa.Text(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_num', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pwd_parcel_parcel_id'), 'pwd_parcel', ['parcel_id'], unique=False)
    op.create_table('service_area_diff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.Column('layer_id', sa.Text(), nullable=True),
    sa.Column('ais_value', sa.Text(), nullable=True),
    sa.Column('ulrs_value', sa.Text(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_area_layer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('layer_id', sa.Text(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_area_line_dual',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('layer_id', sa.Text(), nullable=True),
    sa.Column('source_object_id', sa.Integer(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('left_value', sa.Text(), nullable=True),
    sa.Column('right_value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_area_line_single',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('layer_id', sa.Text(), nullable=True),
    sa.Column('source_object_id', sa.Integer(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_area_polygon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('layer_id', sa.Text(), nullable=True),
    sa.Column('source_object_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('source_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source_name', sa.Text(), nullable=True),
    sa.Column('source_address', sa.Text(), nullable=True),
    sa.Column('street_address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('street_alias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('street_intersection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.Column('int_id', sa.Integer(), nullable=True),
    sa.Column('street_1_full', sa.Text(), nullable=True),
    sa.Column('street_1_name', sa.Text(), nullable=True),
    sa.Column('street_1_code', sa.Text(), nullable=True),
    sa.Column('street_1_predir', sa.Text(), nullable=True),
    sa.Column('street_1_postdir', sa.Text(), nullable=True),
    sa.Column('street_1_suffix', sa.Text(), nullable=True),
    sa.Column('street_2_full', sa.Text(), nullable=True),
    sa.Column('street_2_name', sa.Text(), nullable=True),
    sa.Column('street_2_code', sa.Text(), nullable=True),
    sa.Column('street_2_predir', sa.Text(), nullable=True),
    sa.Column('street_2_postdir', sa.Text(), nullable=True),
    sa.Column('street_2_suffix', sa.Text(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POINT', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_street_intersection_street_1_code'), 'street_intersection', ['street_1_code'], unique=False)
    op.create_index(op.f('ix_street_intersection_street_2_code'), 'street_intersection', ['street_2_code'], unique=False)
    op.create_table('street_segment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seg_id', sa.Integer(), nullable=True),
    sa.Column('street_code', sa.Integer(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('street_full', sa.Text(), nullable=True),
    sa.Column('left_from', sa.Integer(), nullable=True),
    sa.Column('left_to', sa.Integer(), nullable=True),
    sa.Column('right_from', sa.Integer(), nullable=True),
    sa.Column('right_to', sa.Integer(), nullable=True),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='LINESTRING', srid=2272), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('zip_range',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usps_id', sa.Text(), nullable=True),
    sa.Column('address_low', sa.Integer(), nullable=True),
    sa.Column('address_high', sa.Integer(), nullable=True),
    sa.Column('address_oeb', sa.Text(), nullable=True),
    sa.Column('street_predir', sa.Text(), nullable=True),
    sa.Column('street_name', sa.Text(), nullable=True),
    sa.Column('street_suffix', sa.Text(), nullable=True),
    sa.Column('street_postdir', sa.Text(), nullable=True),
    sa.Column('unit_type', sa.Text(), nullable=True),
    sa.Column('unit_low', sa.Text(), nullable=True),
    sa.Column('unit_high', sa.Text(), nullable=True),
    sa.Column('unit_oeb', sa.Text(), nullable=True),
    sa.Column('zip_code', sa.Text(), nullable=True),
    sa.Column('zip_4', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zip_range')
    op.drop_table('street_segment')
    op.drop_index(op.f('ix_street_intersection_street_2_code'), table_name='street_intersection')
    op.drop_index(op.f('ix_street_intersection_street_1_code'), table_name='street_intersection')
    op.drop_table('street_intersection')
    op.drop_table('street_alias')
    op.drop_table('source_address')
    op.drop_table('service_area_polygon')
    op.drop_table('service_area_line_single')
    op.drop_table('service_area_line_dual')
    op.drop_table('service_area_layer')
    op.drop_table('service_area_diff')
    op.drop_index(op.f('ix_pwd_parcel_parcel_id'), table_name='pwd_parcel')
    op.drop_table('pwd_parcel')
    op.drop_table('parcel_curb')
    op.drop_index(op.f('ix_opa_property_account_num'), table_name='opa_property')
    op.drop_table('opa_property')
    op.drop_table('multiple_seg_line')
    op.drop_table('geocode')
    op.drop_table('dor_parcel_error_polygon')
    op.drop_table('dor_parcel_error')
    op.drop_index(op.f('ix_dor_parcel_parcel_id'), table_name='dor_parcel')
    op.drop_table('dor_parcel')
    op.drop_table('curb')
    op.drop_table('address_zip')
    op.drop_table('address_tag')
    op.drop_index(op.f('ix_address_summary_pwd_parcel_id'), table_name='address_summary')
    op.drop_index(op.f('ix_address_summary_opa_account_num'), table_name='address_summary')
    op.drop_index(op.f('ix_address_summary_dor_parcel_id'), table_name='address_summary')
    op.drop_index('address_summary_sort_idx', table_name='address_summary')
    op.drop_table('address_summary')
    op.drop_table('address_street')
    op.drop_table('address_property')
    op.drop_table('address_parcel')
    op.drop_table('address_link')
    op.drop_table('address_error')
    op.drop_table('address')
    ### end Alembic commands ###
