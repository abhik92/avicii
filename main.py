from nadal import Slam
from datetime import datetime, timedelta

match_score = open("points.txt",'r')
score_board = open("scoresheet.txt",'w')

MAX_DAYS = 200
end = datetime.now()
start = end - timedelta(days=MAX_DAYS*7/5 + 50)

for points in match_score:
    game = points.split()
    tournament = game[0]
    final = game[1]
    debut = datetime.fromisoformat(final)
    sell = end - debut
    start_first = start
    if debut < start_first:
        start_first = debut
    set_summary = Slam(tournament, 'yahoo', start_first.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))
    set_one = set_summary.serve(MAX_DAYS)
    set_two = set_summary.serve(int(MAX_DAYS/2))
    set_three = set_summary.serve(int(MAX_DAYS/4))
    bounce = "The current price is {}".format(set_summary.lob(end.strftime("%Y-%m-%d"))) + '\n'
    rolling = "The 200, 100, 50 day rolling averages are {},{},{}".format(set_one, set_two, set_three) + '\n'
    history = "You bought this {} time units ago".format(sell) + '\n'

    print(bounce, rolling, history)
