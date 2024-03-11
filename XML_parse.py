import xml.etree.ElementTree as ET
import csv

# Definice jmenného prostoru
namespace = {'ns': 'http://seznam.gov.cz/ovm/datafile/seznam_ds/v1'}

# Open xml file
tree = ET.parse('nazev_xml_souboru.xml')
root = tree.getroot()

# Open CSV file to write
with open('vystupni_csv_soubor.csv', 'w', newline='', encoding='utf-8') as csvfile:
# Vytvoření objektu pro zápis do CSV
csvwriter = csv.writer(csvfile)

# Writing CSV file header
csvwriter.writerow(['id', 'type', 'subtype', 'firstName', 'lastName', 'tradeName', 'ico', 'city', 
                        'district', 'street', 'cp', 'co', 'zip', 'addressPoint', 'state', 'pdz', 'ovm', 'isMaster', 'idOVM'])

# Browsing box elements in XML file
    for box in root.findall('.//ns:box', namespaces=namespace):
        id = box.find('ns:id', namespaces=namespace).text
        type = box.find('ns:type', namespaces=namespace).text
        subtype = box.find('ns:subtype', namespaces=namespace).text
        firstName = box.find('.//ns:firstName', namespaces=namespace).text if box.find('.//ns:firstName', namespaces=namespace) is not None else ""
        lastName = box.find('.//ns:lastName', namespaces=namespace).text if box.find('.//ns:lastName', namespaces=namespace) is not None else ""
        tradeName = box.find('ns:tradeName', namespaces=namespace).text if box.find('ns:tradeName', namespaces=namespace) is not None else ""
        ico = box.find('ns:ico', namespaces=namespace).text
        city = box.find('.//ns:city', namespaces=namespace).text if box.find('.//ns:city', namespaces=namespace) is not None else ""
        district = box.find('.//ns:district', namespaces=namespace).text if box.find('.//ns:district', namespaces=namespace) is not None else ""
        street = box.find('.//ns:street', namespaces=namespace).text if box.find('.//ns:street', namespaces=namespace) is not None else ""
        cp = box.find('.//ns:cp', namespaces=namespace).text if box.find('.//ns:cp', namespaces=namespace) is not None else ""
        co = box.find('.//ns:co', namespaces=namespace).text if box.find('.//ns:co', namespaces=namespace) is not None else ""
        zip = box.find('.//ns:zip', namespaces=namespace).text if box.find('.//ns:zip', namespaces=namespace) is not None else ""
        addressPoint = box.find('ns:addressPoint', namespaces=namespace).text if box.find('ns:addressPoint', namespaces=namespace) is not None else ""
        state = box.find('ns:state', namespaces=namespace).text if box.find('ns:state', namespaces=namespace) is not None else ""
        pdz = box.find('ns:pdz', namespaces=namespace).text
        ovm = box.find('ns:ovm', namespaces=namespace).text
        isMaster = box.find('.//ns:isMaster', namespaces=namespace).text if box.find('.//ns:isMaster', namespaces=namespace) is not None else ""
        idOVM = box.find('ns:idOVM', namespaces=namespace).text if box.find('ns:idOVM', namespaces=namespace) is not None else ""

# Zápis řádku do CSV souboru
        csvwriter.writerow([id, type, subtype, firstName, lastName, tradeName, ico, city, district, street, cp, co, zip, addressPoint, state, pdz, ovm, isMaster, idOVM])

print('Data byla převedena do CSV souboru.')
