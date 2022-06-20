"""Create users table

Revision ID: 3f46b73d6b30
Revises: 
Create Date: 2022-06-20 11:11:34.503126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f46b73d6b30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "user",
            sa.Column("id", sa.Integer, primary_key=True),
            sa.Column("username", sa.String),
            sa.Column("password", sa.String))


def downgrade():
    op.drop_table("user")
