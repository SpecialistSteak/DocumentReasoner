import json

hello_prompt = open("hello_prompt.txt", "r").read()


def call_ai(userinput, client):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=hello_prompt,
        )
    except Exception as e:
        print(f"some error with sending to Gemini {str(e)}")
        return "{}"

    return json.loads(response.text)
