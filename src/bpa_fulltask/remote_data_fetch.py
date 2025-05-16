import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

def fetch_and_parse_suppliers() -> List[Dict[str, str]]:
    url = "https://services.odata.org/northwind/northwind.svc/Suppliers"
    # headers = {
    #     "Accept": "application/xml"
    # }
    response = requests.get(url)#, headers=headers)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    ns = {
        'atom': 'http://www.w3.org/2005/Atom',
        'd': 'http://schemas.microsoft.com/ado/2007/08/dataservices',
        'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata'
    }

    suppliers: List[Dict[str, str]] = []

    for entry in root.findall('atom:entry', ns):
        content = entry.find('atom:content', ns)
        if content is None:
            continue

        properties = content.find('m:properties', ns)
        if properties is None:
            continue

        supplier: Dict[str, str] = {}
        for child in properties:
            tag = child.tag.split('}', 1)[-1]  # Remove namespace
            text = child.text if child.text is not None else ''
            supplier[tag] = text

        suppliers.append(supplier)

    return suppliers


if __name__ == "__main__":
    print("ok step 1\n")
    suppliers_list = fetch_and_parse_suppliers()
    for supplier in suppliers_list[:3]:  # Just print first 3 for inspection
        print(supplier)

# suppliers_list = fetch_and_parse_suppliers()
# for supplier in suppliers_list[:3]:  # Just print first 3 for inspection
#     print(supplier)


        
