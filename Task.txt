### **Extract Valid Dates in Multiple Formats**
---
Create a Python package named valid_date_extractor that:

Reads a text file
Extracts only valid dates in:

- YYYY-MM-DD
- DD/MM/YYYY
- Month DD, YYYY or Mon DD, YYYY

Ignores invalid dates (wrong months, wrong days, invalid leap years)

Can be used both as a library and from the command line.
1. **ISO style:** `YYYY-MM-DD`

   * Year: 1900–2099
   * Month: 01–12
   * Day: Must be valid for that month (e.g., Feb 29 only in leap years)

2. **Slash style:** `DD/MM/YYYY`

   * Day: 01–31 (valid for month)
   * Month: 01–12
   * Year: 1900–2099

3. **Long style:** `Month DD, YYYY` or `Mon DD, YYYY`

   * Month name: Full or 3-letter abbreviation (case-insensitive)
   * Day: 1–31 (must match month validity)
   * Year: 1900–2099

---

#### **Rules**

* Ignore invalid dates like:

  * `32/13/2020`
  * `2020-02-30`
  * `April 31, 2020`
  * `Feb 29, 2023` (non-leap year)
* Handle **extra spaces** between words and numbers.
* Months may be **mixed case** (e.g., `jAn 05, 2020` should match if valid).
* No hardcoding of valid dates — **validate using regex + Python date validation**.

---

#### **Example Expected Output**

```text
2024-05-21
2023-12-31
14/02/2024
Mar 05, 2023
September 1, 2022
1999-12-25
15/08/2025
Jul 4, 2021
Feb 29, 2024
June 7, 2020
2020-01-01
31/12/2020
Dec 31, 2020
````

---
 