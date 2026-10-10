import sys
from stats import average_by_city, read_valid, warmest_city

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()

    if len(lines) < 3: raise ValueError('Not enough count fields')

    total = {}
    count = {}

    for line in lines:
        city, temp, date = line.split(";")
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1

    best = ""
    for city in total:
        if best == "" or total[city] / count[city] > total[best] / count[best]:
            best = city
    print(len(lines))
    print(0)
    print(total[best] / count[best])