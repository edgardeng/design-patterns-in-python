import datetime
import os
import re

def rename(dir, filename, time, fmt):
    u = int(time) // 1000
    t = datetime.datetime.fromtimestamp(u)
    s = t.strftime('%Y-%m-%d_%H_%M')
    os.rename(os.path.join(dir,filename), os.path.join(dir,s+fmt))


if __name__ == '__main__':
    fold = r'/Users/edgar/Movies/Videos'
    files = os.listdir(fold)
    for filename in files:
        result = re.findall('\d+', filename)
        fmt = filename[filename.find('.'):]
        if result:
            print(filename, result[0], fmt)
            rename(fold,filename,result[0], fmt)
