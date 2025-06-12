from expected_json_format_class import JsonCompanyOutputFormat

basePrompt = open("extract_prompt.txt", "r").read()


def get_json_from_report(filename, media, client):
    try:
        report = client.files.upload(file=media / filename)
    except Exception as e:
        print(f"some error with files {str(e)}")
        return "{}"

    print("Sending report to Gemini")

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=[basePrompt, report],
            config={
                "response_mime_type": "application/json",
                "response_schema": JsonCompanyOutputFormat,
            }
        )
    except Exception as e:
        print(f"some error with sending to Gemini {str(e)}")
        return "{}"

    return response.text


def get_json_from_reports(filename, media, client):
    json_files_of_documents = []

    print("Sending reports to Gemini")

    increment = 1

    for file in filename:
        try:
            report = client.files.upload(file=media / file)
        except Exception as e:
            print(f"some error with files {str(e)}")
            return "{}"

        print(f"Sending report {increment} to Gemini")
        increment += 1

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-preview-05-20",
                contents=[basePrompt, report],
                config={
                    "response_mime_type": "application/json",
                    "response_schema": JsonCompanyOutputFormat,
                }
            )
        except Exception as e:
            print(f"some error with sending to Gemini: {str(e)}")
            print(f"SETTING RESPONSE {increment - 1} to empty")
            response = "{}"

        json_files_of_documents.append(response.json())

    return json_files_of_documents
