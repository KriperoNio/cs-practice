# Разбирает строки журнала, пропуская пустые и негодные.
def read_valid(lines: list[str]):
    data: list[dict] = []

    for line in lines:
        try:
            parsed_line = parse_record(line)

            data += parsed_line
        except ValueError:
            ...

    return data

# Разбирает строку «город;температура;дата» в словарь.
def parse_record(line: str):
    data = {}

    city, temp, date = line.split(";")
    
    if not city or not date:
        raise ValueError('Not enough values in field')

    data['city'] = city
    data['date'] = date

    try:
        data['temp'] =  float(temp)
    except:
        raise ValueError(f'Temperature is not float, is {type(temp)}')

    if len(data.values) != 3: 
        raise ValueError('Not enough fields')
    
    return data

# Средняя температура по каждому городу
def average_by_city(records: list[dict]):
    raise ValueError('Not implemented')

# Город с наибольшей средней температурой. 
def warmest_city(records: list[dict]):
    raise ValueError('Not implemented')