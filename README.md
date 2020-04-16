# jsonplaceholder_tests
API https://jsonplaceholder.typicode.com/

Возможные варианты:
- добавить позитивный тест на получение конкретного поста (GET)
- добавить негативный тест на получение конкретного поста (GET)
- добавить позитивный тест на добавление нового поста (POST)
- добавить негативный тест на добавление нового поста (POST)
- добавить позитивный тест на получение поста по user_id (GET)
- добавить негативный тест на получение поста по user_id (GET)
- придумать свой тест на любой из доступных методов

В тестах должны использоваться фикстуры (минимум в одном тесте) и параметризация (минимум в одном тесте).
Функции для генерации данных (если таковые нужны) хранить в jsonplaceholder_tests/framework/helper.py.
Должен быть как минимум один чекер, проверяющий не только status_code.
В коде не должно быть стилистических ошибок (максимальная длина строки может быть равна 120), для проверки желательно использовать flake8.
