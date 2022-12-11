# Буквозмейка
В задании нам дан исполняемый файл, и задача найти картинку  
Попробуем достать всевнутренности из этого файла  
`binwalk --dd='.*' FindPictire.exe`  
Получаем три файла, один из которых наша картинка  
![strings](https://github.com/Lip4ik/arctf/blob/main/reverse/%D0%98%D1%89%D0%B8%20%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D1%83!/solve/_FindPictire.exe.extracted/4000)  
Наш флаг arctf{yfuyZ3YGas60hDUI3exx}  
 
