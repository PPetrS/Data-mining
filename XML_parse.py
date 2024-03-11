import xml.etree.ElementTree as ET
import csv

# Open xml file
tree = ET.parse('nazev_xml_souboru.xml')
root = tree.getroot()
