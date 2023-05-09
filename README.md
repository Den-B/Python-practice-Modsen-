Инструкция по поднятию сенрвиса.

1) Сервис использует фреймворк Flask. Установка данного фреймворка через pip.
2) Использует nosql базу данных MongoDB. Должен быть доступ к данной бд. Это должна быть распределнная база данных или, как в примере, устанновленная и запущенная на самой рабочей машине.
3) Сервис использует elastic search. Вы должны иметь доступ к этой утилите, то есть она должна быть запущена и настроена либо на рабочей машине, либо удаленно. Настроить авторизацию пользователя, например, здесь используется superuser с паролем superuser и доступом superuser.
4) При необходимости вызвать методы для чтения из csv файла в базу данных и для создания индекса. За это отвечают два скрипта:
    - readFromCsv <filepath>. Запускаем, передавая путь к файлу(можено относительный). Он запишет в базу данных всё необходимое.
    - createElasticSearchIndex. Запускаем для создания индекса.
5) Запуск главного файла main.py, который подтянет сервер, используя стандартные настройки, например, константы в файле constants.py.