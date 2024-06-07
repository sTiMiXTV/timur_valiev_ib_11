person_friends = dict()

def add_friends(name_of_person, list_of_friends):
    global person_friends
    if name_of_person not in person_friends:
        person_friends[name_of_person] = list()
    person_friends[name_of_person].extend(list_of_friends)
    person_friends[name_of_person].sort()

def are_friends(name_of_person1, name_of_person2):
    global person_friends
    return name_of_person2 in person_friends[name_of_person1]

def print_friends(name_of_person):
    global person_friends
    print(' '.join(person_friends[name_of_person]))

add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))

print_friends("Алла")
