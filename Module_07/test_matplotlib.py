import matplotlib.pyplot as plt

# # Data
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# # Create a line graph
# plt.plot(x, y)

# # Display the graph
# plt.show()


# days = [1, 2, 3, 4, 5, 6, 7]
# temperature = [28, 30, 29, 32, 31, 34, 33]

# plt.plot(days, temperature)

# plt.title("Temperature During the Week")
# plt.xlabel("Day")
# plt.ylabel("Temperature (°C)")

# plt.show()


# days = ["Monday", "Tuesday", "Wednesday", "Thursday",
#         "Friday", "Saturday", "Sunday"]

# visitors = [120, 150, 180, 160, 220, 300, 350]

# plt.plot(days, visitors)

# plt.title("Weekly Website Visitors")
# plt.xlabel("Day")
# plt.ylabel("Number of Visitors")

# plt.grid(True)

# plt.show()


# categories = ["Food", "Rent", "Travel", "Shopping", "Other"]
# expenses = [4000, 8000, 2000, 3000, 3000]

# plt.pie(expenses, labels=categories, autopct="%1.1f%%")

# plt.title("Monthly Expenses Distribution")

# plt.show()


# study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
# marks = [35, 40, 50, 55, 65, 70, 80, 90]

# plt.scatter(study_hours, marks)

# plt.title("Study Hours vs Exam Marks")
# plt.xlabel("Study Hours")
# plt.ylabel("Exam Marks")

# plt.grid(True)

# plt.show()



marks = [
    35, 40, 42, 45, 48,
    50, 52, 55, 58, 60,
    62, 65, 68, 70, 72,
    75, 78, 80, 85, 90
]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()