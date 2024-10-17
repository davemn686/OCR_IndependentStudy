import google.generativeai as genai
import os

# Configure the API key once before the loop
genai.configure(api_key=os.environ["API_KEY"])

with open("promptExample.txt", "r") as file:
    user_input = file.read()

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(user_input)

# Print the model's response
print(response.text)
