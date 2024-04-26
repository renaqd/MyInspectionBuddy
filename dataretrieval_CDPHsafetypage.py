# this script is for Abby's device safety page
# this script works and provides the hyperlink to the recall page
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


def search_recall(query):
    base_url = "https://www.cdph.ca.gov"
    url = base_url + "/Programs/CEH/DFDCS/Pages/FDBPrograms/DeviceRecalls.aspx"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }  # Some websites require a User-Agent header to mimic a web browser

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a", href=True)

        found = False
        for link in links:
            if re.search(r'\b{}\b'.format(re.escape(query)), link.text, re.IGNORECASE) or re.search(
                    r'\b{}\b'.format(re.escape(query)), link["href"], re.IGNORECASE):
                print("Match found:")
                print("- Text:", link.text.strip())
                full_url = urljoin(base_url, link["href"])
                print("- URL:", full_url)
                found = True

        if not found:
            print("No results found for your query.")
    else:
        print("Failed to retrieve data from the website.")


def main():
    query = input("Enter your search query: ")
    search_recall(query)


if __name__ == "__main__":
    main()
