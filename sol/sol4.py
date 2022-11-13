def censor_and_alert(text, *words, replace_pattern="*", alert_threshold=5):
    for word in words:
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

    text = censor_and_alert(text, word1, word2)

    # Print result `text`
    print(text)