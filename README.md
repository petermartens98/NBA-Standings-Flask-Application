# NBA-Standings-Flask-Application

This project is a web application built with Python's Flask framework to display up-to-date NBA standings. The application imports required modules such as Flask, pandas, and datetime to handle web requests, data processing, and date/time operations.

The application defines a Flask route to serve as the main landing page and implements a function that leverages pandas and web scraping techniques to retrieve NBA standings data from a website. To optimize performance and reduce network traffic, the data is cached using the functools.lru_cache decorator.

Upon a user's request to view the standings, the application retrieves the cached data and passes it to an HTML template through Flask's render_template function. The HTML template is responsible for rendering the standings in a human-readable format. To ensure data accuracy, the application updates the cached data every hour.

Overall, this project showcases how Python and Flask can be used to create a web application that provides real-time NBA standings, highlighting key features such as web scraping, caching, and data visualization.

## Example Output:
