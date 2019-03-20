def odd_sqr_sum(n):
    result = sum([x**2 for x in range(1, n+1) if x % 2 == 1])

    return result


print(odd_sqr_sum(5))


# 1, 9, 25