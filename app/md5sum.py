"""
author      : zhancc
filename    : md5sum.py
date        : 2020/06/09 16:24:56
description : 计算文件的MD5值，在当前目录生成md5.txt;
              查找某个目录下的所有特定格式文件，在同目录下生成md5.txt。
"""

import os
import codecs
import hashlib
import argparse


def md5sum(file_path: str):
    """
    计算文件的MD5
    :param file_path: str
    :return: str
    """
    if not os.path.exists(file_path):
        raise FileExistsError("{0} cannot be found".format(file_path))
    if not os.path.isfile(file_path):
        raise TypeError("{0} is not a file".format(file_path))
    sh = hashlib.md5()
    with open(file_path, "rb") as fp:
        buff = b""
        while True:
            buff = fp.read(4096)
            if buff:
                sh.update(buff)
            else:
                break
    return sh.hexdigest()


def output_to_file(file_path: str, md5_dict: dict):
    """
    将MD5值和文件名输出到同级目录的md5.txt中
    :param file_path:
    :param md5_dict:
    :return:
    """
    with codecs.open(file_path, "w", "utf-8") as fp:
        for key in md5_dict:
            md5_string = "{0}  {1}".format(key, md5_dict.get(key))
            fp.write(md5_string + "\n")
            print(md5_string)


def find_files(directory: str, formats: tuple = ("sql",)):
    """
    递归查找特定格式的文件
    :param directory: str
    :param formats: list
    :return: str
    """
    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            if item.split(".")[-1] in formats:
                base_dir = "\\".join(path.split("\\")[:-1])
                md5_path = os.path.join(base_dir, "md5.txt")
                output_to_file(md5_path, {item: md5sum(path)})
            else:
                pass
        elif os.path.isdir(path):
            find_files(path, formats)


def get_options():
    parser = argparse.ArgumentParser(
        prog="md5sum", description="", prefix_chars="-",
        add_help=True, allow_abbrev=True, usage="""
        python md5sum.py -d directory1 directory2 -t sql
        python md5sum.py -f game1.sql game2.sql"""
    )
    parser.add_argument("-f", "--file", dest="files", nargs="+", help="file to md5sum")
    parser.add_argument("-d", "--dir", dest="dir", nargs="+", help="dir to md5sum")
    parser.add_argument("-t", "--type", dest="type", nargs="+", default="sql", help="default=sql")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_options()
    formats = args.type if args.type else []
    if args.dir:
        for directory in args.dir:
            find_files(directory, formats)
    if args.files:
        md5_dict = dict()
        for file in args.files:
            if not os.path.exists(file):
                raise FileExistsError("{0} cannot be found".format(file))
            md5_value = md5sum(file)
            md5_dict.update({md5_value: file})
            output_to_file("md5.txt", md5_dict)

