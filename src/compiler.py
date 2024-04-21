from random import randint
from hashlib import sha256
from instructions import INSTRUCTIONS
from cache import Cache
import openai

class Compiler:
    def __init__(self, code: str): 
        self.code = code
        self.ai = openai.OpenAI()
        self.cache = Cache('cache.json')

    def __seed(self):
        return sha256(self.code.encode('utf-8')).hexdigest()

    def __extract(self, code: str) -> str:
        lines = code.splitlines(keepends=True)

        return ''.join(lines[1:-1])

    def compile(self):
        seed = self.__seed()

        cache = self.cache.get(seed)

        if cache is not None:
            return compile(cache, "<string>", "exec")

        response = self.ai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[{
                'role': 'system',
                'content': INSTRUCTIONS
            }, {
                'role': 'system',
                'content': self.code
            }]
        )

        code = response.choices[0].message.content
        code = self.__extract(code)

        self.cache.add(seed, code)
        
        return compile(code, "<string>", "exec")
