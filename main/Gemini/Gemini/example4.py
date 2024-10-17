import google.generativeai as genai
import os

# Configure the API key once before the loop
genai.configure(api_key=os.environ["API_KEY"])

prompt = input("Enter your prompt: ")

fileName = input("Enter file destination: ")

with open(fileName, "r") as file:
    user_input = file.read()

model = genai.GenerativeModel("gemini-1.5-flash")

# Generate the initial response
response = model.generate_content("Make it short: " + prompt + "\t" + user_input)

# Extract the content of the response (assuming `content` or similar method returns the generated text)
initial_response_text = response.text  # Modify this line based on the actual property or method to get text

for i in range(10):
    x = model.generate_content("Rewrite this text in a similar way:\n" + initial_response_text)
    initial_response_text = x.text  # Update the text content for the next iteration

# Print the final response
print(initial_response_text)

