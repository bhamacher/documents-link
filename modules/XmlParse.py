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
            



if __name__ == '__main__':
    print('valid xml ? :  ', XmlParse().SetXmlStrings("xmlvalid"))
    print('substring_found ? :  ', XmlParse().SearchStrings("substring_found"))






