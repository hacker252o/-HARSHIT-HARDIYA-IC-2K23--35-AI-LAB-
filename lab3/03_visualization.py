import matplotlib.pyplot as plt

students = ["Aman", "Riya", "Kabir", "Sara", "Neha"]
marks = [72, 85, 91, 64, 78]

plt.figure(figsize=(7, 4))
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()
