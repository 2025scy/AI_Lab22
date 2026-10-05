# Artificial Intelligence Lab

This repository contains my Artificial Intelligence lab work, written in Python.

## Lab 1: Python Basics

File: `AI_Lab1.py`

| Program | Description |
|---------|-------------|
| 1 | Calculates the percentage from total marks and obtained marks |
| 2 | Calculates the percentage and gives a grade (A, B, C, D, F) |
| 3 | Gives lab marks based on lab attendance (1 to 5) |
| 4 | Uses lists (`class_list` and `marks`) to calculate a result |

## Lab 2: Linear Regression (Student Attendance)

File: `lab2.py`

- Reads student attendance for Lab 1 to Lab 10 from an Excel file (`Student_Attendance_Dataset.xlsx`)
- Converts `P` (Present) to 1 and `A` (Absent) to 0
- Trains a Linear Regression model to predict **Final Marks** from attendance
- Predicts the final marks for a new student

## How to Run

1. Install Python 3 and VS Code.
2. Install the required libraries:
   ```
   pip install pandas scikit-learn openpyxl
   ```
3. Keep the Excel file in the same folder as `lab2.py`.
4. Run a program:
   ```
   python AI_Lab1.py
   python lab2.py
   ```

## Tools Used

- Python
- pandas
- scikit-learn
- VS Code
- Git and GitHub

## Author

GitHub: [2025scy](https://github.com/2025scy)
