
# ======================================================
# مشروع: نظام إدارة الطلاب بواجهة رسومية (Tkinter)
# اللغة: Python
# الوصف:
# هذا البرنامج يتيح لك إضافة طلاب (اسم، عمر، درجة)
# وعرضهم من خلال واجهة رسومية بسيطة باستخدام Tkinter
# ======================================================

# استدعاء مكتبة Tkinter للواجهات الرسومية
import tkinter as tk

# استدعاء messagebox لعرض رسائل تنبيه للمستخدم
from tkinter import messagebox


# ----------------------------------
# قائمة لتخزين بيانات الطلاب
# ----------------------------------
students = []


# ----------------------------------
# دالة إضافة طالب
# يتم تشغيلها عند الضغط على زر "إضافة الطالب"
# ----------------------------------
def add_student():
    # أخذ القيم من مربعات الإدخال
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    # التحقق أن جميع الحقول مُدخلة
    if name and age and grade:
        # تخزين بيانات الطالب في قاموس
        student = {
            "name": name,
            "age": age,
            "grade": grade
        }

        # إضافة الطالب للقائمة
        students.append(student)

        # رسالة نجاح
        messagebox.showinfo("نجاح", "تم إضافة الطالب بنجاح ✅")

        # مسح الحقول بعد الإضافة
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_grade.delete(0, tk.END)

    else:
        # رسالة تحذير في حال نقص البيانات
        messagebox.showwarning("تنبيه", "يرجى تعبئة جميع الحقول ⚠️")


# ----------------------------------
# دالة عرض الطلاب
# ----------------------------------
def show_students():
    # التحقق إذا توجد بيانات
    if students:
        info = ""
        for student in students:
            info += (
                f"الاسم: {student['name']} | "
                f"العمر: {student['age']} | "
                f"الدرجة: {student['grade']}\n"
            )

        # عرض البيانات في نافذة منبثقة
        messagebox.showinfo("قائمة الطلاب", info)
    else:
        messagebox.showinfo("قائمة الطلاب", "لا توجد بيانات حالياً ❌")


# ----------------------------------
# إنشاء النافذة الرئيسية
# ----------------------------------
root = tk.Tk()
root.title("نظام إدارة الطلاب")
root.geometry("400x350")


# ----------------------------------
# عنوان البرنامج
# ----------------------------------
label_title = tk.Label(root, text="نظام إدارة الطلاب", font=("Arial", 16, "bold"))
label_title.pack(pady=10)


# ----------------------------------
# حقل اسم الطالب
# ----------------------------------
label_name = tk.Label(root, text="اسم الطالب:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()


# ----------------------------------
# حقل عمر الطالب
# ----------------------------------
label_age = tk.Label(root, text="عمر الطالب:")
label_age.pack()
entry_age = tk.Entry(root)
entry_age.pack()


# ----------------------------------
# حقل درجة الطالب
# ----------------------------------
label_grade = tk.Label(root, text="درجة الطالب:")
label_grade.pack()
entry_grade = tk.Entry(root)
entry_grade.pack()


# ----------------------------------
# زر إضافة الطالب
# ----------------------------------
button_add = tk.Button(root, text="إضافة الطالب", command=add_student)
button_add.pack(pady=10)


# ----------------------------------
# زر عرض الطلاب
# ----------------------------------
button_show = tk.Button(root, text="عرض الطلاب", command=show_students)
button_show.pack()


# ----------------------------------
# تشغيل البرنامج (الواجهة)
# ----------------------------------
root.mainloop()
