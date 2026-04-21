```python.exe test_001_choice_of_width.py```  

Output:  
<pre>
Input WIDTH, default 0 for infinity process:  
[INFO] | WIDTH set to 0  
SKIP: False |   100.0% | width =  1 | max_bits_ =  1 | max_count_ =   0 | compressing = 100.000% |  
SKIP: False |   100.0% | width =  2 | max_bits_ =  2 | max_count_ =   1 | compressing = 100.000% |  
SKIP: False |   100.0% | width =  3 | max_bits_ =  4 | max_count_ =   2 | compressing = 133.330% |  
SKIP: False |   100.0% | width =  4 | max_bits_ =  5 | max_count_ =   4 | compressing = 125.000% |  
SKIP: False |   100.0% | width =  5 | max_bits_ =  6 | max_count_ =   7 | compressing = 120.000% |  
SKIP: False |   100.0% | width =  6 | max_bits_ =  7 | max_count_ =  10 | compressing = 116.660% |  
SKIP: False |   100.0% | width =  7 | max_bits_ =  8 | max_count_ =  16 | compressing = 114.280% |  
SKIP: False |   100.0% | width =  8 | max_bits_ =  8 | max_count_ =  20 | compressing = 100.000% |  
SKIP: False |   100.0% | width =  9 | max_bits_ =  9 | max_count_ =  29 | compressing = 100.000% |  
SKIP: False |   100.0% | width = 10 | max_bits_ = 10 | max_count_ =  34 | compressing = 100.000% |  
FIRST POSITION FOR COMPRESSING 
True  |   100.0% | width = 11 | max_bits_ = 10 | max_count_ =  45 | compressing =  90.909% |  
True  |   100.0% | width = 12 | max_bits_ = 10 | max_count_ =  52 | compressing =  83.333% |  
True  |   100.0% | width = 13 | max_bits_ = 11 | max_count_ =  65 | compressing =  84.615% |  
True  |   100.0% | width = 14 | max_bits_ = 11 | max_count_ =  74 | compressing =  78.571% |  
True  |   100.0% | width = 15 | max_bits_ = 11 | max_count_ =  89 | compressing =  73.333% |  
True  |   100.0% | width = 16 | max_bits_ = 11 | max_count_ = 100 | compressing =  68.750% |  
...  
True  |   100.0% | width = 32 | max_bits_ <=15 | max_count_ <=1023| compressing <  50.000% |  
...  
</pre>

Собственно из-за своих параметров ширина окна width=32 
является самой лучшей на данный момент.


2024_08_02  
Алексей Белянин  
https://t.me/AlekseyBelyanin  
xayam@yandex.ru  
