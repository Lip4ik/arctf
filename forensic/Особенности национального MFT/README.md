# Особенности национального MFT 
С целью экономии памяти не буду загружать исходники  
Перед решением таска мы видем что-то про MFT и что нужно найти строчку формата base64  
Однако дан нам лишь зашифрованный архив, необходимо его вскрыть  
Воспользуемся утилитой john-the-ripper  
`zip2john Forensics400_ctf.zip > zip.hash`  
Получим хэш пароля от этого архива и сломаем его  
`john zip.hash`
И получим пароль "ctf" от файла MFT  
Одно из самых главных правил ctf, если есть файл его нужно strings-нуть  
`strings db`  
![strings](https://github.com/Lip4ik/arctf/blob/main/forensic/%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BD%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20MFT/solve/strings.jpg)  
Очень сильно бросается в глаза base64 строчка в конце файла, RmxhZzogb3cxUlhCWEFLOE5iaUE4TTlKTGk=  
Ее декондирование приводит к "Flag: ow1RXBXAK8NbiA8M9JLi"  
Наш флаг arctf{ow1RXBXAK8NbiA8M9JLi}  
