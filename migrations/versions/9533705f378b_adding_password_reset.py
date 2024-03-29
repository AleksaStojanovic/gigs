"""adding password reset

Revision ID: 9533705f378b
Revises: 778294f5810e
Create Date: 2024-01-04 12:31:17.800807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9533705f378b'
down_revision = '778294f5810e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('reset_hash', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('reset_sent_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'reset_sent_at')
    op.drop_column('users', 'reset_hash')
    # ### end Alembic commands ###
