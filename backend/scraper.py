import requests
from bs4 import BeautifulSoup

def run_scraper(location, min_price, max_price, num_pages=1):
    base_url = f"https://{location}.craigslist.org/search/apa"
    all_listings = []

    for page in range(num_pages):
        params = {"s": page*120, "min_price": min_price, "max_price": max_price}
        response = requests.get(base_url, params=params)
        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.find_all("li", class_="result-row")
        
        for listing in listings:
            title_tag = listing.find("a", class_="result-title")
            price_tag = listing.find("span", class_="result-price")
            link_tag = listing.find("a", class_="result-title")
            date_tag = listing.find("time", class_="result-date")
            
            if title_tag and price_tag and link_tag and date_tag:
                all_listings.append({
                    "title": title_tag.text,
                    "price": price_tag.text,
                    "link": link_tag["href"],
                    "date_posted": date_tag["datetime"]
                })
    
    return all_listings
