def solve(Q, Queries):
    results = []
    for L, R in Queries:
        count = 0
        while L <= R:
            # Calculate the sum of the range [L, R]
            total = R - L + 1
            if total == 1:
                count += 1
                break
            
            # Replace two numbers a and b with (a+b)//4
            R = (R + 3) // 4  # Apply the reduction rule (ceil division)
            count += 1

        results.append(count)
    return results


# Input processing
Q = int(input())
Queries = [list(map(int, input().split())) for _ in range(Q)]

# Solve and print the output
out = solve(Q, Queries)
print(" ".join(map(str, out)))
