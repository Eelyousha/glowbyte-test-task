#!/bin/bash

# Получаем имя файла и список функций из аргументов командной строки
filename=$1
if [[ ! -f $filename ]]; then
    echo "No such file '$filename'"
    exit 1
fi

shift
functions=("$@")

# Перебираем список функций
for function in "${functions[@]}"
do
    # Используем grep и awk для извлечения времени работы функции из файла лога
    # Считаем среднее и максимальное время работы
    avg_time=$(grep -E "Function $function finished" "$filename" | awk '{sum+=$NF; count++} END{if(count>0) print sum/count}')
    max_time=$(grep -E "Function $function finished" "$filename" | awk '{if($NF>max) max=$NF} END{print max}')

    # Выводим результаты
    echo "Функция: $function"
    echo "Среднее время работы: $avg_time"
    echo "Максимальное время работы: $max_time"
    echo
done
