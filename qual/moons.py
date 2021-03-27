def find_min_cost(x, y, s):
    # x = cost for CJ
    # y = cost for JC
    # we want to minimize flips

    cost = 0
    prev = ''
    start = 0
    for i in range(0, len(s)):
        if s[i] != '?':
            start = i
            prev = s[i]
            break

    for i in range(start+1, len(s)):
        current = s[i]
        if current == '?':
            continue

        if prev == current:
            continue

        # not equal
        if prev == 'C':
            # we found a CJ
            cost += x
        else:
            cost += y

        prev = current

    return cost


if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        x, y, s = input().split(' ')
        cost = find_min_cost(int(x), int(y), s)
        print("Case #{}: {}".format(case_num, cost))
        case_num += 1