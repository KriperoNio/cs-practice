import sys
from stats import average_by_city, read_valid, warmest_city

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()

    data = read_valid(lines)

    correct_lines = len(data.values)
    passed_lines = len(lines) - correct_lines

    
    
    print(len(lines))
    print(0)
    print(total[best] / count[best])