"""add foreign key to post table 

Revision ID: 589ad78bc100
Revises: 446243522e31
Create Date: 2026-01-05 16:41:56.134484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '589ad78bc100'
down_revision: Union[str, Sequence[str], None] = '446243522e31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
