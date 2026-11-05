# Facts represented as simple triples: subject, relation, object.
knowledge = [
    ("A dog", "is_a", "Animal"),
    ("A dog", "has", "Four legs"),
    ("A parrot", "is_a", "Bird"),
    ("A bird", "can", "Fly")
]

for subject, relation, obj in knowledge:
    print(subject, relation, obj)

# A basic query
query = ("A dog", "is_a")
for subject, relation, obj in knowledge:
    if (subject, relation) == query:
        print("Answer:", obj)
