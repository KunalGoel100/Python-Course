import xml.etree.ElementTree as ET
from xml.dom import minidom

# Load the XML file
tree = ET.parse('ItfIn_Outp.xml')
root = tree.getroot()

# Function to modify GetMeasurementTable elements
def modify_get_measurement_table(element):
    if ( element.tag == 'GetMeasurementTable') or ( element.tag == 'GetFunction'):
        # Check conditions for Type attribute
        type_value = element.get('Type', '')
        if 'UBIT32' in type_value:
            code_value = "'((ui32) 0)'"
        elif '.eSt' in type_value:
            code_value = "'((ui8) 0)'"
        elif 't_fl' in type_value:
            code_value = "'((fl32) 0)'"
        elif 't.TBOOL' in type_value:
            code_value = "'((ui8) 0)'"
        elif 'Def_Etsys.e' in type_value:
            code_value = "'((ui8) 0)'"
        elif 't.BITCODED.UBIT8' in type_value:
            code_value = "'((ui8) 0)'"
        elif 't.UI16' in type_value:
            code_value = "'((ui16) 0)'"
        elif 't.UI32' in type_value:
            code_value = "'((ui32) 0)'"
        else:
            ref_element = element.find('Ref')
            code_value = ref_element.get('_') if ref_element is not None else ''

        # Replace Ref with code
        ref_element = element.find('Ref')
        if ref_element is not None:
            code_element = ET.Element('code', {'_': code_value})
            for attr, value in ref_element.attrib.items():
                if attr != '_':
                    code_element.set(attr, value)
            element.remove(ref_element)
            element.append(code_element)

# # Function to modify GetFunction elements
# def modify_get_function(element):
#     if element.tag == 'GetFunction':
#         # Check conditions for Type attribute
#         type_element = element.find('Type')
#         type_value = type_element.get('_', '') if type_element is not None else ''
#         if 'UBIT32' in type_value:
#             code_value = "'((ui32) 0)'"
#         elif '.eSt' in type_value:
#             code_value = "'((ui8) 0)'"
#         else:
#             ref_element = element.find('Ref')
#             code_value = ref_element.get('_') if ref_element is not None else ''

#         # Replace Ref with code
#         ref_element = element.find('Ref')
#         if ref_element is not None:
#             code_element = ET.Element('code', {'_': code_value})
#             for attr, value in ref_element.attrib.items():
#                 if attr != '_':
#                     code_element.set(attr, value)
#             element.remove(ref_element)
#             element.append(code_element)

# Function to remove unwanted empty lines
def remove_empty_lines(element):
    for elem in element.iter():
        if elem.text is not None:
            elem.text = elem.text.strip()
        if elem.tail is not None:
            elem.tail = elem.tail.strip()

# Iterate over all elements and apply modifications
for elem in root.iter():
    modify_get_measurement_table(elem)
    # modify_get_function(elem)

# Apply the function to remove empty lines
remove_empty_lines(root)

# Convert the modified XML tree to a string
xml_str = ET.tostring(root, encoding='unicode')

# Use minidom to pretty-print the XML
pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")

# Save the pretty-printed XML to a new file
with open('cleaned_modified_file.xml', 'w') as f:
    f.write(pretty_xml_str)

print("XML file has been modified, cleaned, and saved as 'cleaned_modified_file.xml'")
