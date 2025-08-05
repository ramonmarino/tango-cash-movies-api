from fastapi import HTTPException
from app.repositories.movie_repo import MovieRepository


class MovieService:
    def __init__(self):
        self.movie_repo = MovieRepository()

    async def get_all_movies(self):
        movies = await self.movie_repo.get_all_movies()
        return movies or []


    async def get_movie_by_id(self, movie_id: int):
        movie = await self.movie_repo.get_movie_by_id(movie_id)
        if movie is None:
            return None
        return movie

    async def add_movie(self, movie_name: str):
        return await self.movie_repo.add_movie(movie_name)

    async def update_movie(self, movie_id: int, new_name: str):
        updated = await self.movie_repo.update_movie(movie_id, new_name)
        return updated

    async def delete_movie(self, movie_id: int):
        deleted = await self.movie_repo.delete_movie(movie_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie deleted successfully"}