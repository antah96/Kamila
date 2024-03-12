import re 

def get_phone_number(): 
return input("Введите номер телефона: ") 

def save_in_database(phone): 
""" Сохраняем номер в Базу данных 
И проводим какие-то действия с номером""" 

def get_phone_database(phone): 
""" Какие-то действия с телефонным номером из Базы данных """ 

phone = get_phone_number() 

if re.match(r'^\d{1,2}-\d{3}-\d{2}-\d{2}-\d{2}$', phone): # Проверка формата номера 
print(f"Получен верный номер телефона: {phone}") 
# Здесь могут быть дополнительные действия с номером 
save_in_database(phone) 

else: 
print("Некорректный номер телефона!")
