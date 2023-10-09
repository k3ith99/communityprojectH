import openai

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

chat_log = []


while True:
    print("Can type")
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role": "user", "content": user_message})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )

        # look at the output; this outputs only the message content
        assistant_response = response['choices'][0]['message']['content']
        print("ChatGPT: ", assistant_response)

        # add the AIs response to chat log
        chat_log.append({"role": "assistant", "content": assistant_response})

