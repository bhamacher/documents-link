import unittest
from document_links import xml_parse

VALIDXML = """<?xml version="1.0" encoding="UTF-8"?>
        <xmldata>
            <results>
                <binding name="id">
                    <literal>s-zera-stor01-data-test_for_xml1.pdf</literal>
                    <literal>s-zera-stor01-data-test_for_xml2.pdf</literal>
                </binding>
            </results>
        </xmldata>"""

class Test(unittest.TestCase):
    def test_valid_xml(self):
        xml_parsing = xml_parse.XmlParse()
        xml_parsing.set_xml_strings(VALIDXML)
        self.assertIs(xml_parsing.xmlvalid, True)

    def test_invalid_xml(self):
        xml_parsing = xml_parse.XmlParse()
        invalid_xml = "<"
        xml_parsing.set_xml_strings(invalid_xml)
        self.assertIs(xml_parsing.xmlvalid, False)

    def test_search_string_with_parse_not_called_yet(self):
        xml_parsing = xml_parse.XmlParse()
        search_result = xml_parsing.search_strings('foo')
        self.assertIs(search_result, None)

    def test_search_string_with_parse_called_invalid(self):
        xml_parsing = xml_parse.XmlParse()
        invalid_xml = "<"
        xml_parsing.set_xml_strings(invalid_xml)
        search_result = xml_parsing.search_strings('foo')
        self.assertIs(search_result, None)

    def test_search_string_with_parse_called_valid_not_found(self):
        xml_parsing = xml_parse.XmlParse()
        xml_parsing.set_xml_strings(VALIDXML)
        search_result = xml_parsing.search_strings('foo')
        self.assertIs(len(search_result), 0)

    def test_search_string_with_parse_called_valid_found(self):
        xml_parsing = xml_parse.XmlParse()
        xml_parsing.set_xml_strings(VALIDXML)
        search_result = xml_parsing.search_strings('s-zera-stor01')
        self.assertIs(len(search_result), 2)

    def test_search_string_with_parse_called_valid_content_found(self):
        xml_parsing = xml_parse.XmlParse()
        xml_parsing.set_xml_strings(VALIDXML)
        search_result = xml_parsing.search_strings('s-zera-stor01')
        self.assertEqual(search_result[0].text, "s-zera-stor01-data-test_for_xml1.pdf")
        self.assertEqual(search_result[1].text, "s-zera-stor01-data-test_for_xml2.pdf")

if __name__ == '__main__':
    unittest.main(verbosity=2)
