def solution(cap, n, deliveries, pickups):
    answer = 0

    total_delivery = 0
    total_pickup = 0

    last_delivery_house = -1
    last_pickup_house = -1

    for i in range(n):
        if deliveries[i] != 0:
            total_delivery += deliveries[i]
            last_delivery_house = i
        if pickups[i] != 0:
            total_pickup += pickups[i]
            last_pickup_house = i

    while total_delivery > 0 or total_pickup > 0:
        answer += (max(last_delivery_house, last_pickup_house) + 1) * 2

        total_delivery, last_delivery_house = visit(cap, deliveries, total_delivery, last_delivery_house)
        total_pickup, last_pickup_house = visit(cap, pickups, total_pickup, last_pickup_house)

    return answer


def visit(cap, house, total, last_house):
    for i in range(last_house, -1, -1):
        if cap < house[i]:
            house[i] -= cap
            total -= cap
            return total, i
        else:
            cap -= house[i]
            total -= house[i]
            house[i] = 0

    return total, -1


cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
result = 16

print(result == solution(cap, n, deliveries, pickups))