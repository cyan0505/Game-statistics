def count_games(file_name):
    with open (file_name, 'rb') as f:
        games = f.readlines()
    return len(games)


def decide(file_name, year):
    with open (file_name, 'rb') as f:
        games_list = str(f.readlines())
    return str(year) in games_list


def get_latest(file_name):
    games = open(file_name, 'r')
    games_list = games.readlines()
    games_list.sort(key = lambda x: int(x.split('\t')[2]), reverse = True)
    latest = games_list[0].split('\t')[0]
    games.close()
    return latest


def count_by_genre(file_name, genre):
    genre = str(genre)
    games = open(file_name, 'r')
    count = 0
    for game in games:
        if genre in game:
            count += 1
    games.close()
    return count


def get_line_number_by_title(file_name, title):
    games = open(file_name, 'r')
    games_list = games.readlines()
    for i in range(len(games_list)):
        if str(title) in games_list[i]:
            games.close()
            return i+1
    raise ValueError


def get_genres(file_name):
    genres_list = []
    games = open(file_name, 'r')
    games_list = games.readlines()
    for line in games_list:
        genre = line.split('\t')[3]
        if genre not in genres_list:
            genres_list.append(genre)
    genres = sorted(genres_list, key=str.lower)
    games.close()
    return genres


def open_file(file_name):
    '''opens file with sicing'''
    with open(file_name, 'r') as f:
        stats = f.readlines()
        game_list = []
        for i in range(len(stats)):
            stats[i] = stats[i][:-1] # remove ‘\n’
            game_list.append(stats[i])
        f.close()
        for i in range(len(game_list)):
            game_list[i] = game_list[i].split('\t')
    return game_list


def sort_abc(file_name):
    game_list = open_file(file_name)
    changed = True
    titles = []
    while changed:
        changed = False
        for i in range(len(game_list) - 1):
            if game_list[i] > game_list[i+1]:
                game_list[i], game_list[i+1] = game_list[i+1], game_list[i]
                changed = True
    for j in range (len(game_list)):
        titles.append(game_list[j][0])
    return titles