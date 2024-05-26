import json

file_path = 'C:/pythonworkspace/AI_practice/YOLO_Object_Detection'

with open(file_path, 'r', encoding='utf-8') as fp:
    data = json.load(fp)

print(json.dumps(data, indent=4))