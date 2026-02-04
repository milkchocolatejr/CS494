import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_TESTS = 3
MODEL_NAME = "llama3.1:8b"


SYSTEM_PROMPT = "Act as a visual decorator! Your job is going to be drawing different things using ascii characters. These characters are confined to a 20 by 20 character grid. Any ASCII character can be used to construct shapes and define line. Output just the drawing."
USER_PROMPT = "Please draw an ASCII star!"

def main():
    print("Program start!")
    temp_values = [0.2, 0.5, 1.0]
    top_p_values = [0.8, 0.5, 0.7]

    for i in range(NUM_TESTS):
        print("=========================")
        print(f"  TEST {i} BEGIN")
        print(f"    Values Tested: top_p - {top_p_values[i]} | temp - {temp_values[i]}")

        response = chat(
            model = MODEL_NAME,
            messages = [
                {"role" : "system", "content" : SYSTEM_PROMPT},
                {"role" : "user", "content" : USER_PROMPT}
            ],
            options = {
                "temperature": temp_values[i],
                "top_p": top_p_values[i]
            }
        )

        print('\n\n\n')
        print(response.message.content)

        print(f"  TEST {i} END")
        print("=========================")


main()