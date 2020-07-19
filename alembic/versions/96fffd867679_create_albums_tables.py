"""create albums table

Revision ID: 96fffd867679
Revises: 
Create Date: 2020-07-19 23:06:12.448630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96fffd867679'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ALBUMS',
        sa.Column('ID', sa.Integer(), autoincrement=True, primary_key=True, unique=True, nullable=False),
        sa.Column('NAME', sa.String(100), nullable=False),
        sa.Column('AUTHOR', sa.String(50), nullable=False)
    )

    op.create_table(
        'PAGES',
        sa.Column('ID', sa.Integer(), autoincrement=True, primary_key=True, unique=True, nullable=False),
        sa.Column('ALBUM_ID', sa.Integer(), nullable=False),
        sa.Column('PAGE', sa.Integer(), nullable=False),
        sa.Column('TEXT', sa.String(1000)),
        sa.Column('IMAGE', sa.String(1000))
    )


def downgrade():
    op.drop_table('ALBUMS')
    op.drop_table('PAGES')
