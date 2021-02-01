from nadal import Slam
from datetime import datetime, timedelta
from hawkeye import VideoReplay

match_score = open("points.txt",'r')

OUTPUT = "scoresheet.txt"
score_board = open(OUTPUT,'w')

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
    bounce = "The current price of {} is {}".format(tournament, set_summary.lob(end.strftime("%Y-%m-%d"))) + '\n'
    rolling = "The 200, 100, 50 day rolling averages are {},{},{}".format(set_one, set_two, set_three) + '\n'
    history = "You bought this {} time units ago".format(sell) + '\n'

    score_board.write(bounce + rolling + history + '\n')

score_board.close()

video = VideoReplay("abhik.mondal1992@gmail.com", OUTPUT)
