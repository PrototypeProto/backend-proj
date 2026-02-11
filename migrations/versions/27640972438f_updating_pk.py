"""updating pk

Revision ID: 27640972438f
Revises: 7c30337fa1ea
Create Date: 2026-02-11 00:37:03.017162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '27640972438f'
down_revision: Union[str, Sequence[str], None] = '7c30337fa1ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_constraint(
        "CoxwainEvaluation_pkey",
        "CoxwainEvaluation",
        type_="primary"
    )

    op.create_primary_key(
        "CoxwainEvaluation_pkey",
        "CoxwainEvaluation",
        ["evaluation_id"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "CoxwainEvaluation_pkey",
        "CoxwainEvaluation",
        type_="primary"
    )

    op.create_primary_key(
        "CoxwainEvaluation_pkey",
        "CoxwainEvaluation",
        ["cox_id"]
    )