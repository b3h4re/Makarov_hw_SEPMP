import json


class JsonHandler:
    @staticmethod
    def is_serializable_data(data: dict):
        if type(data) is not dict:
            return False
        for key in data.keys():
            if type(key) is not str:
                return False
        return True

    def __init__(self, text: str = None, file: str = None, data: dict = None):
        self._data = json.loads('{}')
        if text is not None:
            self._parse_data(text)
        elif file is not None:
            self.read_from_file(file=file)
        elif data is not None:
            if self.is_serializable_data(data):
                self._data = data
            else:
                raise ValueError("Input data is not serializable.")

    def _parse_data(self, text):
        self._data = json.loads(text)

    def read_from_file(self, file=None):
        if file is None:
            raise ValueError("If not using stdinput, relative filepath must be specified")
        text = ''.join([x for x in open(file, "r")])
        self._parse_data(text)

    def read_from_input(self):
        text = ''
        inp = '_'
        while inp:
            inp = input()
            text += inp
        self._parse_data(text)

    def __str__(self):
        return json.dumps(self._data)

    def print_to_file(self, file):
        if type(file) is not str:
            raise ValueError("You must specify a relative file path.")
        output = open(file, "w")
        output.write(self.__str__())

    def get_dict(self):
        return self._data


if __name__ == "__main__":
    data = JsonHandler()
    data.read_from_input()
    data.print_to_file(file="data_file.json")
    data.read_from_file(file="data_file.json")
    res = data.get_dict()
    print(res)