import google.genai as genai

# Initialize the client with your API key
client = genai.Client(api_key="AIzaSyAn35IjK0ZDGYSGWIwRTPdTwOrVGW1R5aw")



from google.genai import types

response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents='What is coding?',
    config=types.GenerateContentConfig(
        system_instruction='You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant.'
    )
)

print("Jarvis says:", response.text)
