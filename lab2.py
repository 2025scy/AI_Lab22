import pandas as pd
from sklearn.linear_model import LinearRegression

# Excel file must be in the SAME folder as this lab2.py file
data = pd.read_excel("Student_Attendance_Dataset.xlsx")
print(len(data))

c = ["Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5",
     "Lab 6", "Lab 7", "Lab 8", "Lab 9", "Lab 10"]

# P = Present -> 1, A = Absent -> 0
data[c] = data[c].replace({"P": 1, "A": 0}).astype(int)

x = data[c]
y = data["Final Marks"]

model = LinearRegression()
model.fit(x, y)

# New student attendance (1 = present, 0 = absent)
N = [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
Ndf = pd.DataFrame([N], columns=c)

p = model.predict(Ndf)
print(p)
