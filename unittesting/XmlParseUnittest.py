import unittest
from modules import XmlParse

validXml = """<?xml version="1.0" encoding="UTF-8"?>
        <xmldata>
            <results>
                <binding name="id">
                    <literal>s-zera-stor01-data-test_for_xml1.pdf</literal>
                    <literal>s-zera-stor01-data-test_for_xml2.pdf</literal>
                </binding>
            </results>
        </xmldata>"""

class Test(unittest.TestCase):
    def test_validXml(self):
        xmlparse = XmlParse.XmlParse()
        xmlparse.SetXmlStrings(validXml)
        self.assertIs(xmlparse.xmlvalid, True)

    def test_invalidXml(self):
        xmlparse = XmlParse.XmlParse()
        invalidXml = "<"
        xmlparse.SetXmlStrings(invalidXml)
        self.assertIs(xmlparse.xmlvalid, False)

    def test_searchStringWithParseNotCalledYet(self):
        xmlparse = XmlParse.XmlParse()
        searchResult = xmlparse.SearchStrings('foo')
        self.assertIs(searchResult, None)

    def test_searchStringWithParseCalledInvalid(self):
        xmlparse = XmlParse.XmlParse()
        invalidXml = "<"
        xmlparse.SetXmlStrings(invalidXml)
        searchResult = xmlparse.SearchStrings('foo')
        self.assertIs(searchResult, None)

    def test_searchStringWithParseCalledValidNotFound(self):
        xmlparse = XmlParse.XmlParse()
        xmlparse.SetXmlStrings(validXml)
        searchResult = xmlparse.SearchStrings('foo')
        self.assertIs(len(searchResult), 0)

    def test_searchStringWithParseCalledValidFound(self):
        xmlparse = XmlParse.XmlParse()
        xmlparse.SetXmlStrings(validXml)
        searchResult = xmlparse.SearchStrings('s-zera-stor01')
        self.assertIs(len(searchResult), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
