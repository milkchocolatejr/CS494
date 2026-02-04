import os, random
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_TESTS = 20
MODEL_NAME = "llama3.1:8b"


SYSTEM_PROMPT = "Act as a visual decorator! Your job is going to be drawing different things using ascii characters. These characters are confined to a 50 by 50 character grid. Any ASCII character can be used to construct shapes and define line. Output just the drawing."
USER_PROMPT = "Please draw an ASCII house !"

def main():
    print(f"Program start! This version uses {NUM_TESTS} random combinations.")
    print(f"Model Name: {MODEL_NAME}")
    print(f"System Prompt: {SYSTEM_PROMPT}")
    print(f"User Prompt: {USER_PROMPT}")

    for i in range(NUM_TESTS):
        top_p = random.random()
        temp = random.random() * 2

        print("")
        print("=========================")
        print(f"  TEST {i} BEGIN")
        print(f"    Values Tested: top_p - {top_p} | temp - {temp}")

        response = chat(
            model = MODEL_NAME,
            messages = [
                {"role" : "system", "content" : SYSTEM_PROMPT},
                {"role" : "user", "content" : USER_PROMPT}
            ],
            options = {
                "temperature": temp,
                "top_p": top_p
            }
        )

        print('\n\n\n')
        print(response.message.content)

        print(f"  TEST {i} END")
        print("=========================")


main()