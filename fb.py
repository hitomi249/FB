# fizzbuzz問題
# 3の倍数の時はfizz
# 5の倍数の時はbuzz
# 3の倍数かつ5の倍数の時はfizzbuzzと表示


def fizzbuzz(i: int) -> str:
    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    if i % 3 == 0:
        return "fizz"
    if i % 5 == 0:
        return "buzz"
    return str(i)


if __name__ == "__main__":
    for i in range(1, 101):
        print(fizzbuzz(i))
