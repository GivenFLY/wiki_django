**Админка**: admin:admin

### Список имеющихся страниц (GET запрос)  
`localhost/api/articles`  
### Список версий одной страницы (GET запрос)  
`localhost/api/articles/<article_id>/versions`  
`localhost/api/articles/3/versions`  
### Создание страницы (POST запрос)  
`localhost/api/articles?title=<title>&text=<text>`  
`localhost/api/articles?title=title&text=text` 
### Получение любой версии одной страницы (GET запрос)  
`localhost/api/articles/<article_id>/<version_number>`  
`localhost/api/articles/3/2`  
###Получение текущей версии страницы (GET запрос)  
`localhost/api/articles/<article_id>`  
`localhost/api/articles/3`  
### Редактирование страницы (PUT запрос)  
`localhost/api/articles/<article_id>?title=<title>&text=<text>`  
`localhost/api/articles/3?title=title&text=text`  
### Изменение текущей версии (PUT запрос)  
`localhost/api/articles/<article_id>/<version_number>`  
`localhost/api/articles/3/5` 
