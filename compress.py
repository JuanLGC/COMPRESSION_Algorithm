 # !/usr/bin/python
# coding=utf-8
import re

symbols = {
#   key             :   symbols[key]
    "implementation":   "🌭",
    "practicality"  :   '🍔',
    "better"        :   '🥨',
    "than"          :   '🥙',
    "Although"      :   "🍖",
    "explain"       :   "🥠",
    
}

def compress(content):

    compressed_content = content.replace("implementation", symbols["implementation"])
    compressed_content = compressed_content.replace("practicality", symbols["practicality"])
    compressed_content = compressed_content.replace("better", symbols["better"])
    compressed_content = compressed_content.replace("than", symbols["than"])
    compressed_content = compressed_content.replace("Although", symbols["Although"])
    compressed_content = compressed_content.replace("explain", symbols["explain"])
    
    print(compressed_content)    

    return compressed_content