import os
from pathlib import Path

from get_json_from_report import *

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=(os.getenv("GOOGLE_AI_STUDIO_API_KEY")))

media = Path("/document_parser/reports/")

# jsons = get_json_from_reports(["aapl-20230930.pdf","nflx-20231231.pdf","pltr-20231231.pdf"], media, client)
json = get_json_from_report("aapl-20230930.pdf", media, client)

# print(jsons)
print(json)
