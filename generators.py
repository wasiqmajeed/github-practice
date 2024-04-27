name_list: list = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "Gabriel", "Hannah",
    "Isaac", "Jessica", "Kevin", "Luna", "Michael", "Nora", "Oliver", "Penelope",
    "Quinn", "Riley", "Sophia", "Theodore", "Umaima", "Victor", "Willow", "Xavier",
    "Yara", "Zachary", "Amelia", "Benjamin", "Camila", "Daniel", "Evelyn", "Felix",
    "Georgia", "Henry", "Isabella", "Jack", "Katherine", "Liam", "Maya", "Noah",
    "Olivia", "Penelope", "Santiago", "Valentina", "William", "Aria", "Elijah",
    "Harper", "Jasper", "Luna", "Mateo", "Nora", "Owen", "Riley", "Sadie"
]


def generator_func(data: list):
    for name in data:
        yield name


gen_names = generator_func(name_list)

print(next(gen_names))
print(next(gen_names))
print(next(gen_names))

for names in gen_names:
    print(names)
