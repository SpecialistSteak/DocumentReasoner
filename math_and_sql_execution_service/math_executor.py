import math
import json

from query_executor import get_query_data


# Example input calculation_json:
# {
#   "lines": [
#     {
#       "command": "ADD",
#       "params": [
#         {
#           "metric_id": 1,
#           "fiscal_year": 2023,
#           "fiscal_period": "FY",
#           "company_ticker": "AAPL"
#         },
#         {
#           "metric_id": 2,
#           "fiscal_year": 2023,
#           "fiscal_period": "FY",
#           "company_ticker": "AAPL"
#         }
#       ]
#     },
#     {
#       "command": "SUBTRACT",
#       "params": [
#         "$0$",
#         {
#           "metric_id": 3,
#           "fiscal_year": 2023,
#           "fiscal_period": "FY",
#           "company_ticker": "AAPL"
#         }
#       ]
#     }
#   ]
# }


def calculate(calculation_json, querydata):
    if isinstance(calculation_json, str):
        json_data = json.loads(calculation_json)
    else:
        json_data = calculation_json
    lines_list: list = json_data.get("lines")
    output_list: list = []
    for line in lines_list:
        get_query_data(line, querydata)
        A = None
        B = None
        input_list = None
        match line.get("command"):
            # Takes in two variables
            case "ADD":
                output_list.append(ADD(A, B))
            case "SUBTRACT":
                output_list.append(SUBTRACT(A, B))
            case "MULTIPLY":
                output_list.append(MULTIPLY(A, B))
            case "DIVIDE":
                output_list.append(DIVIDE(A, B))
            case "POW":
                output_list.append(POW(A, B))
            case "LOG":
                output_list.append(LOG(A, B))

            # Takes in one variable
            case "SQRT":
                output_list.append(SQRT(A))
            case "EXP":
                output_list.append(EXP(A))
            case "LN":
                output_list.append(LN(A))
            case "ABS":
                output_list.append(ABS(A))
            case "FLOOR":
                output_list.append(FLOOR(A))
            case "CEIL":
                output_list.append(CEIL(A))

            # Takes in a list
            case "MIN":
                output_list.append(MIN(input_list))
            case "MAX":
                output_list.append(MAX(input_list))
            case "AVG":
                output_list.append(AVG(input_list))
            case "SUM":
                output_list.append(SUM(input_list))

            # Else
            case _:
                print("Unknown operation.")

    print(json_data)


def ADD(A, B):
    return A + B


def SUBTRACT(A, B):
    return A - B


def MULTIPLY(A, B):
    return A * B


def DIVIDE(A, B):
    return A / B


def SQRT(A):
    return math.sqrt(A)


def EXP(A):
    return math.exp(A)


def POW(A, B):
    return math.pow(A, B)


def AVG(arr):
    return sum(arr) / len(arr)


def SUM(arr):
    return sum(arr)


def LN(A):
    return math.log(A)


def LOG(A, B):
    return math.log(A, B)


def ABS(A):
    return abs(A)


def MIN(A):
    return min(A)


def MAX(A):
    return max(A)


def FLOOR(A):
    return math.floor(A)


def CEIL(A):
    return math.ceil(A)
