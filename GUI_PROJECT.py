import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

#dataset
data = pd.read_csv("student_data.csv")

X = data[["StudyHours", "Attendance", "PreviousMarks", "SleepHours", "AssignmentScore"]]
y = data["FinalMarks"]

model = LinearRegression()
model.fit(X, y)



def show_graph(study, predicted):
    x = data["StudyHours"]
    y = data["FinalMarks"]

    plt.figure()
    plt.scatter(x, y)
    plt.scatter(study, predicted, marker='x', s=120)

    plt.xlabel("Study Hours")
    plt.ylabel("Final Marks")
    plt.title("Study Hours vs Marks")
    plt.grid()
    plt.show()



def draw_lifestyle_bar(study, sleep):
    canvas.delete("all")

    total = 24
    bar_width = 360
    x_start = 20
    y = 50

    study_w = (study / total) * bar_width
    sleep_w = (sleep / total) * bar_width
    remaining_w = bar_width - study_w - sleep_w

    canvas.create_rectangle(x_start, y, x_start + study_w, y + 35, fill="#34dbdb")
    canvas.create_text(x_start + study_w/2, y + 18, text="Study", fill="white")

    canvas.create_rectangle(x_start + study_w, y, x_start + study_w + sleep_w, y + 35, fill="#2ecc60")
    canvas.create_text(x_start + study_w + sleep_w/2, y + 18, text="Sleep", fill="white")

    canvas.create_rectangle(x_start + study_w + sleep_w, y,
                            x_start + bar_width, y + 35, fill="#bdc3c7")
    canvas.create_text(x_start + bar_width - remaining_w/2, y + 18, text="Other", fill="black")

    canvas.create_text(200, 110,
                       text="24-Hour Daily Distribution",
                       font=("Arial", 11, "bold"))


def show_result(result):
    if result > 75:
        text = f"Predicted Marks: {result:.2f} (Excellent)"
        color = "green"
    elif result > 50:
        text = f"Predicted Marks: {result:.2f} (Average)"
        color = "orange"
    else:
        text = f"Predicted Marks: {result:.2f} (Needs Improvement)"
        color = "red"

    label_result.config(text=text, fg=color)



def predict_marks():
    try:
        StudyHours = float(entry_hours.get())
        Attendance = float(entry_attendance.get())
        PreviousMarks = float(entry_prev.get())
        SleepHours = float(entry_sleep.get())
        AssignmentScore = float(entry_assign.get())

        prediction = model.predict([[StudyHours, Attendance, PreviousMarks, SleepHours, AssignmentScore]])
        result = prediction[0]

        label_result.config(text="Calculating...", fg="black")
        root.after(500, lambda: show_result(result))

        draw_lifestyle_bar(StudyHours, SleepHours)
        show_graph(StudyHours, result)

    except:
        label_result.config(text="Enter valid numbers!", fg="red")




root = tk.Tk()
root.title("Student Performance Predictor")
root.geometry("1000x550")
root.config(bg="#ecf0f1")


left_frame = tk.Frame(root, width=400, bg="#f7f4f4")
left_frame.pack(side="left", fill="y")


right_frame = tk.Frame(root, bg="#ecf0f1")
right_frame.pack(side="right", fill="both", expand=True)




try:
    image = Image.open("student.png")

    
    new_width = 380
    aspect_ratio = image.height / image.width
    new_height = int(new_width * aspect_ratio)

    
    new_height = int(new_height * 0.95)

    image = image.resize((new_width, new_height))

    img = ImageTk.PhotoImage(image)

    


    tk.Label(left_frame, image=img, bg="#f4f6f7").pack(padx=40, pady=60)

except:
    tk.Label(left_frame, text="Image not found", bg="#f4f6f7").pack()



tk.Label(right_frame, text="Enter Student Details",
         font=("Arial", 22, "bold"),
         bg="#ecf0f1", fg="#2c3e50").pack(pady=20)


form_frame = tk.Frame(right_frame, bg="#ecf0f1")
form_frame.pack(pady=10)

def create_input(label):
    tk.Label(form_frame, text=label,
             font=("Arial", 13, "bold"),
             bg="#ecf0f1", fg="#2c3e50").pack(pady=5)

    entry = tk.Entry(form_frame,
                     font=("Arial", 13),
                     width=30,
                     bd=2,
                     relief="groove")
    entry.pack(pady=5)

    return entry

entry_hours = create_input("Study Hours")
entry_attendance = create_input("Attendance (%)")
entry_prev = create_input("Previous Marks")
entry_sleep = create_input("Sleep Hours")
entry_assign = create_input("Assignment Score")


tk.Button(right_frame, text="Predict",
          font=("Arial", 14, "bold"),
          bg="#2980b9", fg="white",
          width=18,
          command=predict_marks).pack(pady=20)



label_result = tk.Label(right_frame, text="",
                        font=("Arial", 16, "bold"),
                        bg="#ecf0f1")
label_result.pack(pady=10)



canvas = tk.Canvas(right_frame,
                   width=420,
                   height=160,
                   bg="#ecf0f1",
                   highlightthickness=0)
canvas.pack(pady=20)

root.mainloop()