import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Автоматизация рефлексии")
root.geometry("810x650")

# Создаем текстовый виджет для шаблона

child_name = tk.Label(root, text="Введите имя ребенка.")
child_name.pack(anchor="center")


name_of_children = tk.Entry(root, width=20)
name_of_children.pack(anchor="center")


text_widget = tk.Text(root, height=16, width=100)
text_widget.pack(pady=10)


# Шаблонный текст
template_text_part1 = "На сегодняшнем уроке мы повторили "
template_text_part2 = ". Основной учебной целью урока была "
template_text_part3 = ". Мы смогли \n разобрать такие понятия, как "
template_text_part4 = ", они довольно сложные для понимания ребенка, но тем не менее "
template_text_part5 = "[Имя ребенка] очень старался, мы в дальнейшем продолжим с ними работать и закреплять материал.\n\n Сегодня мы сделали: "
template_text_part6 = "\n[Имя ребенка] отлично справился с заданиями, например, "
template_text_part7 = ". Тем не менее, тему "
template_text_part8 = " нам\n нужно будет дополнительно отработать с помощью домашнего задания и будущих практических проектах.\n\n На следующем уроке мы будем разбирать "
template_text_part9 = ". Это важная тема для понимания будущих сложных\n концепций, и ее освоение заложит хороший фундамент для дальнейшего обучения.\n\n"
template_text_part10 = "[Имя ребенка] проявил большую заинтересованность и усердие на уроке. Если у вас есть вопросы или\n пожелания, пожалуйста, не стесняйтесь связаться со мной или менеджерами школы."

# Вставляем первую часть текста
text_widget.insert(tk.END, template_text_part1)

# Создаем первое поле для ввода
entry1 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry1)  # Вставляем поле ввода в текст

# Вставляем вторую часть текста
text_widget.insert(tk.END, template_text_part2)

# Создаем второе поле для ввода
entry2 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry2)  # Вставляем второе поле ввода в текст

# Вставляем третью часть текста
text_widget.insert(tk.END, template_text_part3)

# My changes

entry3 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry3)  

text_widget.insert(tk.END, template_text_part4)

text_widget.insert(tk.END, template_text_part5)

entry5 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry5)

text_widget.insert(tk.END, template_text_part6)

entry7 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry7)  

text_widget.insert(tk.END, template_text_part7)

entry8 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry8)  

text_widget.insert(tk.END, template_text_part8)

entry9 = tk.Entry(root, width=10)
text_widget.window_create(tk.END, window=entry9)  

text_widget.insert(tk.END, template_text_part9)

text_widget.insert(tk.END, template_text_part10)



# Отключаем возможность редактирования шаблонного текста
text_widget.config(state=tk.DISABLED)

# Переменная для хранения выбранного пола
gender = tk.StringVar(value="Мужской")

# Функция для обновления текста с введенными словами
def update_text():
    word1 = entry1.get()
    word2 = entry2.get()
    word3 = entry3.get()
    word5 = entry5.get()
    word7 = entry7.get()
    word8 = entry8.get()
    word9 = entry9.get()
    name_of_child = name_of_children.get()

    
    # Определяем окончания в зависимости от пола
    if gender.get() == "Мужской":
        a = "старался"
        b = "справился"
        c = "проявил"
    else:
        a = "старалась"
        b = "справилась"
        c = "проявила"
    
    # Формируем новый текст
    new_text = f"""На сегодняшнем уроке мы повторили {word1}. Основной учебной целью урока была {word2}. Мы смогли разобрать такие понятия, как {word3}, они довольно сложные для понимания ребенка, но тем не менее {name_of_child} очень {a}, мы в дальнейшем продолжим с ними работать и закреплять материал.\n
Сегодня мы сделали:
{word5}
{name_of_child} отлично {b} с заданиями, например, {word7}. Тем не менее, тему {word8} нам нужно будет дополнительно отработать с помощью домашнего задания и будущих практических проектах.\n
На следующем уроке мы будем разбирать {word9}. Это важная тема для понимания будущих сложных концепций, и ее освоение заложит хороший фундамент для дальнейшего обучения.\n
{name_of_child} {c} большую заинтересованность и усердие на уроке. Если у вас есть вопросы или пожелания, пожалуйста, не стесняйтесь связаться со мной или менеджерами школы."""
    
    # Очищаем текстовый виджет для результата
    result_text_widget.config(state=tk.NORMAL)
    result_text_widget.delete(1.0, tk.END)
    
    # Вставляем новый текст
    result_text_widget.insert(tk.END, new_text)
    
    # Блокируем редактирование текста
    result_text_widget.config(state=tk.DISABLED)
    print(name_of_children)

# Кнопка для обновления текста
submit_button = tk.Button(root, text="Обновить текст", command=update_text)
submit_button.pack(pady=10)

# Радиокнопки для выбора пола
gender_frame = tk.Frame(root)
gender_frame.pack(pady=5)

gender_label = tk.Label(gender_frame, text="Выберите пол:")
gender_label.grid(row=0, column=0, padx=5)

male_radio = tk.Radiobutton(gender_frame, text="Мужской", variable=gender, value="Мужской")
male_radio.grid(row=0, column=1, padx=5)

female_radio = tk.Radiobutton(gender_frame, text="Женский", variable=gender, value="Женский")
female_radio.grid(row=0, column=2, padx=5)

# Создаем текстовый виджет для отображения результата, чтобы можно было скопировать текст
result_text_widget = tk.Text(root, height=16, width=100, wrap='word')
result_text_widget.pack(pady=10)
result_text_widget.insert(tk.END, "Здесь появится обновленный текст.")
result_text_widget.config(state=tk.DISABLED)  # Блокируем редактирование текста

# Запуск главного цикла программы
root.mainloop()
