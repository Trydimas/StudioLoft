"""initial22

Revision ID: 26addb6e6286
Revises: 998fdfd4d03b
Create Date: 2024-06-08 15:09:17.880143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26addb6e6286'
down_revision: Union[str, None] = '998fdfd4d03b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
