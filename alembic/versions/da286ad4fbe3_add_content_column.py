"""add content column

Revision ID: da286ad4fbe3
Revises: 542b8f788bed
Create Date: 2026-01-05 16:31:34.955196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da286ad4fbe3'
down_revision: Union[str, Sequence[str], None] = '542b8f788bed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
