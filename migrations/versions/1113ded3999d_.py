"""empty message

Revision ID: 1113ded3999d
Revises: 208514278827
Create Date: 2020-01-22 20:30:26.162264

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1113ded3999d'
down_revision = '208514278827'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resource__centers', 'zip')
    op.drop_column('users', 'zip')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('zip', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('resource__centers', sa.Column('zip', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###