import os

def search_file_in_directory(directory, target_file):
    for root, dirs, files in os.walk(directory):
        if target_file in files:
            return os.path.join(root, target_file)
    return None

# 使用示例
file_path = search_file_in_directory(r'\\192.168.10.253\nas\品牌部素材\产品', r'ND180926-7N+GG.jpg')
print(file_path)
