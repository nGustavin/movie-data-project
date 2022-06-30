from movie_data_project.controllers.provider_controller import DataProviderController
from movie_data_project.controllers.validation_controller import DataValidationController

if __name__=='__main__':
  api = DataProviderController()
  data_df = api.get_popular_movies()
  
  data_df.loc[16:29, 'backdrop_path'] = 'invalid_path'
  
  validation_class = DataValidationController(data_df)
  result = validation_class.validate_file_path('backdrop_path', regex=False,extensions=['.jpg'])
  
  failures = result['failure']
  successes = result['success']
  
  print(failures['length'], successes['length'])