Напоминаю, что в тесте 001 мы получили такую таблицу параметров
различных размеров окон width (часть вырезано):

<pre>
width = 11 | max_bits_ = 10 | max_count_ =  45 | compressing =  90.909% |
width = 12 | max_bits_ = 10 | max_count_ =  52 | compressing =  83.333% |
width = 13 | max_bits_ = 11 | max_count_ =  65 | compressing =  84.615% |
width = 14 | max_bits_ = 11 | max_count_ =  74 | compressing =  78.571% |
width = 15 | max_bits_ = 11 | max_count_ =  89 | compressing =  73.333% |
width = 16 | max_bits_ = 11 | max_count_ = 100 | compressing =  68.750% |
width = 32 | max_bits_ <=15 | max_count_ <=1023| compressing <  50.000% |
</pre>

Из таблицы видно, что width=32 позволяет сжать данные за один
проход примерно в два раза и получить 15 бит данных.
Эти 15 бит можно еще сжать с помощью width=15 до 11 бит,
затем width=11 до 10 бит.
Итоговый коэффициент сжатия получается равен 32/10 = 3.2

2024_08_02  
Алексей Белянин  
https://t.me/AlekseyBelyanin  
xayam@yandex.ru  
