from pydantic import BaseModel, field_validator, Field


class MovieDto(BaseModel):
    movie_name: str = Field(...,min_length = 1, max_length= 100)
    
    @field_validator("movie_name")
    def no_special_chars(cls, v):
        v = v.strip()
        if not v.replace(" ", "").isalnum():
            raise ValueError("Invalid movie name: only letters, numbers, and spaces are allowed")
        return v
    
    class Config:
        anystr_strip_whitespace = True
            
        