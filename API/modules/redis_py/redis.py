import redis


class RedisHelper:
    @staticmethod
    def delete(host, port, query):
        r = None
        try:
            r = redis.Redis(host=str(host), port=int(port))
            r.delete(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(str(host), int(port)))

    @staticmethod
    def get(host, port, query):
        r = None
        current_redis_value = "0"
        try:
            r = redis.Redis(host=str(host), port=int(port))
            current_redis_value = r.get(query)
        except Exception as e:
            raise e
        finally:
            if r is not None:
                r.client_kill("{0}:{1}".format(str(host), int(port)))
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
                r.client_kill("{0}:{1}".format(str(host), int(port)))
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
                r.client_kill("{0}:{1}".format(str(host), int(port)))
