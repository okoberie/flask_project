"""adds html render to article table

Revision ID: 7f9b51534f93
Revises: 3f46b73d6b30
Create Date: 2022-06-21 06:54:34.550755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f9b51534f93'
down_revision = '3f46b73d6b30'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("article",
                sa.Column("html_render", sa.String, server_default=""))


def downgrade():
    op.drop_column("article", "html_render")
