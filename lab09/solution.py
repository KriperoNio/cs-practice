import numpy as np


def make_hours() -> list[int]:
    return np.arange(0, 24, 3).tolist()


def vector_report(value: list[float]) -> dict:
    return {
        "third": value[3],
        "last": value[-1],
        "middle": value[2:6],
        "every_second": value[::2],
        "reversed": value[::-1],
    }


def change_vector(values: list[float]) -> list[float]: 
    vector = np.array(values)
    
    copy = vector.copy()
    copy[2:4] = 99
    copy[::2] = -1
    
    return copy.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    vector = np.array(values)
    mask = vector > limit
    
    copy = vector.copy()
    copy[mask] = limit
    
    return copy.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    vector = np.array(values)
    
    fahrenheit = vector * 9 / 5 + 32
    
    return fahrenheit.tolist()
