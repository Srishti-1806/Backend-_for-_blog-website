"""create table posts

Revision ID: 70510b7ce5f2
Revises: 09ad97c196ed
Create Date: 2025-05-25 21:09:11.116413

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70510b7ce5f2'
down_revision: Union[str, None] = '09ad97c196ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id", sa.Integer(), nullable= False, primary_key=True ), sa.Column("posts", sa.String(),
                   nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
