from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk


def dalee():
    global page, text, r1, r2, r3, count, string
    lvl = lvl_var.get()
    responses.append(lvl)
    page += 1
    if btn['text'] == 'Результат':
        if page == 4:
            lvl = lvl_var.get()
            responses.append(lvl)
            page += 1
        for i in range(len(success)):
            if success[i] == responses[i]:
                count += 1
        if count == 0:
            string = 'Вы полный долбоёб (тупее ебучего камня блять).\nСделайте хоть что-то полезное - сдохните нахуй.'
        if count == 1:
            string = 'Вы очень тупой человек (тупее ёбаной обезьяны).\nВам следовало хотя бы окончить первый блять класc.'
        if count == 2:
            string = 'Вы показываете признаки умственного развития.\nНо вы всё равно очень тупой человек (долбоёб).'
        if count == 3:
            string = 'Вы человек со средним интеллектом.Скорее всего\nвы не состоите в "ЧВК Редан" (Не ебанат).'
        if count == 4:
            string = 'Вы умнее большинства людей на планете.\nДостойно уважения (Нормальный человек).'
        if count == 5:
            string = 'Ебать ты молодец. Я просто в ахуе...'
        r1.destroy()
        r2.destroy()
        r3.destroy()
        text.destroy()
        btn.destroy()
        t1 = ttk.Label(text=f'Результат: {count}/5', font='Arial 20 bold')
        t1.pack(pady=20, ipady=2)
        t2 = ttk.Label(text=string, font='Arial 12 bold')
        t2.pack(pady=10)
    else:

        if page == 1:
            text.config(text='Число π равно:')
            r1.config(text='3.879565214324242')
            r2.config(text='3.141592653589793')
            r3.config(text='2.718281828459045')
        elif page == 2:
            text.config(text='В каком месяце 28 дней:')
            r1.config(text='Во всех')
            r2.config(text='В мае')
            r3.config(text='В феврале')
        elif page == 3:
            text.config(text='2 + 2 * 2 = ')
            r1.config(text='4')
            r2.config(text='6')
            r3.config(text='8')
        elif page == 4:
            text.config(text='Назовите формулу спирта: ')
            r1.config(text='С₂H₅OH')
            r2.config(text='H₂O')
            r3.config(text='C₁₁H₁₅NO')
            btn.config(text='Результат')


root = ThemedTk(theme='yaru')
root.geometry('460x180')
root.title('Тест на дауна')
root.resizable(False, False)
responses = []
success = [2, 1, 0, 1, 0]
page = 0
count = 0
text = ttk.Label(text='Какого цвета трава:', font='Arial 20 bold')
text.pack(pady=10)
string = ''
lvl_var = IntVar()
r1 = ttk.Radiobutton(text='Красная', variable=lvl_var, value=0)
r2 = ttk.Radiobutton(text='Синяя', variable=lvl_var, value=1)
r3 = ttk.Radiobutton(text='Зелёная', variable=lvl_var, value=2)
r1.pack()
r2.pack()
r3.pack()
btn = ttk.Button(text='Далее', command=lambda: dalee())
btn.pack(pady=10)
root.mainloop()
