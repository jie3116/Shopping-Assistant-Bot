import requests
from bs4 import BeautifulSoup
#import urllib.parse
#import os

def scrape_products_from_tokopedia(query: str):
    url = f"https://www.tokopedia.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    #affiliate_id = os.getenv("AFFILIATE_ID", "YOUR_AFFILIATE_ID")  # Ambil dari ENV
    products = []

    for item in soup.select("div.css-1f2quy3"):
        try:
            name_tag = item.select_one("div.css-1b6t4dn")
            price_tag = item.select_one("div.css-o5uqvq")
            if not name_tag or not price_tag:
                continue

            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)

            link_tag = item.find("a", href=True)
            if not link_tag:
                continue
            original_url = "https:" + link_tag["href"]

            #encoded_url = urllib.parse.quote_plus(original_url)
            #affiliate_url = f"https://ta.tokopedia.com/affiliate/click?url={encoded_url}&ref={affiliate_id}"

            rating_tag = item.select_one("span.css-1ffszw2")
            rating = rating_tag.get_text(strip=True) if rating_tag else "No rating"

            desc_tag = item.select_one("span.css-1kdc32b")
            specs = desc_tag.get_text(strip=True) if desc_tag else "No specs"

            products.append({
                "name": name,
                "price": price,
                #"url": affiliate_url,
                "original_url": original_url,
                "rating": rating,
                "specs": specs,
                "source": "Tokopedia"
            })

        except Exception as e:
            print("❌ Error parsing product:", e)
            continue

    print("✅ Produk ditemukan:", len(products))
    for p in products:
        print(p)

    return products
