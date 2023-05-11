"""initial

Revision ID: b6d2d15e9b6d
Revises: 239ac7daedc7
Create Date: 2023-05-10 16:39:31.846537

"""
import alembic
from alembic import op
import sqlalchemy as sa
from alembic.operations import BatchOperations

# revision identifiers, used by Alembic.
revision = 'b6d2d15e9b6d'
down_revision = '239ac7daedc7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    # op.drop_constraint('url', table_name='url_services', type_='unique')

    op.drop_table('url_services')

    op.create_table('url_services',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('id_service', sa.INTEGER(), nullable=True),
                    sa.Column('url', sa.TEXT(), nullable=False),
                    sa.ForeignKeyConstraint(['id_service'], ['services.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_services')

    op.create_table('url_services',
                    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
                    sa.Column('id_service', sa.INTEGER(), nullable=True),
                    sa.Column('url', sa.TEXT(), nullable=False),
                    sa.ForeignKeyConstraint(['id_service'], ['services.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('url')
                    )
    # ### end Alembic commands ###
