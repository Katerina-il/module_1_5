immutable_var=7, 9, 13, "Число"
print(type(immutable_var))
print(immutable_var) # Выполните операции вывода кортежа immutable_var на экран
# immutable_var[1]=2  кортеж не поддерживает изменение по элементам
# print(immutable_var)
mutable_list=[1, 3, 7, 15, "Favorite"]
print(mutable_list)
print(type(mutable_list))
mutable_list[1]="whim" # Измените элементы списка
print(mutable_list) #  Выведите на экран измененный список mutable_list.