import os
import base64
import json

class Cache:
    def __init__(self, filename: str):
        self.path = os.path.abspath(filename)
        self.cache = self.__init_cache(self.path)

    def __validate_cache(self, cache: bytes):
        try:
            cache_as_string = base64.b64decode(cache.decode('utf-8'), validate=True)
            cache: dict = json.loads(cache_as_string)

            keys = list(cache.keys())

            for key in keys:
                if len(key) != 64:
                    return False

                if type(cache[key]) != str:
                    return False
        except Exception as e:
            return False

        return True
        
    def __read(self, path: str) -> bytes:
        with open(path, 'rb') as file:
            return file.read()

    def __write(self, path: str, cache: dict):
        with open(path, 'wb') as file:
            cache_as_string = json.dumps(cache)
            cache_encoded = cache_as_string.encode('utf-8')
            b64 = base64.b64encode(cache_encoded)
            file.write(b64)
            file.close()

    def __init_cache(self, path: str):
        if os.path.exists(path):
            cache = self.__read(path)

            if not self.__validate_cache(cache):
                self.__write(path, {})

                return {}
            
            decoded_cache = cache.decode('utf-8')
            decrypted_cache = base64.b64decode(decoded_cache).decode('utf-8')
            dicted_cache = json.loads(decrypted_cache)

            return dicted_cache

        self.__write(path, {})

        return {}

    def get(self, seed: str) -> str | None:
        if seed in self.cache:
            return self.cache[seed]

        return None

    def add(self, seed: str, value: str):
        self.cache[seed] = value

        self.__write(self.path, self.cache)
