#!/usr/bin/env python3
import xml.etree.ElementTree as ET

class XmlParse:
    def SetXmlStrings(self, xmlString):
        try:
            # if xml is able to parse or xml is valid.
            self.tree = ET.fromstring(xmlString)
            self.xmlvalid = True
        except ET.ParseError:
            # if xml is unable to parse or xml is not valid.
            self.xmlvalid = False
            





    def SearchStrings(self, substring_found):
        substring_found = []
        zera_substring = "s-zera-stor01"
        try:
            # if xml is able to parse
            self.tree = ET.fromstring(data)
            self.iteration_elements = self.tree.iter()
            for elem in self.iteration_elements:
                if zera_substring in str(elem.text):
                    substring_found.append(elem.text)
            if substring_found != []:
                return "Substring_found"
            else:
                # if xml is unable to parse
                return "substring_not_found"

        except:
            return "xml is unable to parse"


if __name__ == '__main__':
    print('valid xml ? :  ', XmlParse().SetXmlStrings("xmlvalid"))
    print('substring_found ? :  ', XmlParse().SearchStrings("substring_found"))






