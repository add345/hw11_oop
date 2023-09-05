#создайте класс Архив, который хранит пару свойствю 
# Например,  число и строку/ 
# При новом экзмпляре класса старые данные  из ранее созданных экземпляров сохраняются в пару списокв
#архивов,которые также являются свойствами экземпляров
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Archive:
    """is archive"""
    instance = None
    def __init__(self, text, number):
        """
        Внутри класса создана "магическая" функция __init__.
        Заданы переменные text и number. 
    """
        
        self.text = text
        self.number = number
    def __new__(cls, text, numb):
        if cls.instance:
            cls.instance.arch_txt.append(cls.instance.text)
            cls.instance.arch_numb.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.arch_txt = []
            cls.instance.arch_numb = []
        return cls.instance
    

a1 = Archive('qwerty', 32)
a2 = Archive('uiop', 23)
print(a2.instance.arch_txt, a2.instance.arch_numb)
print(Archive.__doc__)
print(Archive.__init__.__doc__)