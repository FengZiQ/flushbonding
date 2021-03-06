# coding = utf-8
import time
from configFile import configuration


def to_log(str_info, file=configuration['filePath'] + 'testLog.log'):

    with open(file, "r+", encoding='UTF-8', errors='ignore') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ": " + str_info + '\n' + content
        )
        f.close()
    print(str_info)




