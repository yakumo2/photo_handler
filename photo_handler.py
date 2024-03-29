import os
from tqdm import tqdm
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

# 压缩图片并保存
def compress_image(input_path, output_path, quality=60, max_size=400):
    try:
        # 如果输出文件已存在，则跳过压缩
        if os.path.exists(output_path):
            return False
        
        # 打开图片
        image = Image.open(input_path)
        
        # 如果是 HEIC 格式，则转换为 JPEG 格式
        if image.format == 'HEIC':
            output_path = output_path.replace('.jpeg', '.png')  # 修改输出路径为 PNG 格式
            image = image.convert("RGB")

        # 如果是 PNG 格式，则转换为 JPEG 格式
        if image.format == 'PNG':
            output_path = output_path.replace('.jpeg', '.png')  # 修改输出路径为 PNG 格式
            image = image.convert("RGB")
        
        # 获取原始图片尺寸
        width, height = image.size
        
        # 计算调整后的尺寸
        if width >= height:
            new_width = min(width, max_size)
            new_height = int(height * (new_width / width))
        else:
            new_height = min(height, max_size)
            new_width = int(width * (new_height / height))
        
        # 调整尺寸并保存
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        resized_image.save(output_path, quality=quality)  # 设置压缩质量
        
        return True
    except Exception as e:
        print(f"Failed to compress {input_path}: {e}")
        return False

# 遍历文件夹中的图片并压缩保存
def compress_images_in_folder(input_folder, output_folder, high_quality=False):
    max_size = 800 if high_quality else 400
    max_quality = 100 if high_quality else 60
    
    for root, dirs, files in os.walk(input_folder):
        # 生成对应的输出文件夹结构
        rel_path = os.path.relpath(root, input_folder)
        output_root = os.path.join(output_folder, rel_path)
        os.makedirs(output_root, exist_ok=True)
        
        # 遍历文件夹中的文件
        for file in tqdm(files, desc=f'Compressing images in {root}'):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_root, file.split('.')[0] + '.jpeg')  # 添加 -small 后缀
                compress_image(input_path, output_path, quality=max_quality, max_size=max_size)

# 主函数
if __name__ == "__main__":
    input_folder = '/Volumes/共享文件/photo'
    output_folder = 'photo/photo_small'
    output_folder_high_quality = 'photo/photo_big'
    
    compress_images_in_folder(input_folder, output_folder)
    compress_images_in_folder(input_folder, output_folder_high_quality, high_quality=True)
