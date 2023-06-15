from itertools import product, zip_longest



def solution(sequence: str, target: int, signs: list) -> str:
    sign_chains = product(signs, repeat=len(sequence) - 1)
    for chain in sign_chains:
        s = ""
        for num, sign in zip_longest(sequence, chain, fillvalue=''):
            s += num
            s += sign

        if eval(s) == target:
            return s
    return 0




def main():
    sequence = "9876543211"
    target = 200
    signs = ['', '-', '+']
    print(solution(sequence, target, signs), "=", target)



if __name__ == "__main__":
    main()
