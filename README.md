

# FastAPI Crypto Backend

This FastAPI backend serves as a simple API for retrieving information about cryptocurrencies using the Pro API provided by CoinMarketCap.

## Features

- Retrieves the top 100 cryptocurrencies.
- Allows fetching individual cryptocurrency information by ID.

## Requirements

- Python 3.x
- FastAPI
- A valid CoinMarketCap Pro API key 

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/Imranqsl212/cripto_fast-api.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up your CoinMarketCap Pro API key:
   
    - Obtain your API key from [[CoinMarketCap](https://coinmarketcap.com/) ].
    - Set your API key in project.

## Usage

1. Run the FastAPI server:

    ```
    python3 main.py
    ```

2. Open your web browser or use an API client like Postman to interact with the API.

## API Endpoints

### Get Top 100 Cryptocurrencies

- **URL:** `/cripto/`
- **Method:** `GET`
- **Description:** Retrieves the top 100 cryptocurrencies.
- **Response:** JSON object containing information about the top cryptocurrencies.

### Get Cryptocurrency by ID

- **URL:** `/cripto/{id}`
- **Method:** `GET`
- **Description:** Retrieves information about a specific cryptocurrency by its ID.
- **Parameters:**
    - `id` (int): The ID of the cryptocurrency.
- **Response:** JSON object containing information about the cryptocurrency with the specified ID.

## Example

To get information about the top 100 cryptocurrencies:

```
GET /cripto/
```

To get information about a specific cryptocurrency (e.g., with ID 1):

```
GET /cripto/1
```

## Acknowledgments

This project utilizes the CoinMarketCap Pro API to fetch cryptocurrency data. Special thanks to the CoinMarketCap team for providing this service.

---

Feel free to expand upon or customize this README to better fit your project's needs!
