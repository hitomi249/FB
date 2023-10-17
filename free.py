# うるう年を求める関数を作る
# ４の倍数の時はうるう
# １００の倍数で４００で割り切れない時は平年
# ４００の倍数の時はうるうと表示


def uruu(i: int) -> str:
    if i % 100 == 0 and i % 400 == 0:
        return "uruu"
    if i % 4 == 0 and i % 100 == 0:
        return str(i)
    if i % 4 == 0:
        return "uruu"
    return str(i)


if __name__ == "__main__":
        # for i in range(1, 2024):
        #     print(uruu(i))
    print(uruu(2))
    print(uruu(4))
    print(uruu(100))
    print(uruu(400))
    
