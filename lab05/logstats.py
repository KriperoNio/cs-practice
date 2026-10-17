from enum import StrEnum


class MessageLevel(StrEnum):
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"

    BROKEN = "BROKEN"

    @classmethod
    def _missing_(cls, value):
        # Метод срабатывает, только если переданного value нет среди значений выше
        return cls.BROKEN


# Строка журнала «время уровень сообщение» в словарь. Негодная строка — ValueError.
def parse_event(line: str):
    data = {}

    time, level, message = line.split(" ", maxsplit=2)

    if not time.strip():
        raise ValueError(f"Time is empty ({type(time)}|{time})")
    data["time"] = time

    if not level.strip():
        raise ValueError(f"Level is empty ({type(level)}|{level})")
    data["level"] = MessageLevel(level).value

    if not message.strip():
        raise ValueError(f"Message is empty ({type(message)}|{message})")
    data["message"] = message

    return data


assert parse_event("2026-03-01T09:03:55 ERROR Не удалось открыть файл data.csv") == {
    "time": "2026-03-01T09:03:55",
    "level": "ERROR",
    "message": "Не удалось открыть файл data.csv",
}, "Invalid parse level: waited ERROR"
assert parse_event("2026-03-01T09:03:55 ERROR- Не удалось открыть файл data.csv") == {
    "time": "2026-03-01T09:03:55",
    "level": "BROKEN",
    "message": "Не удалось открыть файл data.csv",
}, "Invalid parse level: waited BROKEN"


# Сколько строк каждого уровня. Негодные строки считаются под ключом BROKEN.
def count_levels(lines: list[str]):
    return dict


# n самых частых сообщений уровня ERROR: пары «сообщение, сколько раз».
def top_errors(lines: list[str], n: int):
    return list[list]


# Текст отчёта: строки «уровень: количество» и список частых ошибок.
def format_report(counts: dict, errors: list[list]):
    return str
