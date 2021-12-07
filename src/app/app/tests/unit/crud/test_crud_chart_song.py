from app.crud.charted_song import ChartedSongCRUD
from app.models.charted_song import ChartedSong


def test_get_places_on_dates(session, charts, charted_songs, song, user):
    charts = sorted(charts, key=lambda x: x.date, reverse=False)

    for chart, charted_song in zip(charts, charted_songs):
        chart.user = user
        charted_song.chart = chart
        charted_song.song = song

    start_date = charts[3].date
    end_date = charts[7].date

    session.add(user)
    session.commit()

    for chart in charts:
        session.add(chart)
        session.commit()

    session.add(song)
    session.commit()

    for ch_song in charted_songs:
        session.add(ch_song)
        session.commit()

    crud = ChartedSongCRUD(ChartedSong)
    result = crud.get_places_on_dates(session, start_date, end_date, user.id, song.id)

    assert result == {charted_songs[i].chart: charted_songs[i].place for i in range(3, 8)}
