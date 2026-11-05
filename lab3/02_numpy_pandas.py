import numpy as np
import pandas as pd

marks = np.array([72, 85, 91, 64, 78])
print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Sorted:", np.sort(marks))

table = pd.DataFrame({
    "Student": ["Aman", "Riya", "Kabir", "Sara", "Neha"],
    "Marks": marks
})
table["Result"] = table["Marks"].apply(
    lambda value: "Pass" if value >= 40 else "Fail"
)

print("\nDataFrame:\n", table)
print("\nStudents scoring 80 or more:\n", table[table["Marks"] >= 80])
