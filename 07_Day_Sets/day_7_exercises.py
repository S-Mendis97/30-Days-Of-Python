print("\n### Exercise 7 ###")
print("------------------")

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("The following sets are already given:")
print("IT Companies:", it_companies)
print("\nSets\nA:", A, "\nB:", B)
print("\nAges:", age)

print("\n\nLevel 1: IT Companies\n---------------------")

print("Length of IT Companies set:", len(it_companies))

it_companies.add('Twitter')
print("\nAdd Twitter to IT Companies set using .add:", it_companies)

it_companies.update('X')
print("\nAdd X to IT Companies set using .update:", it_companies)


add_it_companies = ('Comp1', 'Comp2', 'Comp3', 'Comp4', 'Comp5')
it_companies.update(add_it_companies)
print("\nAdd more IT Companies:", it_companies)

remove_comp = input("\nEnter the company to delete: ")
it_companies.remove(remove_comp.capitalize())
print(f"IT Company list after deleting {remove_comp}:", it_companies)

print("\nDifference between .remove and .discard: .discard doesn't throw an error if the item to be deleted is not found in the list")



print("\n\nLevel 2: Sets A & B\n-------------------")

print("A:", A, "\nB:", B)

AB_union = A.union(B)
print("\nA and B joined using .union:", AB_union)

print("\nA intersection B using .intersection:", A.intersection(B))

print("\nIs A a subset of B?", A.issubset(B))

print("\nAre A and B disjoin sets?", A.isdisjoint(B))

print("\nJoin A with B:", A.union(B))
print("Join B with A:", B.union(A))

print("\nSymmetric difference between A and B using .symmetric_difference:", A.symmetric_difference(B))

print("\nDeleting sets A and B...")
del A, B
try:
    A, B
except NameError:
    print("Sets A and B have been deleted!")
else:
    print("Sets A and B have not been deleted!")



print("\n\nLevel 3: Ages\n-------------")

print("Ages:", age)

age_set = set(age)
print(f"Convert the list ages ({age}) to a set -> {age_set}")

sentence = 'I am a teacher and I love to inspire and teach people'

'''
split_sentence = sentence.split()

print("\nSentence:", sentence, "\nSplit sentence:", split_sentence)

unique_words = []

for word in split_sentence:
    if word not in unique_words:
        unique_words.append(word)

print("\nUnique words:", unique_words, "\nNumber of unique words:", len(unique_words))

'''

print("\nSentence:", sentence, "\nSplit sentence:", sentence.split())

unique_words2 = []

for word in sentence.split():
    if word not in unique_words2:
        unique_words2.append(word)

print("\nUnique words:", unique_words2, "\nNumber of unique words:", len(unique_words2))