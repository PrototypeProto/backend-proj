"""column name change

Revision ID: 9a6b0827556b
Revises: ab2d8af67f1f
Create Date: 2026-02-10 22:00:17.614548

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '9a6b0827556b'
down_revision: Union[str, Sequence[str], None] = 'ab2d8af67f1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass