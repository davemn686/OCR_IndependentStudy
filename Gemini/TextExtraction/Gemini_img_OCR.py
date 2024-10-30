
import google.generativeai as genai

genai.configure(api_key="AIzaSyDLt7t45guqJn21t9XFJYG7CQJnfmlxsuw")

filePath = input("Enter file path : ")

# Upload the image file
myfile = genai.upload_file(filePath)


# Generate content with the Gemini model
result = genai.GenerativeModel("gemini-1.5-flash").generate_content([myfile, "\n", 'WHAT TEXT IS IN THIS IMAGE'])


# Output the result
print(result.text)
