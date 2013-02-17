import string


def make_slug(raw_text):
    punctuation_to_strip = string.punctuation.replace("-", "")
    return str(raw_text).translate(string.maketrans(" ", "-"), punctuation_to_strip).lower()


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return {
        'date': value.strftime("%d %b %y"),
        'time': value.strftime("%H:%M:%S")
    }
