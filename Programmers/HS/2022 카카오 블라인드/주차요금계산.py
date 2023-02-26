from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    cars = set()
    in_time = defaultdict(str)
    total_time = defaultdict(int)

    for record in records:
        time, num, state = record.split(' ')
        cars.add(num)
        if state == "IN":
            in_time[num] = time
        else:
            total_time[num] += calc_time(in_time[num], time)
            in_time[num] = ""

    for num, time in in_time.items():
        if time:
            total_time[num] += calc_time(time, "23:59")

    cars = sorted(list(cars))

    for car in cars:
        answer.append(charge(total_time[car], fees))

    return answer


def calc_time(in_time: str, out_time: str) -> int:
    return convert_time(out_time) - convert_time(in_time)


def convert_time(time: str) -> int:
    h, m = map(int, time.split(':'))
    return 60 * h + m


def charge(time: int, fees: list) -> int:
    base_time, base_fee, unit_time, unit_fee = fees
    if time <= base_time:
        return base_fee
    return base_fee + math.ceil((time - base_time) / unit_time) * unit_fee


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
result = [14600, 34400, 5000]

print(result == solution(fees, records))