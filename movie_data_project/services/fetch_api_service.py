import requests

def get_now_playing_movies_list(token):
    base_url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(base_url, headers=headers)
    
    movie_list = []

    counter = 1
    
    while counter <= 5:
        new_url = f'https://api.themoviedb.org/3/movie/popular?language=en-US&page={counter}'
        response = requests.get(base_url, headers=headers)
        if response.status_code in [200, 201]:
            for movie in response.json()['results']:
                    movie_list.append(movie)
        counter += 1
        
    return movie_list
