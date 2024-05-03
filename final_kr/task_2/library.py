import xml.etree.ElementTree as ET


class XMLHandler:

    def read_from_string(self, xml_str: str) -> None:
        self._root = ET.fromstring(xml_str)

    def read_from_file(self, file: str = '') -> None:
        if file == '':
            raise ValueError("If not using stdinput, relative filepath must be specified")
        text = ''.join([x for x in open(file, "r")])
        self.read_from_string(text)

    def read_from_input(self) -> None:
        text = ''
        inp = '_'
        while inp:
            inp = input()
            text += inp
        self.read_from_string(text)

    def __init__(self, xml_str: str = None, file: str = None) -> None:
        self._root = None
        if xml_str is not None:
            self.read_from_string(xml_str)
        if file is not None:
            self.read_from_file(file=file)

    def get_by_keys(self, params: dict):
        keys = set(params.keys())
        for elem in self._root:
            for child in elem:
                if child.tag in keys:
                    if child.text != params[child.tag]:
                        break
            else:
                yield elem

    def get_by_partial_key(self, params: dict):
        keys = set(params.keys())
        for elem in self._root:
            for child in elem:
                if child.tag in keys:
                    if params[child.tag] not in child.text:
                        break
            else:
                yield elem


if __name__ == "__main__":
    library = XMLHandler(file="library.xml")
    books = list(library.get_by_keys({"genre": 'Fantasy'}))
    for book in books:
        print(book.attrib['id'])

    print("\n" + '-' * 15 + "\n")

    books = list(library.get_by_partial_key({"author": 'a'}))
    for book in books:
        print(book.attrib['id'])