def test_get_by_name(session, author_crud, author):
    session.add(author)
    session.commit()
    session.refresh(author)

    obj = author_crud.get_by_name(session, author.name)

    assert obj == author
