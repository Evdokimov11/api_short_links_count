# Обрезка ссылок с помощью Битли

Данный проект создан для создания сокращенных ссылок (при участии сайта [bit.ly](https://app.bitly.com)), а также для подсчета количества преходов по сокращенной ссылке.
Для работы с программой вам необходимо передать ссылку в качетсве параметра: 

* При передаче стандартной ссылки в качестве результата работы программы вы получите сокращенную ссылку.

* При передаче сокращенной ссылки в качестве результата работы программы вы получите количество переходов по ней.

Ниже приведен пример работы программы. 

Для создания сокращенной ссылки: 

```
python main.py https://dvmn.org
```

Для подсчета количества переходов по сокращенной ссылки: 

```
python main.py bit.ly/3EYA1DS
```

![2022-12-07_06-55-41](https://user-images.githubusercontent.com/42433463/206076891-f38ee674-0290-4bd9-a1d8-d6ccb9279d68.png)


### Как установить

Для корректной работы программы вам необходимо создать файл .env и записать в него вай API-ключ в следующем формате: BITLY_API_KEY=Ваш_API_ключ

Python3 должен быть уже установлен. 

Также вам необходимо установить соответствующие внешние пакеты. Версии данных пакетов вы можете найти в файле requirements.txt

Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
