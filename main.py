from random import randint

MAX_SCORE = 5
WIN_SCORE = 3
DRAW_SCORE = 1
TEAMS_NAMES = ["Спартак", "Зенит", "ЦСКА", "Ростов", "Краснодар" , "Терек", "Анжи", "Уфа" , "Рубин", "Локомотив"]
MAX_ID = len(TEAMS_NAMES)

# global structures
matches = dict()
teams = []


def teams_add(teams, name, id):
    teams.append({'name': name,
                  'score': 0,
                  'gols_in': 0,
                  'gols_out': 0,
                  'wins': 0,
                  'losses': 0,
                  'draws': 0,
                  'place': 0,
                  'id': id}
                 );
    return;


# Sample for  teams_add()
# teams_a = []
# teams_add(teams_a , "NAME!")
# teams_add(teams_a , "LOL")
# print(teams_a)

def create_teams(teams):
    for id in range(MAX_ID):
        teams_add(teams, TEAMS_NAMES[id], id)


def teams_sort(teams):
    def sort_key(param):
        return param["score"];

    teams.sort(key=sort_key);
    teams.reverse()
    pl = 1
    for v in teams:
        v["place"] = pl
        pl += 1


# Sample for teams_sort()
# teams_sort(teams)

def table_print(table, cols):
    Border = (9484, 9516, 9488, 9500, 9532, 9508, 9492, 9524, 9496, 9472, 9474)
    FIRST_ROWS = 0
    ROWS = 1
    END_ROWS = 2

    # Печать строки таблицы
    def print_rows(cols, style_rows=ROWS):
        cnt = 0;
        print('%c' % (Border[style_rows * 3]), end='')
        for k in cols:
            cnt += 1
            print('%s' % (chr(Border[9]) * k[1]), end='')
            if (cnt == len(cols)):
                print('%c\n' % (Border[style_rows * 3 + 2]), end='')
            else:
                print('%c' % (Border[style_rows * 3 + 1]), end='')

    print_rows(cols, FIRST_ROWS)
    # Печатать заголовок
    cntElem = 0
    print('%c' % (Border[10]), end='')
    for val in cols:
        cntElem += 1
        str = "{0:^%d}" % (val[1])
        print(str.format(val[2][:val[1]]), end='')
        if (cntElem == len(cols)):
            # last
            print('%c\n' % (Border[10]), end='')
        else:
            # not a last
            print('%c' % (Border[10]), end='')
    print_rows(cols)
    # Печатать строки
    cntRows = 0
    for elem in table:
        cntElem = 0
        print('%c' % (Border[10]), end='')
        for val in cols:
            cntElem += 1
            fstr = "{0:^%d}" % (val[1])
            print(fstr.format(elem[val[0]]), end='')
            if (cntElem == len(cols)):
                # last
                print('%c\n' % (Border[10]), end='')
            else:
                # not a last
                print('%c' % (Border[10]), end='')
        cntRows += 1
        if (cntRows == len(table)):
            print_rows(cols, END_ROWS)
        else:
            print_rows(cols)
    return;


def teams_print(teams):
    col = [("place", 4, "#"),
           ("name", 18, "Имя"),
           ("score", 8, "Очки"),
           ("gols_in", 8, "Забитые"),
           ("gols_out", 8, "Пропущ."),
           ("wins", 8, "Побед"),
           ("losses", 8, "Пораж."),
           ("draws", 8, "Ничьих")]
    table_print(teams, col)
    return


# Samle for teams_print()
# teams_print(teams)


# return -1 if not found
def teams_get_id(teams, name, speed_search=True):
    if (speed_search or hasattr(teams_get_id, '_dir')):
        # create static dir
        if (not hasattr(teams_get_id, '_dir')):
            teams_get_id._dir = {}
            for team in teams:
                teams_get_id._dir[team["name"].lower()] = team["id"]
        return teams_get_id._dir.get(name, -1)
    else:
        for team in teams:
            if (team["name"].lower() == name):
                return team["id"]
    return -1


# -----------------------------------------------------------------
# generating module

# change teams[id] when id wins
def write_winner(id):
    teams[id]["wins"] += 1
    teams[id]["score"] += WIN_SCORE


# change teams[id] when id lose
def write_loser(id):
    teams[id]["losses"] += 1


# change teams[id1] ans teams[id2] when draw
def write_draw(id1, id2):
    teams[id1]["draws"] += 1
    teams[id1]["score"] += DRAW_SCORE
    teams[id2]["draws"] += 1
    teams[id2]["score"] += DRAW_SCORE


# generate match and write information to teams and matches
def generate_match(id1, id2, teams, matches):
    gols1 = randint(0, MAX_SCORE)
    gols2 = randint(0, MAX_SCORE)
    matches[(id1, id2)] = (gols1, gols2)

    teams[id1]["gols_in"] += gols1
    teams[id1]["gols_out"] += gols2
    teams[id2]["gols_in"] += gols2
    teams[id2]["gols_out"] += gols1

    if gols1 > gols2:
        write_winner(id1)
        write_loser(id2)
    elif gols2 > gols1:
        write_winner(id2)
        write_loser(id1)
    elif gols1 == gols2:
        write_draw(id1, id2)
    return


# get match result by team names
def get_match():
    firstTeamId = -2
    secondTeamId = -3
    while check_teams(firstTeamId, secondTeamId) != 1:
        firstTeam, secondTeam = get_query()
        firstTeamId = teams_get_id(teams, firstTeam)
        secondTeamId = teams_get_id(teams, secondTeam)
    matchResult = get_match_result(firstTeamId, secondTeamId)
    print('Матч завершился со счетом ' + str(matchResult[0]) + ' : ' + str(matchResult[1]))
    return

def check_teams(id1, id2):
    if int(id1) == -1 or int(id2) == -1:
        print('Введите существующие команды')
        return -1
    elif id1 == id2:
        print('Команда не может играть сама с собой')
        return 0
    elif id1 == -2 and id2 == -3:
        return -2
    else:
        return 1


def get_query():
    while True:
        try:
            firstTeam, secondTeam = input('Введите названия команд через пробел\n').lower().split(' ')
            return firstTeam, secondTeam
        except ValueError as e:
            print('Ошибка ввода. Введите название 2 команд через пробел\n')
            pass

def get_match_result(firsteamId, secondTeamId):
    if firsteamId < secondTeamId:
        return matches[(firsteamId, secondTeamId)]
    else:
        matchesRev = matches[(secondTeamId, firsteamId)][::-1]
        return matchesRev

# -----------------------------------------------------------------


def main():
    create_teams(teams)
    for id1 in range(MAX_ID - 1):
        for id2 in range(id1 + 1, MAX_ID):
            generate_match(id1, id2, teams, matches)
    teams_sort(teams)
    teams_print(teams)
    get_match()

main()
