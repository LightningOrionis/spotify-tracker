def test_crud_get(session, author_crud, author):
    session.add(author)
    session.commit()
    session.refresh(author)

    obj = author_crud.get(session, author.id)

    assert obj == author


def test_crud_get_all(session, author_crud, authors):
    for author in authors:
        session.add(author)
        session.commit()

    objects = author_crud.get_all(session)

    assert objects == authors


def test_crud_get_by_offset_and_limit(session, author_crud, authors):
    for author in authors:
        session.add(author)
        session.commit()

    objects = author_crud.get_by_offset_and_limit(session, 0, 5)

    assert objects == objects[0:5]


def test_crud_create(session, author_crud):
    create_author_dict = {"id": 5, "name": "author"}

    author_crud.create(session, create_author_dict)
    obj_in_db = author_crud.get(session, 5)

    assert obj_in_db.name == create_author_dict["name"]
    assert obj_in_db.id == create_author_dict["id"]


def test_crud_update(session, author_crud, author):
    update_author_dict = {"name": "author2"}

    session.add(author)
    session.commit()
    session.refresh(author)

    author_crud.update(session, author, update_author_dict)

    obj = author_crud.get(session, author.id)

    assert obj.name == "author2"


def test_crud_delete(session, author_crud, author):
    session.add(author)
    session.commit()
    session.refresh(author)

    author_crud.delete(session, author.id)

    objects = author_crud.get_all(session)

    assert len(objects) == 0
