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
![strings](https://github.com/Lip4ik/arctf/blob/main/forensic/%D0%90%D0%BA%D1%83%D0%BB%D0%B0%20%D0%B2%20%D1%82%D0%B0%D0%BD%D0%BA%D0%B5/solve/flag.jpg)  
Очень сильно бросается в глаза base64 строчка в конце файла, RmxhZzogb3cxUlhCWEFLOE5iaUE4TTlKTGk=  
Ее декондирование приводит к "Flag: ow1RXBXAK8NbiA8M9JLi"
Наш флаг arctf{ow1RXBXAK8NbiA8M9JLi}  
