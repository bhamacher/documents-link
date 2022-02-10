#!/usr/bin/env python3
import unittest
from ..modules import XmlParse as XmlParseClass

class Test(unittest.TestCase):
    def test_validXml(self):
        xmlparse = XmlParseClass.XmlParse()
        data = """<?xml version="1.0" encoding="UTF-8"?>
                <xmldata>
                    <results>
                        <binding name="id">
                            <literal>s-zera-stor01-data-test_for_xml1.pdf</literal>
                            <literal>s-zera-stor01-data-test_for_xml2.pdf</literal>
                        </binding>
                    </results>
                </xmldata>"""
        xmlparse.SetXmlStrings(data)
        self.assertIs(xmlparse.xmlvalid, True)
    def test_invalidXml(self):
        xmlparse = XmlParseClass.XmlParse()
        xmlparse.SetXmlStrings('foo')
        self.assertIs(xmlparse.xmlvalid, False)


    def test_SetXmlStrings(self):
        xml_validation = self.xmlparse.SetXmlStrings("xmlvalid")
        self.assertIs(xml_validation, "Valid_xml")


    def test_SearchStrings(self):
        xml_substrings = self.xmlparse.SearchStrings("substring_found")
        self.assertIs(xml_substrings, "Substring_found")
    

if __name__ == '__main__':
    unittest.main(verbosity=2)

