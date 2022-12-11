# Стеганопонг
Название задание намекает на стеганографию, один из наиболее популярных методов это LSB  
Воспользуемся утилитой stegsolve чтобы посмотреть на незначимые биты картинки  
![strings](https://github.com/Lip4ik/arctf/blob/main/forensic/%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BD%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20MFT/solve/strings.jpg)  
Наблюдаем неестественное изменение в 0 и 1 бите в правом верхнем углу на всех трех каналах  
Достанем эти данные  
![strings](https://github.com/Lip4ik/arctf/blob/main/forensic/%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BD%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20MFT/solve/strings.jpg)  
Наш флаг arctf{07d890f363b8106595203af9cd56cedd}  
  
P.S. Автору райтапа не понравилось перебивать эти символы, ибо Я смог это сделать лишь раза с третьего  
P.S.S. Прошу в будущем в таких заданиях делать leet читаемый флаг  
