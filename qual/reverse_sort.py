def reverse_sort(s):
    cost = 0
    for i in range(len(s)-1):
        min_pos_ahead = find_pos_min(i, s)
        cost += min_pos_ahead - i + 1
        reverse_chunk(s, i, min_pos_ahead)

    return cost


def reverse_chunk(s, start, end):
    chunk = s[start:end+1]
    chunk.reverse()
    chunk_idx = 0
    i = start
    while i<=end:
        s[i] = chunk[chunk_idx]
        i += 1
        chunk_idx += 1

def find_pos_min(starting, s):
    m = -1
    pos = -1
    for i in range(starting, len(s)):
        if m == -1 or s[i] < m:
            m = s[i]
            pos = i
    return pos


if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        list_size = input()
        input_list = [int(i) for i in input().split(" ")]
        cost = reverse_sort(input_list)
        print("Case #{}: {}".format(case_num, cost))
        case_num += 1
