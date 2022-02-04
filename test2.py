import xml.etree.ElementTree as ET
tree = ET.parse('/home/d.kumar/Desktop/python_test/word-doc-extract/word/document.xml')
iteration_elements = tree.iter()
substring = "s-zera-stor01"
text_found = ""
for elem in iteration_elements:
    if substring in str(elem.text):
        #print(elem.text)
        text_found+= str(elem.text) + ", "
print(text_found)
if text_found == "":
    print("not found")