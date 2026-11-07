# Разбирает CSV с заголовком в список словарей. Значения остаются строками.
def csv_to_records(text: str) -> list[dict]:
    result = []
    keys = []

    formated_text = text.strip().splitlines()

    for key in formated_text[0].split(","):
        keys.append(key)

    for line in formated_text[1:]:
        fragment = {}

        for i, value in enumerate(line.split(",")):
            fragment[keys[i]] = value

        result.append(fragment)

    return result


# Простой YAML: «ключ: значение», списки через «- », комментарии после #.
def parse_settings(lines: list[str]) -> dict: ...


# Дополняет записи сведениями из словаря по значению ключа key.
def merge_by_key(rows: list[dict], extra: dict, key: str = id) -> list[dict]: ...


# Список словарей в JSON: отступ 2, ключи по алфавиту, кириллица как есть.
def records_to_json(records: list[dict]) -> str: ...
