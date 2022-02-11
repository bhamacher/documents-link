import xml.etree.ElementTree as ET

class XmlParse:
    def SetXmlStrings(self, xmlString):
        try:
            self.tree = ET.fromstring(xmlString)
            self.xmlvalid = True
        except ET.ParseError:
            self.xmlvalid = False
            
    def SearchStrings(self, substring):
        substring_found = []
        if not self.xmlvalid:
            return None
        try:
            self.iteration_elements = self.tree.iter()
            for elem in self.iteration_elements:
                if substring in str(elem.text):
                    substring_found.append(elem)
        except:
            pass
        return substring_found

    def __init__(self) -> None:
        self.xmlvalid = False
        self.tree = None