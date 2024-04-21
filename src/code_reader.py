import os

class CodeReader:
    def __init__(self, filename: str):
        self.filename = filename

    def __validate_file(self, path: str):
        if not path.endswith('.nl'):
            raise Exception(f'"{self.filename}" invalid file')

        if not os.path.exists(path):
            raise Exception(f'"{self.filename}" not exists')
        
        if not os.path.isfile(path):
            raise Exception(f'"{self.filename}" is not a file')

    def read(self) -> str:
        path = os.path.abspath(self.filename)

        self.__validate_file(path)

        code: list[str] = []

        with open(path, 'r') as file:
            code = file.readlines()
            file.close()

        return code
