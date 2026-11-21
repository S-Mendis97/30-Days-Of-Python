print("\n### Exercise 18 ###")
print("------------------")


# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

# re.match(...)/ re.search(...)/ re.findall(...) - (substring/pattern, string, re.I is case for ignore flag) using re.I includes both upper and lowercase

import re

print("Level 1\n-------")

paragraph = 'I love teaching. If you do not love teaching what else can you love. ' \
'I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

paragraph_split = re.split(r'\s+',                              # split on one or more whitespace characters
                           re.sub(r'[^\w\s]', '', paragraph))   # replace anything that is not a word character or a whitespace with ''

word_num = {}
for word in paragraph_split:

    if word in word_num:
        word_num[word] += 1
    else:
        word_num[word] = 1

word_num_sorted = sorted([(count, word) for word, count in word_num.items()], reverse=True)

print("1. Paragraph:", paragraph, "\nNew paragraph:", paragraph_split)

print("\nFrequency of words:")
for tuple in word_num_sorted:
    print(tuple)


print("\n2. Extract the numbers from the following text and find the distance between the two furthest particles: The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.")

txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

point_matches = re.findall(r'-?\d+', txt)
points = [int(point) for point in point_matches]

print("Extracted points:", points)

mx_pt = max(points)
mn_pt = min(points)
distance = mx_pt - mn_pt

print(f"Distance between the two furthest points, {mx_pt} - ({mn_pt}) = {distance}")





print("\n\nLevel 2\n-------")

def is_valid_variable(variable):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

    if re.match(pattern, variable):
        return True
    else:
        return False

print("Are the following variables valid?")
print("first_name:", is_valid_variable('first_name'))
print("first-name:", is_valid_variable('first-name'))
print("1first_name:", is_valid_variable('1first_name'))
print("firstname:", is_valid_variable('firstname'))





print("\n\nLevel 3\n-------")

sentence = '''%I $am@% a %teacher%, &and& I lo%ve %teaching%;
There $is nothing; &as& mo@re rewarding as educating &and& @emp%o@wering
peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs.
%Does thi%s mo@tivate yo@u to be a tea@cher!?'''

print("Messy sentence:\n", sentence)

# Remove special characters
clean_text = re.sub(r'[%$@&;,.!?]', '', sentence) # or r'[^\w\s]'
print("\nClean text:\n", clean_text)

# Split into words
words = clean_text.split()
print("\nSplit into words:\n", words)

# Count words
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sort by frequency
sorted_words = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True)

print("\nThree most frequent words:", sorted_words[:3])