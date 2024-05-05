import numpy as np

while True:

    nat = input("Nationality(tr, gb, fr, de etc.) or q for exit: ").upper()
    if nat == "Q":
        break

    gender = input("Gender(M?F or q for exit): ").upper()
    if gender == "Q":
        break

    if gender == "M":

        with open("male_names.txt", "r", encoding='utf-16') as file:
            line = file.readlines()

            # Filter the unwanted nationalities
            line = [x for x in line if nat in x]
            # Filter the nationality attribute from the line
            line = [x.split(" -> ")[0] for x in line]

            max_results = len(line)

            male = line[np.random.randint(0, max_results)]

        print(f"Generated name: {male}")

    elif gender == "F":

        with open("female_names.txt", "r", encoding='utf-16') as file:
            line = file.readlines()

            # Filter the unwanted nationalities
            line = [x for x in line if nat in x]
            # Filter the nationality attribute from the line
            line = [x.split(" -> ")[0] for x in line]

            max_results = len(line)

            female = line[np.random.randint(0, max_results)]

        print(f"Generated name: {female}")

    else:
        print("Invalid input")