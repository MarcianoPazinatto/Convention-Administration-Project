"""empty message

Revision ID: ade1644bbff7
Revises: 
Create Date: 2021-02-24 02:02:07.911461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ade1644bbff7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coffee_room',
    sa.Column('id', sa.String(length=36), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('convention',
    sa.Column('id', sa.String(length=36), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
    sa.Column('id', sa.String(length=36), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=36), nullable=False),
    sa.Column('last_name', sa.String(length=36), nullable=False),
    sa.Column('conventions_id', sa.String(length=36), nullable=False),
    sa.Column('coffe_room_id', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['coffe_room_id'], ['coffee_room.id'], ),
    sa.ForeignKeyConstraint(['conventions_id'], ['convention.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    op.drop_table('convention')
    op.drop_table('coffee_room')
    # ### end Alembic commands ###
