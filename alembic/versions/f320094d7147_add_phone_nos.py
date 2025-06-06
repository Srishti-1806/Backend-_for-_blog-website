"""add phone nos

Revision ID: f320094d7147
Revises: b542166f0200
Create Date: 2025-05-26 00:04:13.765117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f320094d7147'
down_revision: Union[str, None] = 'b542166f0200'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("Phone_no", sa.String, nullable= True))
    pass


def downgrade() -> None:
    op.drop_column("users", "Phone_no")
    pass
