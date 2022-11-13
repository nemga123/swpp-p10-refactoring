def count_asterisk_exceed_five(text):
    return text.count("*") > 5

if __name__ == "__main__":
    text = """Because he's the hero Gotham deserves but not the one it needs right now.
So we will hunt him, because he can take it. Because he's not out hero.
He is a silent guardian, a watchful protector... a dark knight."""

    word1 = "hero"
    word2 = "silent"

    # Censor `word1` from `text`
    tmp = text
    while word1 in tmp:
        tmp = tmp[:tmp.find(word1)] + "*" * len(word1) + tmp[tmp.find(word1) + len(word1):]
    text = tmp

    if count_asterisk_exceed_five(text):
        print("More than five *")

    # Censor `word2` from `text`
    tmp = text
    while word2 in tmp:
        tmp = tmp[:tmp.find(word2)] + "*" * len(word2) + tmp[tmp.find(word2) + len(word2):]
    text = tmp

    if count_asterisk_exceed_five(text):
        print("More than five *")

    # Print result `text`
    print(text)