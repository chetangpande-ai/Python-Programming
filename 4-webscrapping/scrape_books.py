import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/100-books-to-read-in-a-lifetime/b?ie=UTF8&node=4348234031"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

books = []

# This selector may need to be updated based on the actual HTML structure
for item in soup.select(".s-result-item"):
    name = item.select_one("h2 span")
    rating = item.select_one(".a-icon-alt")
    price = item.select_one(".a-price-whole")
    if name and rating and price:
        print(name.text.strip(), rating.text.strip(), price.text.strip())
        books.append({
            "Book Name": name.text.strip(),
            "Star Rating": rating.text.strip(),
            "Price": price.text.strip()
        })

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Book Name", "Star Rating", "Price"])
    writer.writeheader()
    writer.writerows(books)

print("Scraping complete. Data saved to books.csv")
