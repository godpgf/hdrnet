import os
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor
import socket
socket.setdefaulttimeout(300)
import sys
input_path = "sample_data/identity/input"
# output_path = "sample_data/identity/output"
output_path = "E:\high_fr"
pic_type = "tiff16_c"


def download_file(name):
    URL = 'https://data.csail.mit.edu/graphics/fivek/img/%s/' % pic_type + name + '.tif'  # 下载由C所调整的图像(可根据需要下载其它的四类图像)

    # urlretrieve 函数的回调函数，显示下载进度

    def cbk(a, b, c):
        '''回调函数
        @a:已经下载的数据包数量
        @b:数据块的大小
        @c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        # 在终端更新进度
        sys.stdout.write("progress: %.2f%%   \r" % (per))
        sys.stdout.flush()

    urlretrieve(URL, output_path + '/' + name + '.tif', cbk)  # 将所获取的图片存储到本地的地址内


if __name__ == "__main__":
    exclued_file_name_list = os.listdir(output_path)
    exclude_file_name_set = set()
    for file_name in exclued_file_name_list:
        file_path = output_path + '/' + file_name
        if os.path.isfile(file_path):
            exclude_file_name_set.add(file_name.split('.')[0])

    file_name_list = os.listdir(input_path)
    with ThreadPoolExecutor(8) as executor:
        for file_name in file_name_list:
            file_path = input_path + '/' + file_name
            file_name = file_name.split('.')[0]
            if os.path.isfile(file_path) and file_name not in exclude_file_name_set:
                print('Downloading ' + file_name + ':')
                executor.submit(download_file, file_name)
