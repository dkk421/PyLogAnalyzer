import re

LOG_PATTERN = re.compile(
    r"^(?P<timestamp>\S+\s+\S+)\s+\[(?P<level>\w+)\]\s+(?P<message>.+)$"
)


def parse_line(line: str):
    line = line.strip()

    if not line:
        return None

    match = LOG_PATTERN.match(line)

    if not match:
        return {
            "timestamp": None,
            "level": "UNKNOWN",
            "message": line,
            "raw_line": line
        }

    return {
        "timestamp": match.group("timestamp"),
        "level": match.group("level"),
        "message": match.group("message"),
        "raw_line": line
    }