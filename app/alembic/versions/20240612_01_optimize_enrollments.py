"""
Revision ID: 20240612_01
Revises: 
Create Date: 2024-06-12

Optimize enrollments table: add composite indexes for query performance
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_index('idx_enrollments_course_status', 'enrollments', ['course_id', 'status'])
    op.create_index('idx_enrollments_student_id', 'enrollments', ['student_id'])
    # If you notice an old inefficient LEFT JOIN-based index, drop it here

def downgrade():
    op.drop_index('idx_enrollments_course_status', table_name='enrollments')
    op.drop_index('idx_enrollments_student_id', table_name='enrollments')
