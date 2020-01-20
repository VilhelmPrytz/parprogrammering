def uncensor(txt, vowels):
    formatted_string = txt.replace("*", "{}")
    return formatted_string
