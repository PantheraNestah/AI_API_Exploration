GEMINI_API_KEY = ""

import re
import google.generativeai as genai

def response_text_formatter(raw_text):
    sections_dict = {}
    sections = re.split(r'(\*\*.*?\*\*)\n', raw_text)
    # Iterating through the sections to populate the dictionary
    for i in range(1, len(sections), 2):
        heading = sections[i].strip()
        text_block = sections[i + 1].strip()
        sections_dict[heading] = text_block
    # Formatting the text in the keys and values
    keys_list = []
    values_list = []
    new_dict = {}
    for key, value in sections_dict.items():
        new_key = key.replace("**", "")
        keys_list.append(new_key)

        new_value = value.replace("**", "")
        new_value = value.replace("*", "")
        values_list.append([new_value])

    final_dict = dict(zip(keys_list, values_list))
    return (final_dict)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

#response = model.generate_content("Air pollution prevention techniques",)

chat = model.start_chat(history=[])
response2 = chat.send_message("examples of cities in kenya")
print(response2.text)
print(response_text_formatter(response2.text))
