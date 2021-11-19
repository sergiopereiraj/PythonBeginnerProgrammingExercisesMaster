
# Your code here!!

def sing():
    for i in range(1, 12):
        text = ""
        if i <= 4:
            return text + "Let it bet,"
        elif i == 5:
            return text + "whisper words of wisdom,"
        elif i <= 10:
            return text + "Let it bet,"
        elif i == 11:
            return text + "there will be an answer,"
        else:
            return text + "Let it bet."


print(sing())