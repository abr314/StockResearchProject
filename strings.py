from enum import Enum

DATE_LABEL = "Date"
HIGH_LABEL = " High"
LOW_LABEL = " Low"
OPEN_LABEL = " Open"
VOLUME_LABEL = " Volume"

class Categories(Enum):
    high = HIGH_LABEL
    low = LOW_LABEL
    date = DATE_LABEL
    open = OPEN_LABEL
    volume = VOLUME_LABEL