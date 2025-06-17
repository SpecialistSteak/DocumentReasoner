import json


def get_querydata(calculation_json):
    if isinstance(calculation_json, str):
        json_data = json.loads(calculation_json)
    else:
        json_data = calculation_json

    lines_list :list = json_data.get("lines")
    output_list :list = []
    for line in lines_list:

