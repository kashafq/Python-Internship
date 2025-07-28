#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json

API_KEY = "put_your_api_key_here"  
BASE_URL = "https://newsapi.org/v2/everything"

def get_news(keyword):
    try:
        params = {
            "q": keyword,
            "apiKey": API_KEY,
            "language": "en",
            "pageSize": 5,
            "sortBy": "publishedAt"
        }
        response = requests.get(BASE_URL, params=params)
        print(" URL:", response.url)  
        response.raise_for_status()
        data = response.json()

        if data["status"] != "ok":
            print(f"! API error: {data.get('message', 'Unknown error')}")
            return None

        articles = data["articles"]
        if not articles:
            print("! No articles found for that keyword.")
            return None

        news_list = []
        print("\n---< Top News Headlines >---")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            news_list.append({
                "title": article["title"],
                "url": article["url"],
                "source": article["source"]["name"]
            })
        print()
        return news_list

    except requests.exceptions.RequestException as e:
        print("! Network or API error:", e)
        return None

def save_to_file(news_list, filename="news_log.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n--< News Summary >---\n")
            for i, article in enumerate(news_list, 1):
                f.write(f"\n{i}. {article['title']}\n")
                f.write(f"   Source: {article['source']}\n")
                f.write(f"   URL: {article['url']}\n")
        print(f"+ News saved to {filename}\n")
    except Exception as e:
        print("! Failed to save:", e)


def main_menu():
    while True:
        print("---| MENU |---")
        print("1. Search News by Keyword")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ").strip()

        if choice == "1":
            keyword = input(" Enter keyword (e.g. weather, sports): ").strip()
            results = get_news(keyword)
            if results:
                save = input(" Save results to file? (y/n): ").strip().lower()
                if save == "y":
                    save_to_file(results)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("! Invalid choice. Try again.\n")

if __name__ == "__main__":
    print("Welcome to the Interactive News App!")
    main_menu()


# In[ ]:




