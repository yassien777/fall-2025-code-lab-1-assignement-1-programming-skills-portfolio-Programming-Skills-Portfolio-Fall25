questions = {
    "France": "paris",
    "Germany": "berlin",
    "Italy": "rome",
    "Spain": "madrid",
    "Egypt": "cairo",
    "Japan": "tokyo",
    "Canada": "ottawa"
}


for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")

    if answer.lower() == capital:
        print("Correct!")
    else:
        print("Wrong!")