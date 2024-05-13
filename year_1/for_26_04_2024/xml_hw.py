import xml.etree.ElementTree as ET


class XMLHandler:

    def read_from_string(self, xml_str):
        self._root = ET.fromstring(xml_str)

    def read_from_file(self, file=None):
        if file is None:
            raise ValueError("If not using stdinput, relative filepath must be specified")
        text = ''.join([x for x in open(file, "r")])
        self.read_from_string(text)

    def read_from_input(self):
        text = ''
        inp = '_'
        while inp:
            inp = input()
            text += inp
        self.read_from_string(text)

    def __init__(self, xml_str: str = None, file: str = None):
        self._root = None
        if xml_str is not None:
            self.read_from_string(xml_str)
        if file is not None:
            self.read_from_file(file=file)

    def count(self, key):
        res = 0
        for child in self._root:
            if child.tag == key:
                res += 1
        return res

    def sort(self, key, reverse=False, f=(lambda x: x)):
        to_sort = []
        for child in self._root:
            elem = [child.attrib['id']]

            for appt in child:
                if appt.tag == key:
                    elem.append(appt.text)
            to_sort.append(tuple(elem))
        to_sort.sort(reverse=reverse, key=f)
        print(to_sort)
        # for book_id, elem in to_sort:
        #     print(self._root[book_id])


if __name__ == "__main__":
    xml = XMLHandler(file="input.xml")
    print(xml.count("book"))
    xml.sort("price", reverse=False, f=(lambda x: float(x[1])))
