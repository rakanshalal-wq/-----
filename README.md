# ======================================================
# مشروع: نظام إدارة الطلاب بواجهة رسومية (Tkinter)
# اللغة: Python
# ======================================================

import tkinter as tk
from tkinter import messagebox

# قائمة لتخزين الطلاب
students = []

# -----------------------------
# دالة إضافة طالب
# -----------------------------
def add_student():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    grade = entry_grade.get().strip()

    if not name or not age or not grade:
        messagebox.showwarning("تنبيه", "يرجى تعبئة جميع الحقول")
        return

    if not age.isdigit() or not grade.isdigit():
        messagebox.showerror("خطأ", "العمر والدرجة يجب أن يكونا أرقامًا")
        return

    student = {
        "name": name,
        "age": int(age),
        "grade": int(grade)
    }

    students.append(student)

    messagebox.showinfo("تم", "تمت إضافة الطالب بنجاح")

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

# -----------------------------
# دالة عرض الطلاب
# -----------------------------
def show_students():
    if not students:
        messagebox.showinfo("الطلاب", "لا يوجد طلاب مضافين")
        return

    output = ""
    for i, s in enumerate(students, start=1):
        output += f"{i}- الاسم: {s['name']} | العمر: {s['age']} | الدرجة: {s['grade']}\n"

    messagebox.showinfo("قائمة الطلاب", output)

# -----------------------------
# إنشاء الواجهة
# -----------------------------
root = tk.Tk()
root.title("برنامج تخزين الطلاب والدرجات")
root.geometry("350x250")

frame = tk.Frame(root)
frame.pack(pady=15)

# الاسم
tk.Label(frame, text="اسم الطالب").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, width=25)
entry_name.grid(row=0, column=1, pady=5)

# العمر
tk.Label(frame, text="العمر").grid(row=1, column=0, sticky="w")
entry_age = tk.Entry(frame, width=25)
entry_age.grid(row=1, column=1, pady=5)

# الدرجة
tk.Label(frame, text="الدرجة").grid(row=2, column=0, sticky="w")
entry_grade = tk.Entry(frame, width=25)
entry_grade.grid(row=2, column=1, pady=5)

# الأزرار
tk.Button(frame, text="إضافة الطالب", command=add_student).grid(
    row=3, column=0, columnspan=2, pady=10
)

tk.Button(frame, text="عرض الطلاب", command=show_students).grid(
    row=4, column=0, columnspan=2
)

# تشغيل البرنامج
root.mainloop()
