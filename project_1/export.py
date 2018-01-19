import reports

question1 = reports.count_games('game_stat.txt')
question2 = reports.decide('game_stat.txt', '2009')
question3 = reports.get_latest('game_stat.txt')
question4 = reports.count_by_genre('game_stat.txt', 'RPG')
question5 = reports.get_line_number_by_title('game_stat.txt', 'Age of Empire')
question6 = reports.get_genres('game_stat.txt')
question7 = reports.sort_abc('game_stat.txt')

with open("answers.txt", "w") as text_file:
    print (question1, file=text_file)
    print (question2, file=text_file)
    print (question3, file=text_file)
    print (question4, file=text_file)
    print (question5, file=text_file)
    print (question6, file=text_file)
    print (question7, file=text_file)
