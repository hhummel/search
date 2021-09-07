from bitarray import bitarray

from src.types import FeedData


def get_ascii_dict() -> dict[str, bitarray]:
    """
    Dict for keys 0-9 with values as bitarrsys of the ascii encoding
    """
    return {chr(x): bitarray(format(ord(chr(x)), 'b')) for x in range(48, 58)}


def get_field_length(value) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, str):
        a = bitarray()
        a.encode(get_ascii_dict(), value)
        print(f"value: {value} encoding: {a.to01()} encoding length: {len(a.to01())}")
        return len(a.to01())
    raise TypeError(f"get_field_length type of {value} must be str or bool")


def get_mask_mapping(data_by_patient: dict[str, list[dict[str, FeedData]]]) -> dict[int, (str, str)]:
    """ Mapping for bitarray representing data for one patient identifier"""
    if not data_by_patient.values:
        return None

    index = 0
    index_dict = {}
    for value in data_by_patient.values():
        for feed in value:
            feed_id = feed["feed_id"]
            for (feed_key, feed_value) in feed["feed_data"].items():
                index_dict[index] = (feed_id, feed_key)
                index += get_field_length(feed_value)
        break
    return index_dict
