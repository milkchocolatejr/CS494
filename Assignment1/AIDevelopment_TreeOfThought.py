import os
from dotenv import load_dotenv
from ollama import chat
NUM_TESTS = 3
MODEL_NAME = "llama3.1:8b"

TEMP = .9
TOP_P = .5

SYSTEM_PROMPT = ("Put yourself in 5 different perspectives of interdisciplinary experts that are centered around the topic you've been asked about. Give their titles in your output, followed by a colon, and then their perspective. When they are completed with their thoughts, output a newline"
                 "You should give 3-5 sentences, the first sentence should be the main point, and the rest should be your thought process. This thought process should be reflective of that perspective's job title."
                           "You should conduct 5 rounds of discussion-style deliberation, before coming to your final answer. Output all of the thoughts, and make the output clean and readable. After this deliberation, you should give your response.")

USER_PROMPT = "How should we proceed with the development of AI? Does it make sense to keep pushing it's development, or should we refine its use-cases, and make it more environmentally friendly?"


def printLine():
    print("==============================")

def main():
    load_dotenv()
    print("Program start!")
    printLine()
    print("System Prompt : " + SYSTEM_PROMPT)
    print("User Prompt : " + USER_PROMPT)
    print("Temperature : " + str(TEMP))
    print("TOP_P : " + str(TOP_P))
    printLine()

    response = chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT}
        ],
        options={
            "temperature": TEMP,
            "top_p": TOP_P,
        }
    )

    print(response.message.content)


main()