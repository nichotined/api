import redis


class RedisHelper:
    @staticmethod
    def delete(host, port, query):
        r = None
        try:
            r = redis.Redis(host=host, port=port)
            r.delete(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(host, port))

    @staticmethod
    def get(host, port, query):
        r = None
        current_redis_value = "0"
        try:
            r = redis.Redis(host=host, port=port)
            current_redis_value = r.get(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(host, port))
            return current_redis_value

    @staticmethod
    def hvals(host, port, query):
        r = None
        hvals_list = None
        try:
            r = redis.Redis(host=host, port=port)
            hvals_list = r.hvals(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(host, port))
            return hvals_list

    @staticmethod
    def setex(host, port, key, query, ttl):
        r = None
        try:
            r = redis.Redis(host=host, port=port)
            r.setex(key, ttl, query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(host, port))
