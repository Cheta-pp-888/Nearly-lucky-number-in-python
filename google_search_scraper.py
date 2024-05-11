import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Send a GET request to the website
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract news articles
    articles = soup.find_all('article')  # Adjust this based on the HTML structure of the website

    for article in articles:
        # Extract article title
        title = article.find('h2').text.strip()
        
        # Extract article summary
        summary = article.find('p').text.strip()

        # Extract article link
        link = article.find('a')['href']

        print(f"Title: {title}")
        print(f"Summary: {summary}")
        print(f"Link: {link}")
        print()

if __name__ == "__main__":
    abp_majha_url = "https://abpmajha.abplive.in/"
    india_tv_url = "https://www.indiatvnews.com/"

    print("ABP Majha News:")
    scrape_news(abp_majha_url)

    print("\nIndia TV News:")
    scrape_news(india_tv_url)
