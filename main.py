import openai
key="************************"#hidden key

openai.api_key = key

begin_of_Bot_chat = "BOT:"
Begin_of_human_chat = "YOU: "


def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[Begin_of_human_chat, begin_of_Bot_chat]
    )

    return response["choices"][0]["text"]


conversation = begin_of_Bot_chat + " Hello, How can i assist you?"
while True:

    print(conversation)
    human_input = input(Begin_of_human_chat)
    if human_input.lower() == "exit":
        break
    conversation = get_response(conversation + Begin_of_human_chat + human_input)
