# coding = utf-8
import time
from configFile import configuration


def to_log(str_info):

    with open(configuration['filePath'] + 'testLog.log', "r+", encoding='UTF-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ": " + str_info + '\n' + content
        )
        f.close()
    print(str_info)




