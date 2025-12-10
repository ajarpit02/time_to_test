def reverse_string(text):
    return text[::-1]

def count_words(text):
    return len(text.split())

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
