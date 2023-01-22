
from gpt_j.gptj_api import Completion
context = "This is a calculator bot that will answer basic math questions"
max_length = 100
temperature = 0.5
top_probability = 1.0
top_k = 40
repetition = 0.216
examples = {
    "5 + 5": "10",
    "6 - 2": "4",
    "4 * 15": "60",
    "10 / 5": "2",
    "144 / 24": "6",
    "7 + 1": "8"}
context_setting = Completion(context, examples)
prompt = "48 / 6"
User = "Student"
Bot = "Calculator"
max_tokens = 50
response = context_setting.completion(prompt,
              user=User,
              bot=Bot,
              max_tokens=max_tokens,
              temperature=temperature,
              top_p=top_probability,
              top_k=top_k,
              rep=repetition)
print(response)
