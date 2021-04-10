def append_sort(nums):
    moves = 0
    for i in range(1, len(nums)):
        prev = nums[i-1]
        current = nums[i]
        if prev < current:
            continue
        s_prev = str(prev)
        s_curr = str(current)
        if prev == current:
            extra = '0'
        elif s_prev.startswith(s_curr):
            extra = s_prev[len(s_curr):]
            if extra.count('9') == len(extra):
                extra = '0' * (len(extra)+1)
            else:
                num_digits = len(extra)
                extra = str(int(extra) + 1)
                extra = extra.zfill(num_digits)

        else:
            extra = ''
            while prev >= current:
                extra += '0'
                current *= 10

        print(current, extra)

        nums[i] = int(s_curr + extra)
        moves += len(extra)
    print(nums)
    return moves

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        l = input()
        nums = [int(i) for i in input().split(' ')]
        moves = append_sort(nums)
        print("Case #{}: {}".format(case_num, moves))
        case_num += 1
