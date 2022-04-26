import xml.etree.ElementTree as ET

class XmlParse:
    def set_xml_strings(self, xml_string):
        try:
            self.tree = ET.fromstring(xml_string)
            self.xmlvalid = True
        except ET.ParseError:
            self.xmlvalid = False

    def search_strings(self, substring):
        substring_found = []
        if not self.xmlvalid:
            return None
        try:
            self.iteration_elements = self.tree.iter()
            for elem in self.iteration_elements:
                if substring in str(elem.text):
                    substring_found.append(elem)
        except ET.ParseError:
            pass
        return substring_found

    def __init__(self) -> None:
        self.xmlvalid = False
        self.tree = None
        self.iteration_elements = None
