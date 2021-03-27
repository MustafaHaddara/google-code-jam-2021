import math

def find_cheater():
    records_by_player = [] # index = player id
    num_players_solved = [0 for _ in range(10_000)] # index = question id
    for i in range(100):
        record = input()
        records_by_player.append(record)
        for i in range(len(record)):
            if record[i] == '1':
                num_players_solved[i] += 1

    max_outliers = -1
    max_idx = -1
    for i, record in enumerate(records_by_player):
        outliers = 0
        # solved is a rough estimate of their "skill"
        solved = len([item for item in record if item == '1'])
        s = 6 * (solved/10_000) - 3

        for q_idx, success in enumerate(record):
            # diff is a rough estimate of the difficulty of the question
            diff = num_players_solved[q_idx] / 100
            q = 6 * (1-diff) - 3

            prob_q = sigmoid(s-q)

            # if they had a high probability of solving, but still failed, track that
            # by our estimate of the smarts, cheater will appear to be a lot smarter than they actually are
            # meaning they'll fail more questions than they actually should
            if prob_q > 0.9 and success == '0':
                outliers += 1

        if outliers > max_outliers:
            max_outliers = outliers
            max_idx = i+1

    return max_idx

def sigmoid(x):
    denom = 1 + math.exp(-1 * x)
    return 1 / denom

if __name__ == "__main__":
    num_cases = int(input())
    p = int(input())
    case_num = 1
    while case_num <= num_cases:
        ordering = find_cheater()
        print("Case #{}: {}".format(case_num, ordering))
        case_num += 1
