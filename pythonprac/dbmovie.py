from pymongo import MongoClient
client = MongoClient('mongodb+srv://youngseok:dhdudtjr11!@cluster0.jactwgi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# movie = db.movies.find_one({'title':'가버나움'})
# star = movie['star']
#
# all_movies = list(db.movies.find({'star': star},{'_id' : False}))
# for m in all_movies:
#     print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})



















# print(movie1)
# movie_star = (movie['star'])
# all_movie = list(db.movies.find({},{'_id':False}))
# for m in all_movie:
#     if movie == m[2]:
#         print(m[0])


# all_movie1 = (list(m['star'] for m in all_movie))
#
# for all_movie_star in all_movie1:
#     if movie_star == all_movie_star:
#         print(all_movie_star)

# 3번째 값과 지금 구해진값이 같다면?
#  제목 추출 이를 위해선