"""create table users

Revision ID: 09ad97c196ed
Revises: 
Create Date: 2025-05-25 20:46:23.747077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09ad97c196ed'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Users", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
    sa.Column("title", sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_table("Users")
    pass
