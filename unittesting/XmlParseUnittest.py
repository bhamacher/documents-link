import unittest
from modules import XmlParse

class Test(unittest.TestCase):
    def test_validXml(self):
        xmlparse = XmlParse.XmlParse()
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
    

if __name__ == '__main__':
    unittest.main()
