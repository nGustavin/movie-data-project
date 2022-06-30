import os
from movie_data_project.services.fetch_api_service import get_now_playing_movies_list
from pandas import DataFrame

class DataProviderController():
  def __init__(self, *args, **kwargs):
    self.API_TOKEN = os.environ['API_TOKEN']
  
  def get_popular_movies(self) -> DataFrame:
    """Returns a list of movies in a panda DataFrame"""
    movie_list = get_now_playing_movies_list(self.API_TOKEN)
    df = DataFrame(movie_list)

    return df

# api = DataValidationController()