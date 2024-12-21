from newspaper import Article
import requests
from bs4 import BeautifulSoup

# Function to scrape news based on category
def get_news(category):
    category_urls = {
        "business": "https://www.reuters.com/business/",
        "market": "https://www.reuters.com/markets/",
        "technology": "https://www.reuters.com/technology/",
        "sports": "https://www.reuters.com/lifestyle/sports/",
        "entertainment": "https://www.reuters.com/lifestyle/entertainment/"
    }
    url = category_urls.get(category)
    news_data = []

    # Scrape the news website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get articles from the main section
    articles = soup.find_all('article', class_='story')

    for article in articles[:5]:  # Fetch top 5 articles
        article_url = article.find('a', href=True)['href']
        full_url = "https://www.reuters.com" + article_url
        article_title = article.find('h3').text.strip()

        # Get full article content
        article_obj = Article(full_url)
        article_obj.download()
        article_obj.parse()

        news_data.append({
            "title": article_title,
            "url": full_url,
            "content": article_obj.text
        })
        
def get_news(category):
    # Hardcoded articles for testing different categories
    if category == "technology":
        return [
            {"title": "AI Revolution in Tech", "content": "Artificial Intelligence is transforming the technology industry."},
            {"title": "5G Technology Expands", "content": "5G networks are growing rapidly across the globe."},
            {"title": "Quantum Computing Breakthrough", "content": "Quantum computing is making huge strides in performance."}
        ]
    elif category == "business":
        return [
            {"title": "Stock Market Surges", "content": "The stock market has seen significant growth this week."},
            {"title": "Startup Boom Continues", "content": "Startups are seeing a surge in funding despite economic challenges."}
        ]
    elif category == "market":
        return [
            {"title": "Market Trends 2024", "content": "The markets are experiencing a mix of highs and lows this quarter."},
            {"title": "Commodities Prices Soar", "content": "Commodity prices are skyrocketing due to supply chain disruptions."}
        ]
    else:
        return []  # Return an empty list if no articles are found for the category


    return news_data
