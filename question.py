from random import choice
import json

with open('spices.csv', 'r') as f:
    data = f.read().split('\n')

question = []
for i in data:
    value = i.split(',')
    # print(value)
    try:
        question.append({value[0]: [value[1], value[2], value[3]]})
    except:
        continue

question_shuffled = []
for i in question:
    while True:
        val = choice(question)
        if val not in question_shuffled:
            break
    question_shuffled.append(val)

print(json.dumps(question_shuffled))

print(len(question_shuffled))
