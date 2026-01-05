"""create post table

Revision ID: 542b8f788bed
Revises: 
Create Date: 2026-01-05 16:20:13.308914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '542b8f788bed'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),)


def downgrade() -> None:
    op.drop_table('posts')
    pass
