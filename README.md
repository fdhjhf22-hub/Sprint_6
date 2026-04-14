\# Проект автотестов для сервиса «Яндекс.Самокат»



\## Описание

UI-тесты для сайта qa-scooter.praktikum-services.ru.  

Проверяются: выпадающий список «Вопросы о важном», позитивные сценарии заказа самоката (верхняя и нижняя кнопки), переходы по логотипам.



\## Технологии

\- Python 3.9+

\- Selenium WebDriver

\- pytest

\- Allure

\- Firefox + geckodriver



\## Установка и запуск

1\. Клонировать репозиторий

2\. Установить зависимости: `pip install -r requirements.txt`

3\. Запустить тесты: `pytest --alluredir=allure\_results`

4\. Сгенерировать отчёт Allure: `allure serve allure\_results`

