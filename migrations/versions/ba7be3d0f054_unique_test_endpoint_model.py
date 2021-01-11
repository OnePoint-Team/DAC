"""unique test endpoint model

Revision ID: ba7be3d0f054
Revises: f4a0bfaf5fc7
Create Date: 2020-10-16 18:07:44.851603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba7be3d0f054'
down_revision = 'f4a0bfaf5fc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uix_endpoint_service_id_prefix', 'endpoint', ['service_id', 'prefix'])
    op.drop_index('ix_groups_name', table_name='groups')
    op.create_index(op.f('ix_groups_name'), 'groups', ['name'], unique=True)
    op.drop_index('ix_method_name', table_name='method')
    op.create_index(op.f('ix_method_name'), 'method', ['name'], unique=True)
    op.create_unique_constraint(None, 'user_groups', ['user_id'])
    op.drop_index('ix_users_identity', table_name='users')
    op.create_index(op.f('ix_users_identity'), 'users', ['identity'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_identity'), table_name='users')
    op.create_index('ix_users_identity', 'users', ['identity'], unique=False)
    op.drop_constraint(None, 'user_groups', type_='unique')
    op.drop_index(op.f('ix_method_name'), table_name='method')
    op.create_index('ix_method_name', 'method', ['name'], unique=False)
    op.drop_index(op.f('ix_groups_name'), table_name='groups')
    op.create_index('ix_groups_name', 'groups', ['name'], unique=False)
    op.drop_constraint('uix_endpoint_service_id_prefix', 'endpoint', type_='unique')
    # ### end Alembic commands ###