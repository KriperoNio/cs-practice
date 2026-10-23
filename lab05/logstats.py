# from enum import StrEnum


# class MessageLevel(StrEnum):
#     INFO = "INFO"
#     DEBUG = "DEBUG"
#     WARNING = "WARNING"
#     ERROR = "ERROR"

#     BROKEN = "BROKEN"

#     @classmethod
#     def _missing_(cls, value):
#         # Метод срабатывает, только если переданного value нет среди значений выше
#         return cls.BROKEN

_KNOWN_LEVELS = {"INFO", "DEBUG", "WARNING", "ERROR"}


def parse_event(line: str):
    data = {}

    time, level, message = map(lambda el: el.strip(), line.strip().split(maxsplit=2))

    if not time:
        raise ValueError(f"Time is empty ({type(time)}|{time})")
    data["time"] = time

    # Если строка не с заглавных букв, то это не уровень, что очень критично!
    if not level or level.upper() != level:
        raise ValueError(f"Level is ({type(level)}|{level})")
    data["level"] = level if level in _KNOWN_LEVELS else "BROKEN"

    if not message:
        raise ValueError(f"Message is empty ({type(message)}|{message})")
    data["message"] = message

    return data


# Сколько строк каждого уровня. Негодные строки считаются под ключом BROKEN.
def count_levels(lines: list[str]):
    data = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.strip().split(" ", maxsplit=2)
        if len(parts) < 2:
            key = "BROKEN"
        else:
            raw = parts[1].strip()
            key = raw if raw in _KNOWN_LEVELS else "BROKEN"
        data[key] = data.get(key, 0) + 1
    return data


# n самых частых сообщений уровня ERROR: пары «сообщение, сколько раз».
def top_errors(lines: list[str], n: int):
    data = {}

    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            data[msg] = data.get(msg, 0) + 1

    items = sorted(data.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[message, count] for message, count in items[:n]]


# Текст отчёта: строки «уровень: количество» и список частых ошибок.
def format_report(counts: dict, errors: list[list]):
    lines = ["Отчёт по журналу", ""]

    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"
