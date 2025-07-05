from backend.services.scraper import scrape_products_from_tokopedia

def search_product(query: str):
    scraped = scrape_products_from_tokopedia(query)
    results = []

    for product in scraped:
        results.append({
            "name": product.get("name"),
            "price": product.get("price"),
            #"url": product.get("url"),  # ini affiliate_url
            "original_url": product.get("original_url"),  # opsional
            "rating": product.get("rating"),              # opsional
            "specs": product.get("specs"),                # opsional
            "source": "Tokopedia"
        })

    return {"query": query, "results": results}
