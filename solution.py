from itertools import product, zip_longest
from pprint import pprint


def solution(sequence: str, target: int, signs: list) -> list:
    result = []
    sign_chains = product(signs, repeat=len(sequence) - 1)
    for chain in sign_chains:
        s = ""
        for num, sign in zip_longest(sequence, chain, fillvalue=''):
            s += num
            s += sign

        if eval(s) == target:
            result.append(s)
    return result


def main():
    sequence = "9876543210"
    target = 200
    signs = ['', '-', '+']
    pprint(solution(sequence, target, signs))


if __name__ == "__main__":
    main()
