from fastapi import APIRouter, HTTPException
from app.dtos.movie_dto import MovieDto
from app.controllers import movie_controller

router = APIRouter()

@router.get("/")
async def get_movies():
    return {"movies": await movie_controller.get_all_movies()}

@router.post("/")
async def add_movies(movie: MovieDto):
    return {"added": await movie_controller.add_movie(movie)}

@router.get("/{movie_id}")
async def get_movie_by_id(movie_id: int):
    movie = await movie_controller.get_movie_by_id(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"movie": movie}

@router.put("/{movie_id}")
async def update_movie(movie_id: int, movie: MovieDto):
    updated = await movie_controller.update_movie(movie_id, movie)
    if not updated:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie updated successfully"}

@router.delete("/{movie_id}")
async def delete_movie(movie_id: int):
    return await movie_controller.delete_movie(movie_id)
