"""add_is_super_user_flag

Revision ID: 0942cfb35142
Revises: 7cca45280928
Create Date: 2024-04-22 11:25:26.281028

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0942cfb35142"
down_revision: Union[str, None] = "7cca45280928"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("is_super_user", sa.Boolean(), server_default=sa.text("false"), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_super_user")
    # ### end Alembic commands ###
