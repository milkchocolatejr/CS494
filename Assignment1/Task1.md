# Q 1.1: Write a prompt using 7 components:
1. Persona (Who is the model acting as?)
2. Instruction (What should the model do?)
3. Context (What background information does the model need?)
4. Format (How should the output be structured?)
5. Audience (Who is the response for?)
6. Tone (What tone should the model use?)
7. Data (What data, examples, or inputs are provided to the model? )

### Query: 

Act as a teacher who is assisting students with learning a how to use AI. Your task is to provide a comprehensive guide on local Ollama prompts in python for a new learner. You can reference Ollama's online libraries and models for further background. For each part of the python AI code, please explain what the parameters for the function/method are intended for. You should use a definitive tone with for your delivery.


You can use this example:

<example>
response = chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": expected},
            ],
            options={"temperature": TEMP},
        )
</example>

<explaination>
You can reference this for what kind of parameters should be explained. In this example, you should explain the "roles", and the "options". Furthermore, you should specify the difference between system and user roles.
</explaination>

 

# Q1.2 : Single Components Variation
## Create at least 2 variants by changing only one component at a time. 

###### For example, you could keep the prompt the same but write the persona in a different way, or keep the prompt but simplify the context to see what changes, or keep the prompt but adjust how strict the output format is.


### 1.2.1. Your prompt should be your own words. You can use any free AI tools (e.g. ChatGPT, ...) for this question to test out your prompt variations. Save your conversation in a pdf and upload the files. (your conversation should include your prompt and also the LLM's answer for different variations)

#### Variation 1
Act a life-long professional who is assisting students with learning a how to use AI. Your task is to provide a comprehensive guide on local Ollama prompts in python for a new learner. You can reference Ollama's online libraries and models for further background. For each part of the python AI code, please explain what the parameters for the function/method are intended for. You should use a definitive tone with for your delivery.

You can use this example:

<example>
response = chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": expected},
            ],
            options={"temperature": TEMP},
        )
</example>

<explaination>
You can reference this for what kind of parameters should be explained. In this example, you should explain the "roles", and the "options". Furthermore, you should specify the difference between system and user roles.
</explaination>


#### Variation 2

Act as a teacher who is creating dense class materials to teach computer science professionals how to use AI; these materials should be short, yet effective. Your task is to provide a comprehensive guide on local Ollama prompts in python for a new learner. You can reference Ollama's online libraries and models for further background. For each part of the python AI code, please explain what the parameters for the function/method are intended for. You should use a definitive tone with for your delivery.


You can use this example:

<example>
response = chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": expected},
            ],
            options={"temperature": TEMP},
        )
</example>

<explaination>
You can reference this for what kind of parameters should be explained. In this example, you should explain the "roles", and the "options". Furthermore, you should specify the difference between system and user roles.
</explaination>


### 1.2.1 Reflection question: what are your findings about changing the different format, write down your observations (undergraduate 2, graduate 4, feel free to write more if you have anything else to share). Questions to answer: Which prompt element acted as the strongest “behavioral lever” for the agent? Support your answer with evidence from at least two variants.

Changing the prompt did not yield different results than I anticipated. I  belived that there would be a small change between the prompt and the first variant. This was confirmed and supported by the content of the responses. The changes were slight, and they really only differed with small changes in structure, and the frequency of use of technical jargin. The second variation, albiet a small change in prompt, yeilded a more significant change-- as expected. The emphasis on dense materials made the code snippets more insightful, and better commented. Furthermore, the materials produced were way easier to ingest and reference quickly than the other responses. 

# Q1.3 : Variation on Components
##### Using the prompt you designed, create and test different combinations of prompt elements. For undergraduate students, test at least 2 combinations, and for graduate students, test at least 4 for a more thorough comparison. For example, you could test: Persona + Context + Tone , or Persona + Instruction. Observe how each combination affects the model’s behavior.

### 1.3.1 Save your conversation in a pdf and upload the files. (your conversation should include your prompt and also the LLM's answer for different variations)

#### Variation 1

#### Variation 2


### 1.3.2 Reflection question: what are your findings about changing the different combinations? Does using only a few prompt components work better than including all 7, or is the full set more effective? If you are require not to use all of 7 componetns, which combination do you think produces the most accurate results? Explain your reasoning.