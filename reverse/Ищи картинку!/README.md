# Буквозмейка
В задании нам дан исполняемый файл, и задача найти картинку  
Попробуем достать всевнутренности из этого файла  
`binwalk --dd='.*' FindPictire.exe`  
Получаем три файла, один из которых наша картинка  
![strings](https://github.com/Lip4ik/arctf/blob/main/misc/%D0%A1%D1%82%D0%B5%D0%B3%D0%B0%D0%BD%D0%BE%D0%BF%D0%BE%D0%BD%D0%B3/solve/data.jpg)  
Наш флаг arctf{yfuyZ3YGas60hDUI3exx}  
 
