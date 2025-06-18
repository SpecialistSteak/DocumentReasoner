from pydantic import BaseModel

class FinParam(BaseModel):
    metric_id: int
    fiscal_year: int
    fiscal_period: str
    company_ticker: str

class Line(BaseModel):
    command: str
    params: list[FinParam | str]

class JsonCompanyOutputFormat(BaseModel):
    lines: list[Line]

# JSON Example:
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
