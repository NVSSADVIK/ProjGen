import google.generativeai as genai

API_Key = "AIzaSyDs5v8_2e7N1dTxydx1LtdQlOSQW3lvfAU"
genai.configure(api_key=API_Key)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Enter exit to quit")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("\nGemini: ", response.text)
