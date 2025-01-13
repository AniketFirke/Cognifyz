import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page = None
        self.soup = None

    def fetch_page(self):
        """Fetch the content of the page using requests."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            self.page = response.content
            self.soup = BeautifulSoup(self.page, 'html.parser')
            print(f"Successfully fetched content from {self.url}\n")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")

    def scrape_data(self):
        """Scrape data from the page based on specific tags and classes."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class NewsScraper(WebScraper):
    def scrape_data(self):
        """Scrape headlines from a news website (e.g., BBC, CNN)."""
        headlines = []
        # Adjust the selector based on the website you're scraping
        for item in self.soup.find_all('h3'):  # Example for a general h3 headline
            title = item.get_text(strip=True)
            if title:
                headlines.append(title)
        return headlines


class QuotesScraper(WebScraper):
    def scrape_data(self):
        """Scrape quotes and their authors from a quotes website."""
        quotes = []
        try:
            # Find all quote containers (adjust the selector based on the website structure)
            for quote_item in self.soup.find_all('div', class_='quote'):
                quote_text = quote_item.find('span', class_='text').get_text(strip=True)
                author = quote_item.find('small', class_='author').get_text(strip=True)
                quotes.append({'quote': quote_text, 'author': author})
        except AttributeError:
            print("Error scraping quotes data.")
        return quotes


def main():
    print("Interactive Web Scraping Program")

    # User selects the type of website they want to scrape
    print("Choose the type of website to scrape:")
    print("1. News Website")
    print("2. Quotes Website")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        url = input("Enter the news website URL (e.g., https://www.indiatoday.in/): ")
        scraper = NewsScraper(url)
    elif choice == '2':
        url = input("Enter the quotes website URL (e.g.,http://quotes.toscrape.com): ")
        scraper = QuotesScraper(url)
    else:
        print("Exiting program.")
        return

    # Fetch page and scrape data
    scraper.fetch_page()
    data = scraper.scrape_data()

    # Display the scraped data
    if choice == '1':
        print("\nTop Headlines:")
        for i, headline in enumerate(data, start=1):
            print(f"{i}. {headline}")
    elif choice == '2':
        print("\nQuotes:")
        if data:
            for i, quote_data in enumerate(data, start=1):
                print(f"{i}. \"{quote_data['quote']}\" — {quote_data['author']}")
    else:
        print("Failed to retrieve weather information.")


if __name__ == "__main__":
    main()
