"""adds newsletter

Revision ID: c9ef0ac1cd28
Revises: 7f9b51534f93
Create Date: 2022-06-21 08:00:22.188529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9ef0ac1cd28'
down_revision = '7f9b51534f93'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "newsletter",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("email", sa.String, unique=True))


def downgrade():
    op.drop_table("newsletter")
