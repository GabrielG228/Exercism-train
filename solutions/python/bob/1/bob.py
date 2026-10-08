def response(hey_bob):
    text = hey_bob.strip()

    if text == "":
        return "Fine. Be that way!"
    
    is_question = text.endswith("?")
    letters = [c for c in text if c.isalpha()]
    is_yell = letters and all(c.isupper() for c in letters)

    if is_question and is_yell:
        return "Calm down, I know what I'm doing!"
    elif is_yell:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
