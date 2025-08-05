import re
from .validator import is_valid_date

MONTHS_FULL = {
    "january":1, "february":2, "march":3, "april":4, "may":5, "june":6,
    "july":7, "august":8, "september":9, "october":10, "november":11, "december":12
}
MONTHS_ABBR = {k[:3]: v for k, v in MONTHS_FULL.items()}

def normalize_spaces(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def extract_valid_dates(text: str):
    text = normalize_spaces(text)
    results = []

    # 1) ISO YYYY-MM-DD (year:any digits, month/day 2 digits)
    iso_pattern = r'\b(\d{1,4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b'
    for match in re.findall(iso_pattern, text):
        year, month, day = int(match[0]), int(match[1]), int(match[2])
        if is_valid_date(year, month, day):
            results.append(f"{year:04d}-{month:02d}-{day:02d}")

    # 2) Slash DD/MM/YYYY (day/month 2 digits, year:any digits)
    slash_pattern = r'\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{1,4})\b'
    for match in re.findall(slash_pattern, text):
        day, month, year = int(match[0]), int(match[1]), int(match[2])
        if is_valid_date(year, month, day):
            results.append(f"{day:02d}/{month:02d}/{year:04d}")

    # 3) Long month or short month name
    # Month DD, YYYY or Mon DD, YYYY with optional extra spaces
    long_month_pattern = long_month_pattern = (
        r'\b('
        r'Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|'
        r'Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?'
        r')\s+(\d{1,2}),\s*(\d{1,4})\b'
    )
    for match in re.findall(long_month_pattern, text):
        month_str, day, year = match[0], int(match[1]), int(match[2])
        month_key = month_str.lower()[:3]
        month = MONTHS_ABBR.get(month_key)
        if month and is_valid_date(year, month, day):
            # preserve original case & spacing approx.
            results.append(f"{month_str} {day}, {year}")

    return results
