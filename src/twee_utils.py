import uuid
import json


def twee_metadata_template(position_x, position_y, width, height):
    position = str(position_x) + "," + str(position_y)
    size = str(width) + "," + str(height)
    metadata = {"position" : position, "size" : size}
    return metadata


def twee_header_template(name:str, tags:list, metadata:dict) -> str:
    
    header_name = str(name)

    assert isinstance(tags, list), f"Function expected a list for arg:tags, instead got {type(tags)}."
    
    header_tags = "["
    
    for tag in tags: header_tags += f"{tag} "
    
    header_tags += "]"
    
    header_metadata = str(metadata)
    
    twee_header = ":: " + header_name + " " + header_tags + " " + header_metadata + "\n"
    
    return twee_header


def render_twee_header(filename:str, header:str):
    if filename[-3:] != ".tw": filename += ".tw"
    with open(filename, "w", encoding='utf-8') as twee_file:
        twee_file.write(str(header))


def get_UUID():
    with open("novel_deets.json", "r", encoding='utf-8') as detail_file:
        novel_data = json.load(detail_file)
    if novel_data['UUID']: 
        return novel_data['UUID']
    fresh_uuid = uuid.uuid4()
    standard_uuid = ""
    for char in str(fresh_uuid):
        if char.isalpha(): standard_uuid += char.upper()
        elif char.isnumeric(): standard_uuid += char
        else: standard_uuid += char
    if len(str(fresh_uuid)) != len(standard_uuid):
        return 0
    return standard_uuid

