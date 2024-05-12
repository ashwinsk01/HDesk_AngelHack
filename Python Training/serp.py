from serpapi import GoogleSearch

def fetch_google_trends(query):
    params = {
        "api_key": "1627678c73594567acf10b1aff2f322a72b7658476fd6f4ead95ea8fea57734d",  # Replace with your SerpApi API key
        "engine": "google_trends",
        "q": query,  # Your keyword or search term
        "tz": "360"  # Timezone offset (e.g., "360" for CST)
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results

# Ask the user for the keyword
keyword = input("Please enter the keyword to search trends for: ")

# Fetch and display the trends data
trends_data = fetch_google_trends(keyword)
print(trends_data)
