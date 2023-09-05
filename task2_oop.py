#Создайте класс МояСтрока где будут
#доступны все варианты str и 
# дополнительно хранится имя автора строк и время создания (time.time)
#Добавьте к задачам с семинара строки документации 
# и методы вывода информации на печать.

from datetime import datetime

class MyStr(str):
    def __new__(cls, value, author):
        """
        Внутри функции new заданы переменные value и author. 
        Это атрибуты экземпляров.
        
        """
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().time().hour
        return instance


ms1 = MyStr('some text', 'Vladislav')
print(ms1, ms1.author)
print(ms1.time)
print(MyStr.__new__.__doc__)