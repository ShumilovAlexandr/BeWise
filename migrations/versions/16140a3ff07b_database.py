"""database

Revision ID: 16140a3ff07b
Revises: 
Create Date: 2023-10-16 01:29:19.566462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16140a3ff07b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
                    sa.Column('question_id', sa.Integer(), nullable=False),
                    sa.Column('question_text', sa.Text(), nullable=False),
                    sa.Column('answer_text', sa.Text(), nullable=False),
                    sa.Column('create_date_time', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('question_id'),
                    sa.UniqueConstraint('answer_text'),
                    sa.UniqueConstraint('question_text')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz')
    # ### end Alembic commands ###
