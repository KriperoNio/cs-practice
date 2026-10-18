import sys
import pathlib
from logstats import parse_event, count_levels, top_errors, format_report


def main(file_name):
    path = pathlib.Path(__file__).resolve().parent / file_name

    log_lines = []
    correct_lines, incorrect_lines = 0, 0
    with open(path, encoding="utf-8") as log:
        for line in log:
            try:
                if not line.strip():
                    continue

                log_lines.append(parse_event(line.strip()))

                correct_lines += 1
            except Exception as e:
                incorrect_lines += 1

    with open(path, encoding="utf-8") as log:
        counted_levels = count_levels(log)
    
    with open(path, encoding="utf-8") as log:
        c_top_errors = top_errors(log, 2)

    print(correct_lines, incorrect_lines, counted_levels, c_top_errors)


if __name__ == "__main__":
    file_name = sys.stdin.read().strip() or "events.log"
    main(file_name)
