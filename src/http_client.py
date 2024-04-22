from aiohttp import ClientSession
from fastapi import HTTPException



class HTTPClient:
    def __init__(self, base_url: str, api: str):
        self.base_url = base_url
        self.api = api
        self.headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": api,
        }

    async def get(self, endpoint: str, params=None):
        async with ClientSession(headers=self.headers) as session:
            async with session.get(self.base_url + endpoint, params=params) as response:
                if response.status != 200:
                    raise HTTPException(status_code=response.status, detail="HTTP Error")
                return await response.json()


class CMCHTTPClient(HTTPClient):
    async def get_listings(self):
        return await self.get("/v1/cryptocurrency/listings/latest")

    async def get_currency(self, id: int):
        return await self.get("/v2/cryptocurrency/quotes/latest", params={"id": id})