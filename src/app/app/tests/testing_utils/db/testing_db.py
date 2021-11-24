from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base

# CREATE_DB_URL = os.getenv("CREATE_DB_URL")
# TEST_DB_URL = os.getenv("TEST_DB_URL")

CREATE_DB_URL = "postgresql://igor:1234@localhost:5432/postgres"
TEST_DB_URL = "postgresql://igor:1234@localhost:5432/test_st_db"


class TestingDatabase:
    def __enter__(self):
        self.create_database()
        self.init_database()
        return self.get_test_session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.drop_database()

    def create_database(self):
        engine = create_engine(CREATE_DB_URL)
        conn = engine.connect()

        conn.execution_options(isolation_level="AUTOCOMMIT")
        conn.execute("CREATE DATABASE test_st_db")

        conn.close()
        engine.dispose()

    def drop_database(self):
        engine = create_engine(CREATE_DB_URL)
        conn = engine.connect()

        conn.execution_options(isolation_level="AUTOCOMMIT")
        conn.execute("DROP DATABASE test_st_db")

        conn.close()
        engine.dispose()

    def init_database(self):
        engine = create_engine(TEST_DB_URL)
        Base.metadata.create_all(engine, checkfirst=True)

        engine.dispose()

    def get_test_session(self):
        engine = create_engine(TEST_DB_URL)
        session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

        return session(), engine
