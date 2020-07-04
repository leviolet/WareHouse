# coding:  utf-8
# author:  leviolet
# license: MIT
# 将普通的变量赋值形式变为流程图的变量赋值形式
# 如 a=1;b=2 -> 1=>a 2=>b
# 分隔符可以是换行或分号

import re
def f(s):
    m = re.split(r"[;\n]",s)  # 分隔符
    m = [x.replace(" ",'') for x in m if x.replace(" ",'')]
    m = [' => '.join(x.split("=")[::-1]) for x in m ]
    print('\n'.join(m))

f('''t = current->next;
current->next = newpoint;
newpoint->next = t;''')