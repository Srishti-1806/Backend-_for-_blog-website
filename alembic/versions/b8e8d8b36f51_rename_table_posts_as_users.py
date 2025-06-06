"""rename table posts as users

Revision ID: b8e8d8b36f51
Revises: 70510b7ce5f2
Create Date: 2025-05-25 21:22:45.994279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e8d8b36f51'
down_revision: Union[str, None] = '70510b7ce5f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Users", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_table("Users")
    pass

