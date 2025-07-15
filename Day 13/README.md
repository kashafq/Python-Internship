# API Data Fetcher & Exchange Rate Analyzer

## Overview
This Python script fetches real-time exchange rate data from a free public API and generates a text report of selected currency rates.

## API Used
- **Exchange Rate API**
- URL: https://api.exchangerate-api.com/v4/latest/USD
- No API key or authentication required

## Technologies Used
- `requests` for HTTP API communication
- JSON parsing using `.json()`
- Functions, conditionals, error handling

## Features
- Fetch exchange rates from a public API
- Supports custom API URLs
- Optional currency filter (e.g., only show "EUR", "INR", etc.)
- Saves output to `exchange_rate_report.txt`

