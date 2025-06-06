"""add last few columns to posts table

Revision ID: c64fccdae412
Revises: 7920fb0486ce
Create Date: 2025-05-25 23:23:58.266963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c64fccdae412'
down_revision: Union[str, None] = '7920fb0486ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("Posts", sa.Column(
        "published", sa.Boolean(), nullable = False, server_default="TRUE"),)
    op.add_column("Posts", sa.Column(
        "created_at", sa.TIMESTAMP(timezone=True), nullable= False, server_default=sa.text("NOW()")))
    pass


def downgrade() -> None:
    op.drop_column("Posts", "published")
    op.drop_column("Posts", "created_at")
    pass
