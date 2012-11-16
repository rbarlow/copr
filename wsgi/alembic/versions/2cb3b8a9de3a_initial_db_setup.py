"""Initial db setup

Revision ID: 2cb3b8a9de3a
Revises: None
Create Date: 2012-11-16 11:38:30.605131

"""

# revision identifiers, used by Alembic.
revision = '2cb3b8a9de3a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('openid_name', sa.String(length=100), nullable=False),
    sa.Column('proven', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('copr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('chroots', sa.Text(), nullable=False),
    sa.Column('repos', sa.Text(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('build',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pkgs', sa.Text(), nullable=True),
    sa.Column('canceled', sa.Boolean(), nullable=True),
    sa.Column('chroots', sa.Text(), nullable=False),
    sa.Column('repos', sa.Text(), nullable=True),
    sa.Column('submitted_on', sa.Integer(), nullable=False),
    sa.Column('started_on', sa.Integer(), nullable=True),
    sa.Column('ended_on', sa.Integer(), nullable=True),
    sa.Column('results', sa.Text(), nullable=True),
    sa.Column('memory_reqs', sa.Integer(), nullable=True),
    sa.Column('timeout', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('copr_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['copr_id'], ['copr.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('copr_permission',
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('copr_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['copr_id'], ['copr.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'copr_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('copr_permission')
    op.drop_table('build')
    op.drop_table('copr')
    op.drop_table('user')
    ### end Alembic commands ###
