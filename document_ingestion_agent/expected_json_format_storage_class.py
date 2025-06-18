from typing import List
from pydantic import BaseModel

class FinanceInformation(BaseModel):
    metric_id: int
    fiscal_year: int
    fiscal_period: str
    value: int

class CompanyFinancials(BaseModel):
    company_ticker: str
    filing_date: str
    currency: str
    financials: List[FinanceInformation]

class CompanyDataDocument(BaseModel):
    company_data: List[CompanyFinancials]

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