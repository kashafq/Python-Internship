# Interactive News CLI App – NewsAPI

## 📌 About
This is a command-line Python application that fetches real-time news headlines based on any keyword you enter (e.g. "weather", "Pakistan", "sports"). It uses the [NewsAPI](https://newsapi.org/) to retrieve data.

## 🔧 Features
- Search news articles by any keyword
- Displays top 5 headlines with source and URL
- Simple CLI menu system
- Error handling for failed API requests or empty results
- Option to save results to a `.txt` file

## 🚀 How to Run
1. Clone this repo
2. Install `requests` module if needed:
   ```bash
   pip install requests
   pip install requests
4. Get a free API key from  [https://newsapi.org]
5. Open `interactive_api.py` and paste your API key like this:
```python
   API_KEY = "your_actual_key_here"
5. Run the script:
python interactive_api.py