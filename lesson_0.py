a = 1 # int
b = 5.5 # float
c = True # bool = 1
d = False # bool = 0
print (id(a)) # выводит ID переменной, типа место хранения
a = 1 + 3
print (id(a)) # ID изменился
name = "Alex" # strok type кавычки могут быть одинарные и двойные
last_name = 'Martyn'
company = '"Alliance"'
print(name + ' ' + last_name + ' ' + company)

company_list = ["Alliance",
                "Master",
                "User"] # список в квадратных скобках, изменяемый,
# но требует больще опер памяти чем тапл
print ('before change', company_list)
print (id(company_list))
company_list[0] = 'Union' # заменили первое (0) значение в списке
print ('after change', company_list)
print (id(company_list)) # после замены переменной ID не изменился
print(company_list [0]) # список начинается с 0
print(company_list [-3])
print(company_list [-1]) # -1 это последний
print(name [0]) # строковое значение это тоже список
company_tuple = ("Alliance",
                 "Master",
                 "User") # tuple это кортеж, изменить по индексу нельзя
company_dict = {'name': "Alliance",
                'adress': 'Korolev, Pionerskaya, 3',
                'employers': 20,
                'active' : True}
print(company_dict)
company_dict['name'] = 'Tesla' # заменено название в словаре
print(company_dict)
company_dict['employers'] -=1 # типа уволился 1 сотрудник (-1)
print(company_dict)
company_list = [company_dict,
               company_dict,
               company_dict]
print(company_list)
company_list[0]['name'] = 'Ford' # изменилось название у всех словарей,
# тк они одни и те же
print(company_list)
