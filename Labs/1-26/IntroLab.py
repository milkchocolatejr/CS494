import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 10

MY_PROMPT = "Reverse this text <text>Hello, World!</text>"
MODEL_NAME = "llama3.1:8b"
EXPECTED_OUTPUT = "!dlroW ,olloH"
TEMP = 0.05


# ---Basic Prompt Test --- #
# Runs the basic prompt a set number of times, and returns true if expected output is given.
def basic_prompt_test(prompt: str, expected: str) -> bool:
    print(f"Your prompt says: {prompt}")
    print("Expected output:", EXPECTED_OUTPUT)

    for i in range(NUM_RUNS_TIMES):
        print(f"Running your prompt... [{i}/{NUM_RUNS_TIMES}]")
        response = chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": expected},
            ],
            options={"temperature": TEMP},
        )
        output_text = response.message.content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip() or output_text.strip().__contains__(EXPECTED_OUTPUT):
            print("     Expected output SUCCESS!")
            return True
        else:
            print(f"    Expected output: {EXPECTED_OUTPUT}")
            print(f"    Actual output: {output_text}")
    return False


def main():
    basic_prompt_test(MY_PROMPT, EXPECTED_OUTPUT)


main()
