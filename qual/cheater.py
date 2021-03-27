def find_cheater():
    max_correct = -1
    max_idx = -1
    for i in range(100):
        num_correct = len([c for c in input() if c=='1'])
        if num_correct > max_correct:
            max_correct = num_correct
            max_idx = i+1

    return max_idx


if __name__ == "__main__":
    num_cases = int(input())
    p = int(input())
    case_num = 1
    while case_num <= num_cases:
        ordering = find_cheater()
        print("Case #{}: {}".format(case_num, ordering))
        case_num += 1
