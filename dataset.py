import xml.etree.ElementTree as ET

def read_xml_file(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    list_with_all_boxes = []

    for boxes in root.iter('object'):
        image_id = root.find('filename').text
        class_name = boxes.find('name').text

        ymin, xmin, ymax, xmax = None, None, None, None
        ymin = str(int(boxes.find("bndbox/ymin").text))
        xmin = str(int(boxes.find("bndbox/xmin").text))
        ymax = str(int(boxes.find("bndbox/ymax").text))
        xmax = str(int(boxes.find("bndbox/xmax").text))

        tuple_with_single_box = (image_id, class_name, xmin, ymin, xmax, ymax)
        single_row = get_format_result(tuple_with_single_box)
        list_with_all_boxes.append(single_row)
    return list_with_all_boxes

def get_format_result(iterator):
    separator = ','
    return separator.join(iterator)