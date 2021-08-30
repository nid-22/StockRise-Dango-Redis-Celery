docker build -t "cfe-redis" .
docker run -it --rm -p 6379:6379 "cfe-redis"
#to check if redis is working
#in mac/linus u just have to do redis cli ping
# in windows
'''
>>> import redis
>>> r = redis.Redis(host='localhost',port=6379, db=0) 
>>> settr=r.set('foo','bar')
>>> gettr = r.get('foo')
>>> print(settr,gettr)

'''