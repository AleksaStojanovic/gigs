"""adding musician applications

Revision ID: 921bca1dad13
Revises: 1e20813af5fe
Create Date: 2024-01-04 10:45:41.717505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '921bca1dad13'
down_revision = '1e20813af5fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('gig_id', sa.Integer(), nullable=True),
    sa.Column('musician_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gig_id'], ['gigs.id'], ),
    sa.ForeignKeyConstraint(['musician_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applications')
    # ### end Alembic commands ###