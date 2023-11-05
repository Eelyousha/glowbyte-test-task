# glowbyte-test-task

## python

### Первая часть

Дан файл config.yaml - структура заранее не известна, знаем только формат.
На основе него необходимо создать дикт.
При обращении по ключу k вместо KeyError этот объект должен поднимать Exception(f"Error in confguraton: no such key {k}")

### Вторая часть

С помощью sqlalchemy реализовать следующий алгоритм:
На вход приходит таблица (attr_name String, attr_value Integer)

Для каждого attr_name необходимо оставить не более 3 строк, причем оставить нужно максимальные значения attr_value

Проставить id и var_id (id соответствует attr_name, var_id соответствует связке attr_name, attr_value)

После рассчитать среднее, минимальное и максимальное значения attr_value для каждого attr_name

На выходе необходимо получить 2 набора данных:
(id UUID, attr_name String, avg_value Float, min_value Integer, max_value Float)

(id UUID, var_id UUID, attr_value)

## bash

Дан лог с сообщениями в формате:

Function f1 started

Function f1 finished. Time: 1.13s

Function f2 started

Function f3 started

Function f3 finished. Time: 2.47s

Function f2 finished. Time: 3.92s

Function f4 started

Function f4 finished. Time: 0.26s

Написать bash скрипт

На вход подаются имя файла и список функций (./script.sh log.log f1 f3)

На выходе вывести среднее и максимальное время работы для каждой из указанных функций
