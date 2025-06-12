from pydantic import BaseModel


class FinanceInformation(BaseModel):
    metric_id: int
    fiscal_year: int
    fiscal_period: str
    value: int


class JsonCompanyOutputFormat(BaseModel):
    company_ticker: str
    filing_date: str
    currency: str
    financials: list[FinanceInformation]
