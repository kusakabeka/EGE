def f(s, c, m):
    if s >= 78: return c % 2 == m % 2
    if c == m: return 0
    # +1(эффективный перебор) +4 *4
    h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 4, c + 1, m)]

    return any(h) if (c + 1) % 2 == m % 2 else all(h)

for s in range(1, 78):
    for m in range(1, 5):
        if f(s, 0, m) == 1:
            if m == 4:print(s)
            break