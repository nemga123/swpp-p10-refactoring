def censor_and_alert(text, *word_list, replace_pattern="*", alert_threshold=5):
    for word in word_list:
        text = text.replace(word, replace_pattern * len(word))
        if text.count("*") > alert_threshold:
            print(f"More than {alert_threshold} {replace_pattern}")
    return text

if __name__ == "__main__":
    text = """Because he's the hero Gotham deserves but not the one it needs right now.
So we will hunt him, because he can take it. Because he's not out hero.
He is a silent guardian, a watchful protector... a dark knight."""

    word1 = "hero"
    word2 = "silent"

    # TODO: 4. Consider general usage
    # TODO: 3. Substitute algorithm

    # TODO: 2. Extract method, remove duplicated code
    # Censor `word1` from `text`
    text = censor_and_alert(text, word1, word2)

    # TODO: 2. Extract method, remove duplicated code
    # Censor `word2` from `text`
    # Print result `text`
    print(text)