# Photo Handler

读取input_folder里的照片，压缩成适合网络传输的更小的图片：

1. 压缩成两个尺寸：
    1. big: 最大的横或宽不超过800
    2. small:最大的横或宽不超过400
2. 遇到别的文件格式，转为jpeg，目前会读取的格式有`png``jpg``jpeg``heic`
3. 默认的文件夹
   ```
    input_folder = 'photo/photo_original'
    output_folder = 'photo/photo_small'
    output_folder_high_quality = 'photo/photo_big'
    ```
4. 会保留`input_folder`下原来的子文件夹结构，文件名也相同(当然拓展名都被转成`jpeg`了)
