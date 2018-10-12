##########################
## Change xml config file
##########################
from xml.etree import ElementTree as ET

file = 'file.xml'
root = 'site_config'
attr = 'timeout'
value = '15s'


tree = ET.parse(file)

for elem in tree.iter(tag=root):
  elem.find(attr).text=value

tree.write(file)
