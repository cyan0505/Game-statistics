import reports

question1 = reports.get_most_played('game_stat.txt')
question2 = reports.sum_sold('game_stat.txt')
question3 = reports.get_selling_avg('game_stat.txt')
question4 = reports.count_longest_title('game_stat.txt')
question5 = reports.get_date_avg('game_stat.txt')
question6 = reports.get_game('game_stat.txt', 'Minecraft')
question7 = reports.get_date_ordered('game_stat.txt')

with open("answers.txt", "w") as text_file:
    print (question1, file=text_file)
    print (question2, file=text_file)
    print (question3, file=text_file)
    print (question4, file=text_file)
    print (question5, file=text_file)
    print (question6, file=text_file)
    print (question7, file=text_file)
