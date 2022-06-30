import unittest
from movie_data_project.controllers.provider_controller import DataProviderController
from movie_data_project.controllers.validation_controller import DataValidationController

class TestDataValidationController(unittest.TestCase):
    
    api = DataProviderController()
    data_df = api.get_popular_movies()
    dataframe = data_df[:100]
    
    
    def test_file_test_validation_should_return_failures(self):
        self.dataframe.loc[1:10, 'backdrop_path'] = 'invalid_path'
        validation_class = DataValidationController(self.dataframe)
        result = validation_class.validate_file_path('backdrop_path', regex=False,extensions=['.jpg'])
        failures = result['failure']
        self.assertEqual(failures['length'], 10)
        
        
    def test_file_test_validation_should_return_succeses(self):
        self.dataframe.loc[1:10, 'backdrop_path'] = 'invalid_path'
        validation_class = DataValidationController(self.dataframe)
        result = validation_class.validate_file_path('backdrop_path', regex=False,extensions=['.jpg'])
        successes = result['success']
        self.assertEqual(successes['length'], 90)

if __name__ == '__main__':
    unittest.main()