from fastapi import APIRouter
from init import client

router = APIRouter(prefix="/cripto",tags=['crypto'])


@router.get("/")
async def get_crypto():
    return await client.get_listings()


@router.get("/{id}")
async def get_crypto_by_id(id: int):
    return await client.get_currency(id)
