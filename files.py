import csv


class FilePathNotFoundError(FileNotFoundError):
    pass


class FilePermissionError(PermissionError):
    pass


class FilePathIsDirectoryError(IsADirectoryError):
    pass


class FileMalformedDataError(Exception):
    pass


class InvalidScoreTableDataError(Exception):
    pass


class ScoreTable:
    '''
    Class ScoreTable. Contains attributes:
    :param score_table: list of highscores
    '''
    def __init__(self, score_table) -> None:
        if len(score_table) > 9:
            raise InvalidScoreTableDataError('Max 9 highscores!')
        for score in score_table:
            if not isinstance(score, int):
                raise InvalidScoreTableDataError('Position is not int type')
        self.score_table = score_table

    def add_score(self, score):
        '''
        add score than sort and delete last element if length of score list
        is grater than 9
        '''
        if score not in self.score_table:
            self.score_table.append(score)
            self.score_table.sort(reverse=True)
            while len(self.score_table) > 9:
                self.score_table.pop()

    def __str__(self) -> str:
        '''
        just __str__ method creating string fomr list
        '''
        list = ''
        for index, score in enumerate(self.score_table):
            list += f'{index+1}.    {score:5}\n'
        return list


def load(path):
    '''
    Load high scores from file
    '''
    try:
        with open(path, 'r') as file_handle:
            return read_from_file_csv(file_handle)
    except FileNotFoundError:
        raise FilePathNotFoundError('Path not found')
    except PermissionError:
        raise FilePermissionError('Cant open file')
    except IsADirectoryError:
        raise FilePathIsDirectoryError('Path is a directory')


def save(path, scores):
    '''
    Save high scores to file
    '''
    try:
        with open(path, 'w') as file_handle:
            return write_to_file_csv(file_handle, scores)
    except FileNotFoundError:
        raise FilePathNotFoundError('Path not found')
    except PermissionError:
        raise FilePermissionError('Cant open file')
    except IsADirectoryError:
        raise FilePathIsDirectoryError('Path is a directory')


def read_from_file_csv(file_handle):
    '''
    Read high scores to file
    '''
    scores = []
    csv_reader = csv.DictReader(file_handle)
    for row in csv_reader:
        if None in row.values():
            raise FileMalformedDataError('Missing column in row')
        score = row['score']
        if not score.isdigit():
            raise FileMalformedDataError('Score must be Int')
        scores.append(int(score))
    return scores


def write_to_file_csv(file_handle, scores):
    '''
    Write high scores to file
    '''
    writer = csv.DictWriter(
        file_handle,
        ['score']
    )
    writer.writeheader()
    for score in scores:
        writer.writerow({
            'score': score,
        })
