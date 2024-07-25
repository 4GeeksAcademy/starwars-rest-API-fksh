"""empty message

Revision ID: 9fc9be1966a7
Revises: 2b3ec8518479
Create Date: 2024-07-22 12:07:06.931653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fc9be1966a7'
down_revision = '2b3ec8518479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('characters_name', sa.String(length=120), nullable=False),
    sa.Column('hair_colour', sa.String(length=120), nullable=False),
    sa.Column('skin_colour', sa.String(length=120), nullable=False),
    sa.Column('eye_colour', sa.String(length=120), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planets_name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('terrain', sa.String(length=120), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('planet')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.create_table('planet',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('population', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='planet_pkey'),
    sa.UniqueConstraint('name', name='planet_name_key')
    )
    op.drop_table('users')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
