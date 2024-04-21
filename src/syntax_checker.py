class SyntaxChecker:
    def __init__(self, code: list[str], max_line_length=80):
        self.code = code
        self.max_line_length = max_line_length

    def check_syntax(self):
        errors: list[str] = []

        if len(self.code) == 0:
            errors.append('file is empty')

        first_line = self.code[0]
        last_line = self.code[-1]

        if first_line != '\n':
            errors.append('missing "\\n" on first line')

        if last_line != '\n' and not last_line.endswith('\n'):
            errors.append('missing "\\n" on last line')

        for index, line in enumerate(self.code):
            line_number = index + 1
            line = line.rstrip()

            if len(line.strip()) > self.max_line_length:
                errors.append(f'line {line_number} is too long. Max of {self.max_line_length}')

            tabs = line.replace(line.lstrip(), '')

            if len(tabs) % 4 != 0:
                errors.append(f'invalid identation on line {line_number}')

        for error in errors:
            print(f'[!] {error}')
        
        if len(errors) > 0:
            exit(1)
