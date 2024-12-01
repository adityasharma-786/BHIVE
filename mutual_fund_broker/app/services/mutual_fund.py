import httpx
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
BASE_URL = 'https://latest-mutual-fund-nav.p.rapidapi.com'


async def get_open_ended_schemes(current_user: str = None):
    url = f'{BASE_URL}/latest?Scheme_Type=Open'
    headers = {
        'x-rapidapi-host': 'latest-mutual-fund-nav.p.rapidapi.com',
        'x-rapidapi-key': RAPIDAPI_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # This will return the mutual fund data
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from RapidAPI")
