#!/usr/bin/env python3
import unittest
import sys, os
sys.path.insert(1, "/home/d.kumar/data/gitproject/zera/documents-link/")
from modules import XmlParse as XmlParseClass

class Test(unittest.TestCase):
    xmlparse = XmlParseClass.XmlParse()
    def test_SetXmlStrings(self):
        xml_validation = self.xmlparse.SetXmlStrings("xmlvalid")
        self.assertIs(xml_validation, "Valid_xml")


    def test_SearchStrings(self):
        xml_substrings = self.xmlparse.SearchStrings("substring_found")
        self.assertIs(xml_substrings, "Substring_found")
    

if __name__ == '__main__':
    unittest.main(verbosity=2)
