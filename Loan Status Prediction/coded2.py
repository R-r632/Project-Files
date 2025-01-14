def solve(Q, Queries):
    MAX_X = 10 ** 6 + 1
    steps = [0] * MAX_X
    prefix_steps = [0] * MAX_X

    for x in range(1, MAX_X):
        x_new = (x + 2) // 4  # Rounding off to the nearest integer
        steps[x] = steps[x_new] + 1
        prefix_steps[x] = prefix_steps[x - 1] + steps[x] + 1

    result = []
    for L, R in Queries:
        total_steps = prefix_steps[R] - prefix_steps[L - 1] - 2
        result.append(total_steps)
    return result

Q = int(input())
Queries = [list(map(int, input().split())) for _ in range(Q)]
out_ = solve(Q, Queries)
print(' '.join(map(str, out_)))

