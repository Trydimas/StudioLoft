"""initial

Revision ID: 0925bb65cfec
Revises: 32f0c1f4af75
Create Date: 2024-06-08 15:03:36.777573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0925bb65cfec'
down_revision: Union[str, None] = '32f0c1f4af75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
