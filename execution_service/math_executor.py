# See mathformat.txt for explanation
import math
import json


def calculate(calculation_json):
    json_data = json.loads(calculation_json)
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


def SIN(A):
    return math.sin(A)


def COS(A):
    return math.cos(A)
