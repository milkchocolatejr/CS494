"""
# Develop a program using Retrieval-Augmented Generation (RAG) to retrieve information from the course syllabus and answer user questions.
# You are free to use any API or open-source models to build your assistant.
# You may use the RAG lab materials from Canvas as a reference.



"""
import random
import time

from keybert import KeyBERT
from dotenv import load_dotenv
from ollama import chat
from datetime import datetime
import re, math, subprocess, os

from pyparsing import results

TEMP = .3 # Low, should limit creativity
TOP_P = .2 # Low, great for Q&A applications
TOP_K = 8
MODEL_NAME = "llama3.1:8b"
SYLLABUS_FILE = "Syllabus.txt"
DEBUG = False
RELEVANCE_TOLERANCE = 0.0000001
MOST_RELEVANT = True
MAX_CLUSTER = 1

# A helper used to clear the terminal on all OS
# Needed because I develop on 2 OS (Windows Desktop and Mac Laptop)
def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (posix)
    else:
        _ = os.system('clear')

# A helper to generate a unique time code
def get_time_code():
    return datetime.now().strftime("%Y-%m-%d") + str(random.randint(1, 1000))

# A helper to print out lines
def printLine():
    print("==============================")

def section_data(data):
    sections = {}

    lines = data.splitlines()

    current_title = None
    current_content = []

    for line in lines:

        line = line.strip()

        # Detect section header (line begins with <ROMAN>)
        if line.startswith("<"):

            # Save previous section before starting new one
            if current_title is not None:
                sections[current_title] = "\n".join(current_content).strip()

            current_title = line
            current_content = []

        else:
            if current_title is not None:
                current_content.append(line)

    # Save last section
    if current_title is not None:
        sections[current_title] = "\n".join(current_content).strip()

    return sections

# A helper function for index()
# Used to calculate the TF-IDF value for the given word
def vectorize(word, corpus):
    res = {}
    num_containing = 0


    for title, section_data in corpus.items():
        # Find # of valid tokens in data
        tokens = section_data.split()
        num_tokens = len(tokens)

        times_seen = tokens.count(word)

        TF = times_seen / num_tokens

        res[title] =  TF

        if times_seen > 0:
            num_containing = num_containing + 1


    IDF = 0

    try:
        IDF = math.log10(len(corpus)/ num_containing)
    except ZeroDivisionError:
        pass

    for title, TF in res.items():
        res[title] = TF * IDF

    if DEBUG:
        printLine()
        print("VECTORIZE DEBUG MESSAGE")
        printLine()
        print(f"Word: {word}")
        print(f"Sections found: {len(corpus)}")
        print(results)
        printLine()

    return res

# Returns a string representation of the source file.
def getCorpus():
    try:
        file = open(SYLLABUS_FILE, 'r', encoding='utf-8-sig')
        file_contents = file.read().lower()

        file.close()

        sections = section_data(file_contents)

        return sections, file_contents
    except FileNotFoundError:
        print(f"Error: The file '{SYLLABUS_FILE}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Given a query
# Returns a relevance relation dictionary
def index(keywords, corpus):
    relevance_dict = {}

    for word in keywords :
        if word not in relevance_dict.keys():
            relevance_dict[word] = vectorize(word, corpus)

    # Return relevance matrix -- Indexing complete
    return relevance_dict

# Given relevance weight array and corpus
# Returns relevant data from the corpus
def retrieve(relevance_dict, corpus):
    unique_words = set()
    weights = {}
    helpful_data = []

    for word, vector in relevance_dict.items():
        if(word) in unique_words:
            continue
        unique_words.add(word)

        for title, rating in vector.items():
            if title not in weights.keys():
                weights[title] = 0

            weights[title] += rating

    max_rating = 0
    for title, rating in weights.items():
        if rating > max_rating:
            max_rating = rating
            helpful_data = [title, corpus[title]]

    return helpful_data

# Given relevant data, the user's query, and the system_prompt
# Returns the LLM's response
def generate(helpful_data, query, sys_prompt):
    findings = "I found no relevant data from the corpus."

    print(helpful_data)

    if helpful_data:
        findings = f"I found this potentially relevant data from the section:\n\n{helpful_data[0]}\n\n{helpful_data[1]}"

    start = time.time()
    print(f"LLM Model '{MODEL_NAME}' started...")
    response = chat(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": sys_prompt + f"Preprocessing result : {findings}"},
            {"role": "user", "content": query},
        ],
        options={
            "temperature": TEMP,
            "top_p": TOP_P,
        }
    )

    end = time.time()

    print(f"Response generated! Time taken: {end - start}s")

    return response.message.content

def log_relevance(relevance_data, query, time_code):
    file_name = f"relevance_{time_code}.txt"
    file = open(file_name, "w")
    file.write("Query: " + query + "\n")
    file.write(str(relevance_data))
    file.close()

    return file_name

def log_retrieval(retrieval_data, query, time_code):
    file_name = f"retrieval_{time_code}.txt"
    file = open(file_name, "w")
    file.write("Query: " + query + "\n")
    file.write(str(retrieval_data))
    file.close()

    return file_name

def log_generation(generation_results, query, sys_prompt, time_code):
    file_name = f"generation_{time_code}.txt"
    file = open(file_name, "w")
    file.write("Query: " + query + "\n")
    file.write("System Prompt: " + sys_prompt + "\n")
    file.write(str(generation_results))
    file.close()

    return file_name

clear_terminal()
printLine()
print("CS494 - AGENTIC AI | ASSIGNMENT 2 | AJ WILLIAMS (awill276) 'THE GOAT'")
printLine()

load_dotenv()
corpus, file_content = getCorpus()

kb_model = KeyBERT()

sys_prompt = (
    "You are to act as a chatbot agent, assigned to students who are attempting to learn information about the course. "
    "The user will ask a question, or state a topic that they are interested in, and you are to provide SOME information on that."
    "The invariant is that you must make the answer accurate and supplemented by the syllabus. SYLLABUS IS LAW."
    "You will have two things at your disposal to provide this information."
    "First, you will have access to the entire syllabus, so you can create informed answers"
    "In your context window, you will also have specialized information that you can point the user towards."
    "Quoting the syllabus when you can is always best, but ONLY if it is deemed supplemental to the answer."
    "If the question is not related to the course, or you receive no information related to the question"
    ", you can respond with REJECT, and provide reasoning to your rejection (2 sentence max)."
    "Your format should contain your 1-15 sentence personal evaluation, and then any supplemental text in block indent style."
    "Make sure you think carefully before responding, and provide answers similar to a professor that is teaching the course.")


while(True):
    printLine()
    it_code = str(get_time_code())
    print("******* CURRENT TIME ID: " + it_code + " *******")
    printLine()
    print("NOTE: Hit 'enter' to quit the program.")
    raw_query = input("What would you like to know about CS 494?: ").lower()

    if raw_query == "" :
        break

    keywords_tuple = kb_model.extract_keywords(
        raw_query,
        keyphrase_ngram_range=(1, MAX_CLUSTER), # Only allows 1 word long keywords
        stop_words="english",
        top_n = TOP_K,
    )

    keywords = []

    for kw, _ in keywords_tuple:
        keywords.append(kw)

    print(f"Keywords identified: {keywords}")

    relevance_data = index(keywords, corpus)

    relevance_log_file_name = log_relevance(relevance_data, raw_query, it_code)

    print(f"Indexing complete. Results stored in : '{relevance_log_file_name}'")

    helpful_data = retrieve(relevance_data, corpus)

    helpful_log_file_name = log_retrieval(helpful_data, raw_query, it_code)

    print(f"Retrieval complete. Results stored in : '{helpful_log_file_name}'")

    generation_results = generate(helpful_data, raw_query, sys_prompt)

    generation_log_file_name = log_generation(generation_results, raw_query, sys_prompt, it_code)

    print(f"Generation complete. Results stored in : '{generation_log_file_name}'")
