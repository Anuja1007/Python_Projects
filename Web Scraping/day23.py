"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


def scrape_h2_headers(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Network error:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    headers = []

    h2_tags = soup.find_all("h2")

    # DEBUG (optional)
    print(f"Found {len(h2_tags)} <h2> tags")

    for h2 in h2_tags:
        text = h2.get_text(separator=" ", strip=True)
        text = text.replace("[edit]", "").strip()

        if text and text.lower() != "contents":
            headers.append(text)

    return headers


def main():
    headers = scrape_h2_headers(URL)

    if not headers:
        print("❌ No headers found.")
        return

    print(f"\n✅ Total <h2> headers found: {len(headers)}\n")
    print("First 10 section titles:\n")

    for i, title in enumerate(headers[:10], start=1):
        print(f"{i}. {title}")


if __name__ == "__main__":
    main()
