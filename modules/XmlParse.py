#!/usr/bin/env python3
import xml.etree.ElementTree as ET
data = """<?xml version="1.0" encoding="UTF-8"?>
<xmldata>
	<results>
		<binding name="id">
			<literal>s-zera-stor01-data-test_for_xml1.pdf</literal>
            <literal>s-zera-stor01-data-test_for_xml2.pdf</literal>
		</binding>
	</results>
</xmldata>"""

class XmlParse:
    def SetXmlStrings(self, xmlvalid):
        try:
            # if xml is able to parse or xml is valid.
            self.tree = ET.fromstring(data)
            xmlvalid = self.tree
            return "Valid_xml"
            
        except ET.ParseError:
            # if xml is unable to parse or xml is not valid.
            return "Not_valid_xml"
            


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






