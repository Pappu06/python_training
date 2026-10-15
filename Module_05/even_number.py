
with open("numbers.txt", "r") as f:
    numbers = f.readlines()

even_numbers = []
count = 0
for number in numbers:
    if int(number.strip()) % 2 == 0:
        even_numbers.append(number.strip())
        count += 1

print(f"Number of even numbers: {count}")
