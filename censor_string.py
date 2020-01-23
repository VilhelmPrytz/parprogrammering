def censor_string(txt, lst, char):
    return_data = []

    for word in txt.split():
        is_banned = False
        for banned in lst:

            if word.lower() == banned.lower():
                is_banned = True

        return_data.append(char * len(word)) if is_banned else return_data.append(word)
        
    return " ".join(return_data)

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))
print(censor_string("The cow jumped over the moon.", ["cow", "over"], "*"))
print(censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*"))
