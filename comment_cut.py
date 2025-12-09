import os
import glob
import pandas as pd
import re

dir_path = "./static/images/img/game/"
file_list = glob.glob(os.path.join(dir_path, "*.js"))
for file_path in file_list:
    print("file:"+file_path)
    f = open(file_path,encoding='UTF-8')
    text = f.read()
    f.close()
    f = open(file_path,'w',encoding='UTF-8')
    new_text = re.sub("/\*[\s\S]*?\*/", "", text)
    f.write(new_text)
    f.close()

