# News-App-with-Api
News App to Fetch Top 10 Latest News from the US

This Python script fetches the top 10 latest news from the US using the News API. The script uses the requests library to make an API call and extracts the titles of the latest news articles. The news API key (apikey) is required to access the API and fetch the news.
Overview of Code:

    API Key: You need a valid News API key (apikey).
    Fetching the News: The script sends a request to the News API endpoint for top headlines from the US.
    Processing the Response: The response is parsed as JSON, and the titles of the articles are extracted and printed.
    Displaying the Latest News: The script prints the top 10 latest news headlines.

Full Code:

python

import requests

# API key for News API
apikey = "1c3d661bb65e48d38165d75873835580"

def getnews():
    # URL to fetch the top headlines from the US
    newsurl = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + apikey
    
    # Send a GET request to the news API and parse the JSON response
    news = requests.get(newsurl).json()

    # Extract articles from the response
    articles = news["articles"]
    
    # Prepare a list to hold the article titles
    newarticle = []
    
    # Loop through the articles and append each title to the list
    for arti in articles:
        newarticle.append(arti["title"])
    
    # Print the top 10 news articles
    for i in range(min(10, len(newarticle))):  # Handle cases where there are fewer than 10 articles
        print(f"The News No {i+1} is:\n\n{newarticle[i]}")

# Call the function to get and print the latest news
getnews()

How the Code Works:

    News API URL:
        The API URL for fetching top headlines is "https://newsapi.org/v2/top-headlines?country=us&apiKey=".
        The country=us query parameter ensures we are fetching news from the US.

    Requests Library:
        The requests.get(newsurl) sends an HTTP GET request to the News API.
        .json() converts the response into a Python dictionary.

    Extract Articles:
        The articles are stored in news["articles"] and each article is a dictionary containing details like the title, description, etc.
        We extract only the title of each article with arti["title"].

    Print Top 10 Headlines:
        The script loops through the first 10 headlines and prints them.

Key Points to Note:

    API Key: Replace the API key (apikey) with your own valid key from NewsAPI. You can sign up for free access to the API, which gives you limited free usage.

    Error Handling: You should include error handling in case the request fails (e.g., due to network issues or invalid API key). For instance:

    python

if news.get("status") != "ok":
    print("Failed to fetch news.")

Limitation: The News API returns a limited number of articles based on the plan you are subscribed to. Free plans may have a limit on the number of requests and articles you can fetch.
