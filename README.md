# Документация

Код приложения лежит на ветке master

## Необходимые зависимости:

- djangorestframework	3.13.1
- Django	4.0.5	
- mysqlclient	2.1.0	2.1.0

## API

#### Адрес: 

> http://127.0.0.1:8000

#### Конечные точки:

- /tasks/quad

  Параметры запроса (query parameters):
  - a_value(float)
  - b_value(float)
  - c_value(float)
  
  Это значения коэффициентов по формуле __a__*x^2+__b__*x+__c__ = 0
- /tasks/colors/{num}

  Где num - номер предмета (int)
