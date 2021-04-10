def prime_solitaire(cards):
    best_score = 0
    for pair in split_permutations(cards):
        s = sum(pair.a)
        p = prod(pair.b)
        if s == p and s > best_score:
            best_score = s
    return best_score

def prod(l):
    total = 1
    for i in l:
        total *= i
    return total

def split_permutations(cards):
    result = []
    head = cards[0]

    if len(cards) == 1:
        return [Pair([head], []), Pair([], [head])]

    tail_perms = split_permutations(cards[1:])
    for t in tail_perms:
        a = t.a
        b = t.b
        result.append(Pair(a + [head], b))
        result.append(Pair(a, b + [head]))
    yield result

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f"|{self.a}<>{self.b}|"

if __name__ == "__main__":
    num_cases = int(input())
    case_num = 1
    while case_num <= num_cases:
        cards = []
        rows = int(input())
        for _ in range(rows):
            card,num = [int(i) for i in input().split(' ')]
            for _ in range(num):
                cards.append(card)
        points = prime_solitaire(cards)
        print("Case #{}: {}".format(case_num, points))
        case_num += 1
