"""add column context to table posts

Revision ID: 8ddaf31a86c7
Revises: f7f90c99f399
Create Date: 2025-05-25 21:26:52.616003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ddaf31a86c7'
down_revision: Union[str, None] = 'f7f90c99f399'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("Posts",sa.Column("content", sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column("Posts","content")
    pass
