from fastapi import FastAPI
from app.router import movie_routes
from app.db.database import database

app = FastAPI(
    title= "Tango and Cash: Your Movies, Your Bullets"
)

app.include_router(movie_routes.router, prefix= "/movies", tags=["movies"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


    