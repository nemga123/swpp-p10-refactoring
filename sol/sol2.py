def censor(text, word):
    return text.replace(word, "*" * len(word))

if __name__ == "__main__":
    text = """Because he's the hero Gotham deserves but not the one it needs right now.
So we will hunt him, because he can take it. Because he's not out hero.
He is a silent guardian, a watchful protector... a dark knight."""

    word1 = "hero"
    word2 = "silent"

    # TODO: 4. Consider general usage
    # TODO: 3. Substitute algorithm

    text = censor(text, word1)

    if text.count("*") > 5:
        print("More than five *")

    text = censor(text, word2)

    if text.count("*") > 5:
        print("More than five *")

    # Print result `text`
    print(text)