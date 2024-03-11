import xml.etree.ElementTree as ET
import csv

# Open xml file
tree = ET.parse('nazev_xml_souboru.xml')
root = tree.getroot()

# Open CSV file to write
with open('vystupni_csv_soubor.csv', 'w', newline='', encoding='utf-8') as csvfile:
# Vytvoření objektu pro zápis do CSV
csvwriter = csv.writer(csvfile)
