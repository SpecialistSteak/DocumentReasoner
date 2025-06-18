import json


# Expected data_json format:
# {
#   "company_data": [
#     {
#       "company_ticker": "AAPL",
#       "filing_date": "2024-09-30",
#       "currency": "USD",
#       "financials": [
#         {
#           "metric_id": 1,
#           "fiscal_year": 2024,
#           "fiscal_period": "FY",
#           "value": 401500000000
#         },
#         {
#           "metric_id": 10,
#           "fiscal_year": 2024,
#           "fiscal_period": "FY",
#           "value": 102300000000
#         }
#       ]
#     },
#     {
#       "company_ticker": "MSFT",
#       "filing_date": "2024-06-30",
#       "currency": "USD",
#       "financials": [
#         {
#           "metric_id": 1,
#           "fiscal_year": 2024,
#           "fiscal_period": "FY",
#           "value": 236584000000
#         }
#       ]
#     }
#   ]
# }

# Expected calculation_json format:
# {
#   "lines": [
#     {
#       "command": "SUBTRACT",
#       "params": [
#         {"metric_id": 1, "fiscal_year": 2023, "fiscal_period": "FY"},
#         {"metric_id": 1, "fiscal_year": 2022, "fiscal_period": "FY"}
#       ]
#     },
#     {
#       "command": "DIVIDE",
#       "params": [
#         "$0$",
#         {"metric_id": 1, "fiscal_year": 2022, "fiscal_period": "FY"}
#       ]
#     },
#     {
#       "command": "MULTIPLY",
#       "params": [
#         "$1$",
#         {"metric_id": 1, "fiscal_year": 2022, "fiscal_period": "FY"}
#       ]
#     }
#   ]
# }

def fetch_param_data_from_db(param, data_json):
    metric_id = param["metric_id"]
    fiscal_year = param["fiscal_year"]
    fiscal_period = param["fiscal_period"]
    company_ticker = param["company_ticker"]

    data_json_financials = data_json["financials"]
    for data_json_financial in data_json_financials:
        if data_json["company_data"]["company_ticker"] == company_ticker:
            if (data_json_financial["metric_id"] == metric_id
                    and data_json_financial["fiscal_year"] == fiscal_year and
                    data_json_financial["fiscal_period"] == fiscal_period):
                return data_json_financial["value"]
    return None


def get_query_data(data_json, calculation_json):
    if isinstance(calculation_json, str):
        json_data = json.loads(calculation_json)
    else:
        json_data = calculation_json

    if isinstance(data_json, str):
        database_data = json.loads(data_json)
    else:
        database_data = data_json

    lines_list: list = json_data.get("lines")
    output_list: list = []
    for line in lines_list:
        params_for_this_line = line.get("params")
        params_for_this_line_output_list = []
        for param in params_for_this_line:
            if isinstance(param, str):
                params_for_this_line_output_list.append(param)
            else:
                params_for_this_line_output_list.append(fetch_param_data_from_db(param, database_data))
        output_list.append(params_for_this_line_output_list)
    return output_list
