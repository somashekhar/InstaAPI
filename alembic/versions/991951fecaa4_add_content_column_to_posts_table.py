"""add content column to posts table

Revision ID: 991951fecaa4
Revises: d16fd2cf3112
Create Date: 2024-10-23 14:56:00.287673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '991951fecaa4'
down_revision: Union[str, None] = 'd16fd2cf3112'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
