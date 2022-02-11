import xml.etree.ElementTree as ET
tree = ET.parse('document.xml')
iteration_elements = tree.iter()
sunstring = "s-zera-stor01"
text_found = ""
for elem in iteration_elements:
    if sunstring in str(elem.text):
        #print(elem.text)
        text_found+= str(elem.text) + ", "
print(text_found)
if text_found == "":
    print("not found")
