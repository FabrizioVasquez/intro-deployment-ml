# Aqui van a ir la caracteristicas necesarias para la prediccion y el target "worldwide_gross" que vamos a devolver

from pydantic import BaseModel # Esto es para serializar los json que van entrando y saliendo de nuestro modelo

class PredictionRequest(BaseModel):
    opening_gross: float
    screens: float
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int 
    cast_total_facebook_likes: float
    budget: float
    imdb_score: float


class PredictionResponse(BaseModel):
    worldwide_gross: float
    
