with open("cred_secrets", "r") as file:
    GEMINI_API_KEY = file.read().replace('\n', '')

import re
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])
context = """
    Am using you to to answer user questions therefore be brief and exact and direct to the point,
    don't provide additional content. For context, use current data from Openweather.
    Consider this in all the following chats. Format all responses in all chats as a list or a summarised paragraph.
"""
chat.send_message(context)

def send_prompt(prompt):
    response = chat.send_message(prompt)
    return response
    #return response_text_formatter(response.text)

def response_text_formatter(raw_text):
    sections_dict = {}
    sections = re.split(r'(\*\*.*?\*\*)\n', raw_text)
    # Iterating through the sections to populate the dictionary
    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        text_block = sections[i + 1].strip()
        sections_dict[heading] = text_block
    # Formatting the text in the keys and values
    if not (sections_dict == {}):
        keys_list = []
        values_list = []
        for key, value in sections_dict.items():
            new_key = key.replace("**", "")
            keys_list.append(new_key)

            new_value = value.replace("**", "")
            new_value = value.replace("*", "")
            values_list.append([new_value])

        final_dict = dict(zip(keys_list, values_list))
        return (final_dict)
    else:
        intermidiate_text = re.sub(r"\*+", "", raw_text)
        processed_text = intermidiate_text.split("\n")
        if "" in processed_text: processed_text.remove("")
        return (processed_text[0:2])


gen_res1 = send_prompt("air pollution prevantive measures")
#gen_res2 = send_prompt("air pollution levels in Juja")
#gen_res3 = send_prompt("most polluted towns in kenya")
print(gen_res1)
