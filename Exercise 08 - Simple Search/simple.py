names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]


if "Sam" in names:
    print("Sam is in the list!")
else:
    print("Sam is not in the list.")


search_term = input("Enter a name to search: ")

if search_term in names:
    print(search_term, "is in the list!")
else:
    print(search_term, "is not in the list.")