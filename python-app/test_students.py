import pytest
import psycopg2

from students import add_student, get_student, average_grade


@pytest.fixture
def conn():
    connection = psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )

    with connection.cursor() as cur:
        cur.execute("TRUNCATE TABLE students RESTART IDENTITY")
    connection.commit()

    yield connection

    connection.close()


def test_add_and_get_student(conn):
    student = add_student(conn, "Amel", 15)


    assert student is not None
    assert student[1] == "Amel"
    assert student[2] == 15.0


def test_get_student(conn):
    not_student = get_student(conn, "zzz")

    assert not_student is None



def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)

    assert average_grade(conn) == 12.0
