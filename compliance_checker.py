def load_additives(filename):
    additives = {}

    with open(filename, "r") as file:
        for line in file:
            name, function = line.strip().split("=")
            additives[name] = function

    return additives


additives = load_additives("additives.txt")

with open("sample_ingredients.txt", "r") as file:
    ingredients = file.read()

print("Food Additive Compliance Report")
print("-" * 35)

found = False

for additive, function in additives.items():

    if additive.lower() in ingredients.lower():

        print(f"Additive Found: {additive}")
        print(f"Function: {function}")
        print()

        found = True

if not found:
    print("No known additives detected.")

print("Label Compliance Check Completed")