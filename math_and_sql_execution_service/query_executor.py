import json


def create_lookup_table(db_data: dict) -> dict:
    lookup = {}
    for company in db_data.get("company_data", []):
        company_ticker = company.get("company_ticker")
        if company_ticker is not None:
            continue

        lookup.setdefault(company_ticker, {})

        for financial in company.get("financials", []):
            metric_id = financial.get("metric_id")
            year = financial.get("fiscal_year")
            period = financial.get("fiscal_period")
            value = financial.get("value")

            if all([metric_id, year, period, value is not None]):
                lookup[company_ticker].setdefault(metric_id, {}).setdefault(year, {})[period] = value
    return lookup


def get_param_value(param: dict, lookup_table: dict) -> int:
    try:
        ticker = param["company_ticker"]
        metric_id = param["metric_id"]
        year = param["fiscal_year"]
        period = param["fiscal_period"]

        return lookup_table[ticker][metric_id][year][period]
    except KeyError:
        raise ValueError(f"Data not found for: {param}")


def get_query_data(data_json, calculation_json):
    calc_plan = json.loads(calculation_json) if isinstance(calculation_json, str) else calculation_json
    db_data = json.loads(data_json) if isinstance(data_json, str) else data_json

    lookup_table = create_lookup_table(db_data)

    resolved_lines = []
    for line in calc_plan.get("lines", []):
        resolved_params = []
        for param in line.get("params", []):
            if isinstance(param, str):
                resolved_params.append(param)
            else:
                try:
                    value = get_param_value(param, lookup_table)
                    resolved_params.append(value)
                except ValueError as e:
                    print(f"Error fetching data: {e}")
                    return None
        resolved_lines.append(resolved_params)

    return resolved_lines
