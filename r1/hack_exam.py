from math import gcd

def invert(s):
    r = ''
    for c in s:
        if c == 'T':
            r+='F'
        else:
            r+='T'
    return r

def find_best_1_student(answers, points):
    if len(answers)-points > points:
        # they got less than half right
        # flip it and return that
        return invert(answers), len(answers)-points
    return answers, f"{points}/1"

def find_best_multiple_students(records, num_questions):
    common = None
    for (answers, points) in records:
        if common is None:
            common = correct_permutations_outer(answers, points)
        else:
            common = common.intersection(correct_permutations_outer(answers, points))
    count_t = [0 for _ in range(num_questions)]
    for option in common:
        for idx,c in enumerate(option):
            if c == 'T':
                count_t[idx] += 1
    
    answers = ''

    print(common)

    numerator = 0
    denomenator = len(common)
    for c in count_t:
        if denomenator - c > c:
            answers += 'F'
            numerator += denomenator-c
        else:
            answers += 'T'
            numerator += c
    
    g = gcd(numerator, denomenator)
    numerator = int(numerator/g)
    denomenator = int(denomenator/g)

    return answers, f"{numerator}/{denomenator}"

def correct_permutations_outer(answers, points):
    if len(answers)-points > points:
        # they got less than half right
        # flip it and use that
        answers = invert(answers)
        points = len(answers)-points

    num_to_change = len(answers)-points
    bitset = [i=='T' for i in answers]

    bitset_permutations = flip(bitset, num_to_change)
    return set([bitset_to_str(b) for b in bitset_permutations])

def flip(bitset, num):
    result = []
    if num == 0:
        result.append(bitset)
        return result
    if num > len(bitset):
        return result

    head = bitset[0]

    # case where we flip head
    tails = flip(bitset[1:], num-1)
    for t in tails:
        r = [not head]
        r.extend(t)
        result.append(r)

    # case where we don't flip head
    tails = flip(bitset[1:], num)
    for t in tails:
        r = [head]
        r.extend(t)
        result.append(r)

    return result

def copy(bitset):
    return bitset[:]

def bitset_to_str(bitset):
    return "".join(['T' if i else 'F' for i in bitset])

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        num_students,num_questions = [int(i) for i in input().split(' ')]
        if num_students == 1:
            answers,s_points = input().split(' ')
            result_answers, result_points = find_best_1_student(answers, int(s_points))
        else:
            records = []
            for _ in range(num_students):
                answers,s_points = input().split(' ')
                records.append( (answers, int(s_points)) )
            result_answers, result_points = find_best_multiple_students(records, num_questions)
        print("Case #{}: {} {}".format(case_num, result_answers, result_points))
        case_num += 1
