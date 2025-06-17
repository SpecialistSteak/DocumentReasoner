import math
import json


# Example input calculation_json:
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
#         100
#       ]
#     }
#   ]
# }

def calculate(calculation_json, querydata):
    if isinstance(calculation_json, str):
        json_data = json.loads(calculation_json)
    else:
        json_data = calculation_json
    lines_list :list = json_data.get("lines")
    output_list :list = []
    for line in lines_list:
        match line.get("command"):
            # Takes in two variables
            case "ADD":
                print()
            case "SUBTRACT":
                print()
            case "MULTIPLY":
                print()
            case "DIVIDE":
                print()
            case "POW":
                print()
            case "LOG":
                print()

            # Takes in one variable
            case "SQRT":
                print()
            case "EXP":
                print()
            case "LN":
                print()
            case "ABS":
                print()
            case "FLOOR":
                print()
            case "CEIL":
                print()

            # Takes in a list
            case "MIN":
                print()
            case "MAX":
                print()
            case "AVG":
                print()
            case "SUM":
                print()

            # Else
            case _:
                print()


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