#!/usr/bin/python3
#! --*-- coding:utf-8 --*--
import os
import shutil
import subprocess
import argparse


def generate_data(datasets_dir):
    """
    遍历datasets_dir目录下所有的子目录，对于每个子目录，
    如果子目录中存在make_dataset.py文件，则运行该文件，
    并在成功或失败时打印相应的消息。
    
    Args:
        datasets_dir (str): 数据集目录的路径。
    
    Returns:
        None
    
    """
    for subdir in os.listdir(datasets_dir):
        subdir_path = os.path.join(datasets_dir, subdir)

        if os.path.isdir(subdir_path):
            script_path = os.path.join(subdir_path, "make_dataset.py")

            if os.path.isfile(script_path):
                try:
                    subprocess.run(["python", script_path], check=True)
                    print(f"Success make_dataset.py in {subdir_path}")
                except:
                    print(f"Fail make_dataset.py in {subdir_path}")
            else:
                print(f"*******No make_dataset.py in {subdir_path}*******")


def del_data(datasets_dir):
    """
    删除datasets_dir目录下所有名为"data"的文件夹中的第一个.jsonl文件及其所在文件夹。
    
    Args:
        datasets_dir (str): 数据集目录路径
    
    Returns:
        None
    
    """
    for root, dirs, files in os.walk(datasets_dir):
        if "data" in dirs:
            data_dir_path = os.path.join(root, "data")
            for file in os.listdir(data_dir_path):
                if file.endswith(".jsonl"):
                    shutil.rmtree(data_dir_path)
                    print(f"success delete data folder {data_dir_path}")
                    break

def get_args():
    """
    解析命令行参数。
    命令行参数定义了 --generate 和 --delete 两个参数，用户生成测试数据集和删除测试数据集。
    
    Args:
        无
    
    Returns:
        argparse.Namespace: 包含解析后的命令行参数的命名空间对象
    
    """
    parser = argparse.ArgumentParser(description="Process datasets")
    parser.add_argument("--generate", "-g", action="store_true", help="generate data")
    parser.add_argument("--delete", "-d", action="store_true", help="delete data")
    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    args = get_args()
    datasets_dir = "datasets"
    if args.generate:
        generate_data("datasets")
        print("Success generate data")
        exit(0)
        
    if args.delete:
        del_data("datasets")
        print("Success delete data")
        exit(0)
