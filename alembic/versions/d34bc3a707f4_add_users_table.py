"""add users table

Revision ID: d34bc3a707f4
Revises: 8ddaf31a86c7
Create Date: 2025-05-25 22:57:46.442195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd34bc3a707f4'
down_revision: Union[str, None] = '8ddaf31a86c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable= False ),
                    sa.Column("email", sa.String(), nullable= False ),
                    sa.Column("password", sa.String(), nullable= False ),
                    sa.Column("created_at", sa.TIMESTAMP(timezone = True), nullable= False,
                    server_default = sa.text("now()")),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
