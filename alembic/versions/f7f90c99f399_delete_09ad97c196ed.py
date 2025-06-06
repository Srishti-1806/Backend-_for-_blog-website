"""delete 09ad97c196ed

Revision ID: f7f90c99f399
Revises: b8e8d8b36f51
Create Date: 2025-05-25 21:24:56.160399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7f90c99f399'
down_revision: Union[str, None] = 'b8e8d8b36f51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("posts")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
