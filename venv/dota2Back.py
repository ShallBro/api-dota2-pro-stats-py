# controllers/dota2back.py
from database import connect_db, Heroes
from sqlalchemy.orm import Session
import httpx
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
# from typing import List
# from pydantic import BaseModel, Field


app = FastAPI(
    title="Dota2Stats app"
)


@app.get("/search")
async def get_search(q: str):
    api_url = "https://api.opendota.com/api/search?q=" + q
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, timeout=httpx.Timeout(timeout=20.0))
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "error": "Ошибка при выполнения запроса"}


@app.get("/players/{account_id}/matches")
async def get_matches(account_id: int):
    my_str = str(account_id)
    api_url = "https://api.opendota.com/api/players/" + my_str + "/matches"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, timeout=httpx.Timeout(timeout=20.0))
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "error": "Ошибка при выполнения запроса"}


@app.get("/players/{account_id}/peers")
async def get_peers(account_id: int):
    my_str = str(account_id)
    api_url = "https://api.opendota.com/api/players/" + my_str + "/peers"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url, timeout=httpx.Timeout(timeout=20.0))
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "error": "Ошибка при выполнения запроса"}


@app.get("/players/{account_id}/heroes")
async def get_heroes(account_id: int):
    my_str = str(account_id)
    api_url = "https://api.opendota.com/api/players/" + my_str + "/heroes"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "error": "Ошибка при выполнения запроса"}


@app.get("/matches/{match_id}")
async def get_matches_id(match_id: int):
    my_str = str(match_id)
    api_url = "https://api.opendota.com/api/matches/" + my_str
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": response.status_code, "error": "Ошибка при выполнения запроса"}


@app.get("/image/{id}")
def get_image(id: int, db: Session = Depends(connect_db)):
    hero = db.query(Heroes).filter(Heroes.id == id).first()
    if hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    response = RedirectResponse(url=hero.images)
    return response
