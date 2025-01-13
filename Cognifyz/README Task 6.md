* WebScraper Class:

    The base class provides the core functionality for fetching the web page and parsing it with BeautifulSoup.
    The fetch_page() method fetches the web page content using requests and initializes the BeautifulSoup object.
    The scrape_data() method is an abstract method that should be implemented by subclasses to define specific scraping logic.

* NewsScraper Class:

    Inherits from WebScraper and overrides the scrape_data() method to scrape headlines. Here, we search for all <h3> tags and extract the text.
    The find_all() method is used to extract all elements of a particular tag (like headlines).

* WeatherScraper Class:

    Inherits from WebScraper and overrides the scrape_data() method to extract temperature and weather condition data.
    The find() method looks for specific elements with the class names for temperature and condition.

* Main Program:

    The user is prompted to choose the type of website they want to scrape (news or weather).
    Based on the selection, the appropriate scraper class is instantiated and the data is fetched and displayed.


-----------------------------------------------------------------------------------------------------------------
Testing the Program:

1) News Website:

    You can test the program with news websites like BBC or CNN.
    The class NewsScraper can be adjusted to match the HTML structure of different news websites.

2) Weather Website:

    You can test it with websites like weather.com by providing the URL and ensuring that the class WeatherScraper targets the right elements to extract temperature and condition.

* API and File Handling:

The code currently uses interactive input from the user. To turn it into a more automated process, we could wrap the scraping functionality in a web API or script to regularly fetch the data, save it to a database, or generate periodic reports.