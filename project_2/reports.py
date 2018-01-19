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


def get_most_played(file_name):
    game_list = open_file(file_name)
    game_list.sort(key = lambda x: float(x[1]), reverse=True)
    title = game_list[0][0]
    return title


def sum_sold(file_name):
    game_list = open_file(file_name)
    copies = []
    for game in game_list:
        copies.append(game[1])
    copies_sold = sum(map(float, copies))
    return copies_sold


def get_selling_avg(file_name):
    game_list = open_file(file_name)
    copies = []
    for game in game_list:
        copies.append(game[1])
    copies_sold = sum(map(float, copies))
    copies_sold = copies_sold / float(len(copies))
    return copies_sold


def count_longest_title(file_name):
    game_list = open_file(file_name)
    titles = []
    for game in game_list:
        titles.append(game[0])
    titles.sort(key = lambda x: len(x), reverse=True)
    return len(titles[0])


def get_date_avg(file_name):
    game_list = open_file(file_name)
    date = []
    for game in game_list:
        date.append(game[2])
    date_avg = sum(map(int, date))
    date_avg = (date_avg / len(date))
    return round(date_avg)


def get_game(file_name, title):
    game_list = open_file(file_name)
    for game in game_list:
        if title == (game[0]):
            game_good = [game[0], float(game[1]), int(game[2]), game[3], game[4]]
    return game_good

def get_date_ordered(file_name):
    game_list = open_file(file_name)
    game_list.sort(key = lambda x: x[0])
    game_list.sort(key = lambda x: x[2], reverse=True)
    titles = []
    for game in game_list:
        titles.append(game[0])
    return titles