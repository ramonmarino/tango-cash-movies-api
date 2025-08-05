from app.services.services_movies import MovieService
from app.dtos.movie_dto import MovieDto

movie_service = MovieService()

async def get_all_movies():
    return await movie_service.get_all_movies()

async def get_movie_by_id(movie_id: int):
    return await movie_service.get_movie_by_id(movie_id)

async def add_movie(movie: MovieDto):
    return await movie_service.add_movie(movie.movie_name)

async def update_movie(movie_id: int, movie: MovieDto):
    return await movie_service.update_movie(movie_id, movie.movie_name)

async def delete_movie(movie_id: int):
    return await movie_service.delete_movie(movie_id)
    