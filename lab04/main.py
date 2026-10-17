import sys
from stats import average_by_city, read_valid, warmest_city

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()

    data = read_valid(lines)

    correct_lines = len(data)
    passed_lines = \
        len([line for line in lines if line.strip() != ""])\
            - correct_lines

    stat = average_by_city(data)
    best_avg_temp = max(stat.values() or [0.0])
    
    print(correct_lines)
    print(passed_lines)
    print('%.1f' % best_avg_temp)

# Азов;24.5;2026-07-01
# мусор
# Азов;25.5;2026-07-02
# Астрахань;25.0;2026-08-09
# мусор; ;2026-07-01
# ;
# 
# Таганрог;30,0;2026-07-01