import psycopg2


def add_student(conn, name, grade):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO students (name, grade)
            VALUES (%s, %s)
            RETURNING id, name, grade
            """,
            (name, grade)
        )
        student = cur.fetchone()

    conn.commit()
    return (student[0], student[1], float(student[2]))


def get_student(conn, name):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, grade FROM students WHERE name = %s",
            (name,)
        )
        student = cur.fetchone()

    if student is None:
        return None

    return (student[0], student[1], float(student[2]))


def average_grade(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        result = cur.fetchone()[0]

    return float(result) if result is not None else 0.0