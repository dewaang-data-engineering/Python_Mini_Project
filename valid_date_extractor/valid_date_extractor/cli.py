import argparse
from valid_date_extractor.extractor import extract_valid_dates

def main():
    parser = argparse.ArgumentParser(description="Extract valid dates from a text file.")
    parser.add_argument('file', type=str, help="Path to a text file")
    args = parser.parse_args()

    with open(args.file, 'r', encoding='utf-8') as f:
        text = f.read()

    dates = extract_valid_dates(text)
    for d in dates:
        print(d)

if __name__ == '__main__':
    main()
