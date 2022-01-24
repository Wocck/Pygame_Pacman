import pytest
from io import StringIO
from files import (
    read_from_file_csv,
    write_to_file_csv,
    load,
    save,
    ScoreTable,
    FilePathNotFoundError,
    FilePathIsDirectoryError,
    FilePermissionError,
    InvalidScoreTableDataError,
    FileMalformedDataError
)


def test_load_not_exists():
    with pytest.raises(FilePathNotFoundError):
        load('files_for_tests/nonexist.txt')


def test_load_no_permission():
    with pytest.raises(FilePermissionError):
        load('files_for_tests/nopermission.txt')


def test_load_directory():
    with pytest.raises(FilePathIsDirectoryError):
        load('files_for_tests')


def test_save_directory():
    scores = []
    with pytest.raises(FilePathIsDirectoryError):
        save('files_for_tests', scores)


def test_save_not_exists():
    with pytest.raises(FilePathNotFoundError):
        load('files_for_tests/nonexist.txt')


def test_save_no_permission():
    with pytest.raises(FilePermissionError):
        load('files_for_tests/nopermission.txt')


def test_ScoreTable():
    scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = ScoreTable(scores)
    assert s.score_table[0] == 1
    assert s.score_table[8] == 9


def test_ScoreTable_invalid_length():
    scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with pytest.raises(InvalidScoreTableDataError):
        ScoreTable(scores)


def test_ScoreTable_invalid_data():
    scores = [1, 2, 3, '4', 5, 7, 8, 9, 10]
    with pytest.raises(InvalidScoreTableDataError):
        ScoreTable(scores)


def test_ScoreTable_add_score():
    scores = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    s = ScoreTable(scores)
    s.add_score(6)
    assert len(s.score_table) == 9
    assert s.score_table[0] == 10
    assert s.score_table[8] == 2
    assert s.score_table[3] == 7
    assert s.score_table[4] == 6
    assert s.score_table[5] == 5


def test_read_from_file_csv():
    data = 'score\n'\
            '9\n'\
            '8\n'\
            '7\n'\
            '6\n'\
            '5\n'\
            '4\n'\
            '3\n'\
            '2\n'\
            '1\n'\

    file_handle = StringIO(data)
    scores = read_from_file_csv(file_handle)
    s = ScoreTable(scores)
    assert s.score_table[0] == 9
    assert s.score_table[8] == 1


def test_read_from_file_csv_float_error():
    data = 'score\n'\
            '9.0\n'\
            '8\n'\
            '7\n'\
            '6\n'\
            '5\n'\
            '4\n'\
            '3\n'\
            '2\n'\
            '1\n'\

    file_handle = StringIO(data)
    with pytest.raises(FileMalformedDataError):
        read_from_file_csv(file_handle)


def test_read_from_file_csv_string_error():
    data = 'score\n'\
            '9\n'\
            'abba\n'\
            '7\n'\
            '6\n'\
            '5\n'\
            '4\n'\
            '3\n'\
            '2\n'\
            '1\n'\

    file_handle = StringIO(data)
    with pytest.raises(FileMalformedDataError):
        read_from_file_csv(file_handle)


def test_read_from_file_csv_none_error():
    data = 'score\n'\
            '9\n'\
            ' \n'\
            '7\n'\
            '6\n'\
            '5\n'\
            '4\n'\
            '3\n'\
            '2\n'\
            '1\n'\

    file_handle = StringIO(data)
    with pytest.raises(FileMalformedDataError):
        read_from_file_csv(file_handle)


def test_write_to_csv():
    scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = ScoreTable(scores)
    file_handle = StringIO()
    write_to_file_csv(file_handle, s.score_table)

    data = file_handle.getvalue()   # making string out of file_handle
    file_handle_2 = StringIO(data)  # making file like object from string
    scores = read_from_file_csv(file_handle_2)

    assert scores[0] == 1
    assert scores[8] == 9
