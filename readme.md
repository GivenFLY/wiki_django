**Админка**: admin:admin

* Список имеющихся страниц
`localhost/api/articles` GET
* Список версий одной страницы
`localhost/api/articles/<article_id>/versions` GET
`localhost/api/articles/3/versions` 
* Создание страницы
`localhost/api/articles?title=<title>&text=<text>` POST
`localhost/api/articles?title=title&text=text` 
* Получение любой версии одной страницы
`localhost/api/articles/<article_id>/<version_number>` GET
`localhost/api/articles/3/2`
* Получение текущей версии страницы
`localhost/api/articles/<article_id>` GET
`localhost/api/articles/3`
* Редактирование страницы
`localhost/api/articles/<article_id>?title=<title>&text=<text>` PUT
`localhost/api/articles/3?title=title&text=text`
* Изменение текущей версии
`localhost/api/articles/<article_id>/<version_number>` PUT
`localhost/api/articles/3/5` 