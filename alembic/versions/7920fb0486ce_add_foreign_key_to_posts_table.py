"""add foreign-key to posts table

Revision ID: 7920fb0486ce
Revises: d34bc3a707f4
Create Date: 2025-05-25 23:10:20.092940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7920fb0486ce'
down_revision: Union[str, None] = 'd34bc3a707f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("Posts", sa.Column("owner_id", sa.Integer(), nullable = False))
    op.create_foreign_key("post_users_fk", source_table= "Posts", 
    referent_table="users",local_cols=["owner_id"],
    remote_cols = ["id"], ondelete = "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name= "Posts")
    op.drop_column("Posts", "owner_id")
    pass
