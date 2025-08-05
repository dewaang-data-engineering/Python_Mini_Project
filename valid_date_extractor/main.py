from valid_date_extractor.extractor import extract_valid_dates

if __name__ == "__main__":
    with open("sample_dataset.txt", "r", encoding="utf-8") as f:
        text = f.read()

    dates = extract_valid_dates(text)
    for d in dates:
        print(d)
