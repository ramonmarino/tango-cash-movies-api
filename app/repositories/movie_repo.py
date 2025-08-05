from app.db.database import database
from app.models.movie_model import movies  

class MovieRepository:
    async def get_all_movies(self):
        query = movies.select()
        return await database.fetch_all(query)

    async def get_movie_by_id(self, movie_id: int):
        query = movies.select().where(movies.c.id == movie_id)
        return await database.fetch_one(query)

    async def add_movie(self, movie_name: str):
        query = movies.insert().values(movie_name=movie_name)
        movie_id = await database.execute(query)
        return {"id": movie_id, "movie_name": movie_name}

    async def update_movie(self, movie_id: int, new_name: str):
        query = movies.update().where(movies.c.id == movie_id).values(movie_name=new_name)
        result = await database.execute(query)
        return result > 0

    async def delete_movie(self, movie_id: int):
        query = movies.delete().where(movies.c.id == movie_id)
        result = await database.execute(query)
        return result > 0