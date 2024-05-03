import json


class JsonHandler:
    @staticmethod
    def is_serializable_data(data: dict) -> bool:
        if type(data) is not dict:
            return False
        for key in data.keys():
            if type(key) is not str:
                return False
        return True

    def __init__(self, text: str = None, file: str = None, data: dict = None) -> None:
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

    def _parse_data(self, text) -> None:
        self._data = json.loads(text)

    def read_from_file(self, file: str=None) -> None:
        if file is None:
            raise ValueError("If not using stdinput, relative filepath must be specified")
        text = ''.join([x for x in open(file, "r")])
        self._parse_data(text)

    def read_from_input(self) -> None:
        text = ''
        inp = '_'
        while inp:
            inp = input()
            text += inp
        self._parse_data(text)

    def __str__(self) -> str:
        return json.dumps(self._data)

    def print_to_file(self, file: str) -> None:
        if type(file) is not str:
            raise ValueError("You must specify a relative file path.")
        output = open(file, "w")
        output.write(self.__str__())

    def get_dict(self) -> dict:
        return self._data

    def get_by_keys(self, params: dict) -> dict:
        for elem in self._data:
            for key in params.keys():
                if elem[key] != params[key]:
                    break
            else:
                yield elem

    def get_by_partial_keys(self, params: dict):
        for elem in self._data:
            for key in params.keys():
                if params[key] not in elem[key]:
                    break
            else:
                yield elem


if __name__ == "__main__":
    students = JsonHandler(file="students.json")
    class_value = '5a'
    club_value = 'Football'
    for student in students.get_by_keys({"Class": class_value, "Club": club_value}):
        print(student)

    print("\n" + '-'*15 + "\n")
    gender_value = 'W'
    for student in students.get_by_keys({"Gender": gender_value}):
        print(student)

    print("\n" + '-'*15 + "\n")
    name = "e"
    for student in students.get_by_partial_keys({"Name": name}):
        print(student)