n = 352
def f(n: int) -> list[int]:
    return [i for i in range(1, n // 2 + 1) if n % i == 0]
print(f(n))
#[1, 2, 3, 4, 6, 8, 11, 12, 22, 24, 33, 44, 66, 88, 132]
#[1, 2, 4, 8, 11, 16, 22, 32, 44, 88, 176]
# 1 2 4 8 11 22