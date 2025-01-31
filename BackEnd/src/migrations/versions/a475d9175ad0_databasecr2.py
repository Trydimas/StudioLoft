"""DatabaseCr2

Revision ID: a475d9175ad0
Revises: 0a3d6e9a701e
Create Date: 2024-06-05 23:03:43.341443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a475d9175ad0'
down_revision: Union[str, None] = '0a3d6e9a701e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name_project', sa.String(), nullable=False),
    sa.Column('Size', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Images', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(), nullable=False),
    sa.Column('Last_name', sa.String(), nullable=False),
    sa.Column('Father_name', sa.String(), nullable=False),
    sa.Column('Description', sa.String(), nullable=False),
    sa.Column('Phrase', sa.String(), nullable=False),
    sa.Column('Image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('staff')
    op.drop_table('projects')
    # ### end Alembic commands ###
