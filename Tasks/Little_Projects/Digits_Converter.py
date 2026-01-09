"""
Simple digits converter from dex to another system by base and vice-versa
"""


def main():
    # tests
    # print(num_to_dex_by_base_string('111111', 2))
    # print(num_to_dex_by_base_string('1AF2', 16))
    # print(find_base(['88', '32', '22', '16', '17']))
    # print(dex_to_num_by_base_string('1000', 16))
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
    if base <= (36): # If the base is within the limit of English letters in lowercase + 10
        inv_hex = inv_hex.lower()
    letters = get_additional_letter_by_base(base)

    for i in range(len(hex_num)):
        n = inv_hex[i]
        n_num = 0
        if n in letters:
            n_num = 10 + letters.index(n)
        else:
            n_num = int(n)
        int_res += n_num * base**i

    return str(int_res)


def get_additional_letter_by_base(base: int) -> str:
    letters = ""
    add_letters = base - 10

    if add_letters > -1:
        for i in range(add_letters):
            letters += chr(ord("a") + i)
    return letters


def dex_to_num_by_base_string(dex_num: str, base: int) -> str:
    result = ""
    letters = get_additional_letter_by_base(base)
    int_dex_num = int(dex_num)
    while int_dex_num > 0:
        num = int_dex_num % base
        int_dex_num = int_dex_num // base
        if num > 9:
            num = letters[num - 10]
        result += str(num)
    return result[::-1]


if __name__ == "__main__":
    main()
