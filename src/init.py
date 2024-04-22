from http_client import CMCHTTPClient
from config import settings


client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com", api=settings.CMC_API_KEY
)