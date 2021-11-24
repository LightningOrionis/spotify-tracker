def test_get_charts_by_user_in_day(session, chart_crud, chart, user):
    session.add(user)
    session.commit()

    chart.user_id = user.id

    session.add(chart)
    session.commit()

    objects = chart_crud.get_user_charts_in_day(session, chart.date, chart.user_id)

    assert len(objects) == 1
    assert objects[0] == chart
