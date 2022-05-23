# [
# {
#     "model": "movies.movie",
#     "pk": 1,
#     "fields": {
#         "title": "Act why team bag tell over smile themselves.",
#         "overview": "Once feeling according. Follow several Republican best about accept.\nAgency play what report. Know sound shoulder small.",
#         "release_date": "1978-01-22T12:48:49Z",
#         "poster_path": "New fish right agreement night. Create name yet smile pay west.\nEvent cause method exist detail new. Fire stand happen focus allow eye.",
#         "actors": [
#             6
#         ]
#     }
# },
# {
#     "model": "movies.movie",
#     "pk": 2,
#     "fields": {
#         "title": "Mean everybody treatment.",
#         "overview": "Majority factor break treatment sense. Republican community green gun generation care.\nFly under travel couple small foot see. Manage wish court ground.",
#         "release_date": "2013-09-19T00:06:55Z",
#         "poster_path": "Throw identify ball born. He with wide future.\nLearn training child. Hundred off tree benefit none. Instead it hot tend focus.",
#         "actors": [
#             6,
#             9
#         ]
#     }
# },
import requests
from pprint import pprint

movies=[]
genre_dict={28:1, 12:2, 16:3, 35:4, 80:5, 99:6, 18:7, 10751:8, 14:9, 36:10, 27:11, 10402:12, 9648:13, 10749:14, 878:15, 10770:16, 53:17, 10752:18, 37:19}
pk=1
for i in range(1,2):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '9e1354871190e85ce319d2dba94128d7',
        'language':'ko',
        'page': i
    }

    response = requests.get(BASE_URL+path, params=params) # 영화를 불러와서

    data = response.json()

    for item in data['results']:
        if item['vote_average']>7.5 and item['vote_count']>2000:
            tmp=dict()
            fields=dict()
            tmp['model'] = 'movies.movie'
            tmp['pk'] = pk
            pk+=1
            fields['backdrop_path'] = item['backdrop_path']
            fields['poster_path'] = item['poster_path']
            fields['genre_ids'] = []
            for num in item['genre_ids']:
                fields['genre_ids'].append(genre_dict[num])
            fields['overview'] = item['overview']
            fields['title'] = item['title']
            fields['release_date'] = item['release_date']
            tmp['fields'] = fields
            movies.append(tmp)

import json

with open('movies.json', 'w', encoding='utf-8') as make_file:
    json.dump(movies, make_file, ensure_ascii=False, indent="\t")