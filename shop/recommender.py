from django.conf import settings
import redis

# connect to redis
r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)


class Recommender(object):

    def get_product_key(self,id):
        return "product {} purshased with".format(id)

    # def get_product_bought(self, products):
