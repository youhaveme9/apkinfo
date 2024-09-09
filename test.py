import xml.etree.ElementTree as ET

xml = ET.parse('AndroidManifest.xml')
root = xml.getroot()
if root.tag != 'manifest':
    exit(1)