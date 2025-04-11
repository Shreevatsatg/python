import random

#simulate a vocabulary
vocab=["hello","world","cat","dog","banana","code","run","sit","eat","apple"]

#simulate a model
def model_predictict(prev_tokens,position):
    if position==0:
        possible=["hello","code","cat"]
    elif position==1 and "code" in prev_tokens:
        possible=["run","sit"]
    elif position==1:
        possible=["world","banana","dog"]
    elif position==2:
        possible=["apple","banana","eat"]
    else:
        possible=vocab

#return a random from th list
    return random.choice(possible)

#generation function
def generate_text(max_length=5):
    generated =[]
    for position in range(max_length):
        next_token=model_predictict(generated,position)
        generated.append(next_token)
    return" ".join(generated)

#example run
print(generate_text())
