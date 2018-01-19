import reports

question1 = reports.count_games('game_stat.txt')
question2 = reports.decide('game_stat.txt', '2009')
question3 = reports.get_latest('game_stat.txt')
question4 = reports.count_by_genre('game_stat.txt', 'RPG')
question5 = reports.get_line_number_by_title('game_stat.txt', 'Age of Empire')
question6 = reports.get_genres('game_stat.txt')
question7 = reports.sort_abc('game_stat.txt')

print (question1)
print (question2)
print (question3)
print (question4)
print (question5)
print (question6)
print (question7)
