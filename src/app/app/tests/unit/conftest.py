import datetime

import pytest
from factory.fuzzy import FuzzyDate, FuzzyInteger, FuzzyText

from app.crud.author import AuthorCRUD
from app.crud.chart import ChartCRUD
from app.models.author import Author
from app.models.chart import Chart
from app.models.charted_song import ChartedSong
from app.models.song import Song
from app.models.user import User
from app.tests.testing_utils.db import testing_db


@pytest.fixture()
def session():
    with testing_db.TestingDatabase() as session_obj:
        session, engine = session_obj
        yield session
        session.close()
        engine.dispose()


@pytest.fixture()
def author_crud():
    crud = AuthorCRUD(Author)
    return crud


@pytest.fixture()
def chart_crud():
    crud = ChartCRUD(Chart)
    return crud


def author_factory():
    author = Author(id=FuzzyInteger(0, 10000000).fuzz(), name=FuzzyText().fuzz())
    return author


@pytest.fixture()
def author():
    return author_factory()


@pytest.fixture()
def authors():
    return [author_factory() for _ in range(10)]


def user_factory():
    user = User(id=FuzzyInteger(0, 100000).fuzz(), hashed_password=FuzzyText().fuzz(), email=FuzzyText().fuzz())
    return user


@pytest.fixture()
def user():
    return user_factory()


@pytest.fixture()
def users():
    return [user_factory() for _ in range(10)]


def chart_factory():
    chart = Chart(date=FuzzyDate(datetime.date(2020, 1, 1)).fuzz(), name=FuzzyText().fuzz())
    return chart


@pytest.fixture()
def chart():
    return chart_factory()


@pytest.fixture()
def charts():
    return [chart_factory() for _ in range(10)]


def song_factory():
    song = Song(id=FuzzyInteger(1, 10000000).fuzz(), name=FuzzyText().fuzz())
    return song


@pytest.fixture()
def song():
    return song_factory()


@pytest.fixture()
def songs():
    return [song_factory() for _ in range(10)]


def charted_song_factory():
    return ChartedSong(place=FuzzyInteger(1, 50).fuzz())


@pytest.fixture()
def charted_songs():
    return [charted_song_factory() for _ in range(10)]
