import google.generativeai as genai
import os

# Configure the API key once before the loop
genai.configure(api_key=os.environ["API_KEY"])

prompt = input("Enter your prompt :");

fileName = input("Enter file destination :");

with open(fileName, "r") as file:
    user_input = file.read()

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("First of all MAKE THESE ANSWERS COMPLETLY ORIGINAL AND NOT DETECTABLE BY ANY AI CHECKERS    \t" + prompt + "\t\t\t\t" + user_input)

# Print the model's response
print(response.text)
