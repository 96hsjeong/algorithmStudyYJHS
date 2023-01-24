from itertools import product


def solution(users, emoticons):
    answer = [0, 0]

    m = len(emoticons)

    discount_rates = product([10, 20, 30, 40], repeat=m)

    for discount_rate in discount_rates:
        count = 0
        amount = 0

        for ratio, price in users:
            total = 0
            for i, emoticon in enumerate(emoticons):
                if ratio <= discount_rate[i]:
                    total += emoticon * (100 - discount_rate[i]) * 0.01
            if price <= total:
                count += 1
            else:
                amount += total

        answer = max(answer, [count, amount])

    return answer


users = 	[[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
result = [4, 13860]

print(result == solution(users, emoticons))
