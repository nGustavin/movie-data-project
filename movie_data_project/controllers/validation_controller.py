from movie_data_project.services.fetch_api_service import get_now_playing_movies_list
import pandas as pd

class DataValidationController(object):
  def __init__(self, dataframe,*args, **kwargs):
    self.df = dataframe
  def validate_file_path(self, column, regex: bool = False, extensions: list | str = None):
    """
    Validate the pattern of a file path in a Pandas Dataframe.

    Valid pattern example: /my_file.csv
    Invalid pattern example: my_file
    """
    series = self.df[column]

    metadata = {
      "failure": {
        "items": [],
        "length": 0
      },
      "success": {
        "items": [],
        "length": 0
      }
    }
    
    if type(extensions) == list:
      for ext in extensions:
        for item in series:
          if item.endswith(ext):
            metadata['success']['items'].append(item)
            metadata['success']['length'] += 1
          else:
            metadata['failure']['items'].append(item)
            metadata['failure']['length'] += 1
    elif type(extensions) == str:
      for item in series:
        if item.endswith(extensions):
            metadata['success']['items'].append(item)
            metadata['success']['length'] += 1
        else:
            metadata['failure']['items'].append(item)
            metadata['failure']['length'] += 1
    
    return metadata
  


# api = DataValidationController()