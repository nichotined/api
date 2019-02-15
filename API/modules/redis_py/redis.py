import redis


class RedisHelper:
    @staticmethod
    def delete(host, port, query):
        r = None
        current_redis_value = None
        try:
            r = redis.Redis(host=str(host), port=int(port))
            current_redis_value = r.delete(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                del r
            return current_redis_value

    @staticmethod
    def get(host, port, query):
        r = None
        current_redis_value = None
        try:
            r = redis.Redis(host=str(host), port=int(port))
            current_redis_value = r.get(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                del r
            return current_redis_value

    @staticmethod
    def hvals(host, port, query):
        r = None
        hvals_list = None
        try:
            r = redis.Redis(host=str(host), port=int(port))
            hvals_list = r.hvals(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                del r
            return hvals_list

    @staticmethod
    def setex(host, port, key, query, ttl):
        r = None
        try:
            r = redis.Redis(host=str(host), port=int(port))
            r.setex(key, ttl, query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                del r
