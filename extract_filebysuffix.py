import os
import shutil
import pprint

def extract_images(source_folder, destination_folder):
    # 确保目标文件夹存在
    os.makedirs(destination_folder, exist_ok=True)
    
    # 设定图片扩展名
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')

    for source_folder in source_folders:
        pprint.pp(f"source_folder:{source_folder}")
        for root, _, files in os.walk(source_folder):
            pprint.pp(f"root:{root}, _:{_}, files:{files}")
            for filename in files:
                if filename.lower().endswith(image_extensions):
                    pprint.pp(f"filename:{filename}")
                    # 构造源文件的完整路径
                    source_file = os.path.join(root, filename)
                    # 复制文件到目标文件夹
                    shutil.copy(source_file, destination_folder)

# 使用示例
# extract_images(['C:/path/to/source_folder1', 'C:/path/to/source_folder2'], 'C:/path/to/destination_folder')
source_folders = [r'\\192.168.10.253\nas\品牌部素材\产品\19产品',
                  r'\\192.168.10.253\nas\品牌部素材\产品\20产品',r'\\192.168.10.253\nas\品牌部素材\产品\21产品',r'\\192.168.10.253\nas\品牌部素材\产品\22产品',
                  r'\\192.168.10.253\nas\品牌部素材\产品\23产品']

destination_folder = r'D:\胡图图\素材\公司素材'

extract_images(source_folders, destination_folder)
