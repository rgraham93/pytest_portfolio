import pytest
import psycopg2
from common_utils import *

@pytest.fixture
def get_postgresql_db_conn(fig):
    """
    PyTest fixture that provides a PostgreSQL database connection.
    The connection is automatically closed after the test completes.
    """
    conn = psycopg2.connect(
        dbname=f"{fig['dbname']}",
        user=f"{fig['user']}",
        password=f"{fig['pass']}",
        host=f"{fig['host']}",
        port=f"{fig['port']}"
    )
    
    try:
        yield conn
    finally:
        conn.close()