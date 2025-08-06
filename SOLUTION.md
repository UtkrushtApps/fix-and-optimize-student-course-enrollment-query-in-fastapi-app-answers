# Solution Steps

1. Review the API's current approach for fetching students by course and, optionally, by status. Identify that the current LEFT JOIN strategy is not necessary for enrolled students in a course and can be replaced with a more efficient JOIN.

2. Optimize the SQLAlchemy models (models.py): Ensure that there are dedicated indexes and composite indexes on enrollments for (course_id, status), (student_id), and uniqueness constraint (student_id, course_id).

3. Modify the database migration files (alembic): Create a migration that adds these indexes to the enrollments table. Write an Alembic revision to add and drop these indexes, as shown.

4. Update database.py to ensure DB connection and create tables are set as per production use.

5. Refactor the endpoint in main.py: Use an INNER JOIN from Student to Enrollment, filtering by course_id and optionally status. This limits rows processed, leverages the new indexes, and avoids expensive LEFT JOINs.

6. Retain proper ORM relationships for convenient querying and cascade loading as needed. Confirm pydantic (schemas.py) responses are appropriate.

7. Test fetching students by course and status to verify correctness and that results are near-instant even with large datasets (thousands of rows).

8. Validate that the query plans (e.g., via EXPLAIN in psql) are using the new indexes.

