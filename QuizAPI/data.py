import requests

parameters = {'amount': 10,
              'type': 'boolean',
              'category': 18
              }
request = requests.get('https://opentdb.com/api.php', params=parameters)

question_data = request.json()['results']
