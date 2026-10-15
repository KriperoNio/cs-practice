# Разбирает строки журнала, пропуская пустые и негодные.
def read_valid(lines: list[str]):
    data: list[dict] = []

    for line in lines:
        if not line.strip():
            continue # Empty — pass
        try:
            parsed_line = parse_record(line.strip())

            data.append(parsed_line)
        except ValueError as a:
            print(a)

    return data

# Разбирает строку «город;температура;дата» в словарь.
def parse_record(line: str):
    data = {}

    city, temp, date = line.split(";")
    
    if not city or not date:
        raise ValueError('Not enough values in field')

    data['city'] = city.strip()
    if not city:
        raise ValueError(f"Empty city: {line!r}")
    
    data['date'] = date.strip()
    if not date:
        raise ValueError(f"Empty data: {line!r}")

    if not temp.strip():
        raise ValueError(f"Empty tempirature: {line!r}")
    try:
        data['temperature'] = float(temp.replace(",", "."))
    except:
        raise ValueError(f'Temperature is not float, is {type(temp)}({temp})')

    if len(data.values()) != 3: 
        raise ValueError('Not enough or too much fields')
    
    return data

# Средняя температура по каждому городу
def average_by_city(records: list[dict]):
    data = {}

    for record in records:
        city = record['city']
        if city not in data:
            data[city] = {}

        data[city]['count'] = data[city].get('count', 0) + 1
        data[city]['total_temp'] = data[city].get('total_temp', 0) + record['temperature']

    return {
        city: stats["total_temp"] / stats["count"] for city, stats in data.items()
    }

# Город с наибольшей средней температурой. 
def warmest_city(records: list[dict]):
    if not records:
        return ""
    
    return min(records, key = lambda r: (-r['temperature'], r['city']))['city']