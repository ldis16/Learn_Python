"""
Simple digits converter from dex to another system by base and vice-versa
"""
import random

def main():
    # tests
    base = 1616
    print("Base:", base)
    num = 161616161616
    print("num:", num)
    rnd_base_num = dex_to_num_by_base_string(num, base)
    print("new num:", rnd_base_num)
    reverse_num = num_to_dex_by_base_string(rnd_base_num, base)
    print("reverse num:", reverse_num)
    ...


def find_base(seq: list) -> str:
    result = 0
    start_num = 0
    max_base = 10 + 26
    is_less_than_10 = "".join(seq).isdigit()
    if is_less_than_10:
        start_num = max([int(i) for i in "".join(seq)])
    else:
        start_num = 10

    for i in range(start_num, max_base + 1):
        dec_seq = [int(num_to_dex_by_base_string(n, i)) for n in seq]
        if dec_seq[0] == sum(dec_seq[1:]):
            result = i
            break
    if result == 0:
        return "Not Found"
    else:
        return result


def num_to_dex_by_base_string(hex_num: str, base: int) -> str:
    int_res = 0
    inv_hex = hex_num[::-1]
    if base <= 36:  # If the base is within the limit of English letters in lowercase + 10
        inv_hex = inv_hex.lower()

    for i in range(len(hex_num)):
        n = inv_hex[i]
        n_num = 0
        if n.isdecimal():
            n_num = int(n)
        else:
            n_num = 10 + ord(n) - ord("a")
            
        int_res += n_num * base**i

    return str(int_res)


def dex_to_num_by_base_string(dex_num: str, base: int) -> str:
    result = ""
    int_dex_num = int(dex_num)
    while int_dex_num > 0:
        num = int_dex_num % base
        int_dex_num = int_dex_num // base
        if num > 9:
            num = chr(ord("a") + (num - 10))
        result += str(num)
    return result[::-1]


if __name__ == "__main__":
    main()
