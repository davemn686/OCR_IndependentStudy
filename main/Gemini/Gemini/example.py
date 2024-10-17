import google.generativeai as genai
import os

# Configure the API key once before the loop
genai.configure(api_key=os.environ["API_KEY"])

while True:
    # Prompt the user for input
    user_input = input("Enter Prompt : ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Exiting prompt. . .")
        break  # Exit the loop
    
    # Otherwise, proceed with the model call
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    
    # Print the model's response
    print(response.text)
