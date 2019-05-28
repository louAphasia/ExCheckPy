import xml.etree.ElementTree as ET

tree=ET.parse('plik.xml')
root=tree.getroot()
#root=ET.fromstring(plik_as_string)

print(len(root[0]))