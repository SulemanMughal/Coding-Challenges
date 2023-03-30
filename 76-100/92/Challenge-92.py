import re
def hidden_anagram(text, phrase):
    text = re.sub(r'[^a-z]', '', text.lower())
    phrase = re.sub(r'[^a-z]', '', phrase.lower())
    
    for i in range(len(text)):
        if sorted(phrase) == sorted(text[i:i+len(phrase)]):
            return text[i:i+len(phrase)]
    
    return 'noutfond'