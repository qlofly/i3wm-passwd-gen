# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random
import pyperclip

chars = '+-/!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
for n in range(1):
    password =''
    for i in range(21):
        password += random.choice(chars)
    print(password)
pyperclip.copy(password)