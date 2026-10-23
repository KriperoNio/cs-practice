import sys
import pathlib
from logstats import parse_event, count_levels, top_errors, format_report


def main(file_name):
    base = pathlib.Path(__file__).resolve().parent
    path = base / file_name

    total, errors, broken = 0, 0, 0
    with open(path, encoding="utf-8") as log:
        for line in log:
            if not line.strip():
                continue
            total += 1
            try:
                event = parse_event(line.strip())
            except ValueError as e:
                broken += 1
                continue
            if event["level"] == "ERROR":
                errors += 1

    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(path, encoding="utf-8") as log:
        tops = top_errors(log, 2)

    print(total)
    print(errors)
    print(broken)

    report = format_report(counts, tops)
    with open(base / "report.txt", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    file_name = sys.stdin.read().strip() or "events.log"
    main(file_name)
