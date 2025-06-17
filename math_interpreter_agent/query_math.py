import json

math_prompt = open("mathagentqueryprompt.txt", "r").read()

from math_and_sql_execution_service.expected_json_format_calculations_class import FinParam

def generate_math_query(userinput, client):
    try:
        final_math_prompt = math_prompt + userinput
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=final_math_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": FinParam,
            }
        )
    except Exception as e:
        print(f"some error with sending to Gemini {str(e)}")
        return "{}"

    return json.loads(response.text)
