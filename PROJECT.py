import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#dataset
data = pd.read_csv("student_data.csv")

# Inputs(X) and Output(y)
X = data[["StudyHours", "Attendance", "PreviousMarks", "SleepHours", "AssignmentScore"]]
y = data["FinalMarks"]

# Split_data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()


model.fit(X_train, y_train)

StudyHours = float(input("Number of study hours: "))
Attendance = float(input("Attendance: "))
PreviousMarks = float(input("Previous Marks of a student: "))
SleepHours = float(input("Sleep Hours of a student: "))
AssignmentScore = float(input("Assignment Score of a student: "))


prediction = model.predict([[StudyHours, Attendance, PreviousMarks, SleepHours, AssignmentScore]])

print("Predicted Final Marks of student:", prediction[0])      