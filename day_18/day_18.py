import re
from collections import Counter


paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

regex_pattern = r"[A-Za-z]+"
matches = re.findall(regex_pattern, paragraph.lower())
print(matches)

counts = Counter(matches)
print(counts)

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

regex_pattern = r"\d+|-\d+"
matches = re.findall(regex_pattern, text)
print(matches)
int_match = [int(i) for i in matches]
print(int_match)
print(int_match[-1] - int_match[0])


def clean_text(text: str):
    regex_pattern = r"[^a-zA-Z0-9 ]"
    text = re.sub(regex_pattern, "", text)

    return text


def most_frequent_words(text: str):
    regex_pattern = r"[A-Za-z]+"
    matches = re.findall(regex_pattern, text.lower())
    return Counter(matches).most_common(3)


sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))  # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
