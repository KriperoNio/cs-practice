import pathlib, os


def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}

    for path in paths:
        name = path.rsplit("/", 1)[-1]

        if "." in name and not name.startswith("."):
            extension = name.rsplit(".", 1)[1].lower()
        else:
            extension = ""

        result[extension] = result.get(extension, 0) + 1

    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""

    return min(paths, key=lambda path: (-path.count("/"), path))


def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    unit = 0

    while size >= 1024 and unit < len(units) - 1:
        size /= 1024
        unit += 1

    if unit == 0:
        return f"{size:.0f} {units[unit]}"

    return f"{size:.1f} {units[unit]}"


paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

count_by_extension(paths)  # {"pdf": 1, "txt": 1, "png": 1, "": 1}
deepest_path(paths)  # "docs/img/logo.png"

human_size(900)  # "900 Б"
human_size(1536)  # "1.5 КБ"
human_size(5 * 1024 * 1024)  # "5.0 МБ"
