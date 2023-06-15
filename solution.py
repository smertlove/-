from itertools import product



def solution(sequence: str, target: int, signs: list) -> str:
    sign_chains = product(signs, repeat=len(sequence) - 1)
    for chain in sign_chains:
        s = ""
        for num, sign in zip(sequence, chain):
            s += num
            s += sign
        s += "0"
        if eval(s) == target:
            return s
    return 0




def main():
    sequence = "9876543210"
    target = 200
    signs = ['', '-', '+']
    print(solution(sequence, target, signs), "=", target)



if __name__ == "__main__":
    main()
