import os

# 디렉토리 경로 설정
directory_path = '/Users/inkyung/Desktop/IT_Projects/ttproject/선정적 이미지 소스/관계 이미지'

# prefix1.jpg, prefix2.jpg, ... , 
prefix = '비관계이미지'

# 변경할 prefix
#new_prefix = '관계이미지'

start_idx = 1

# digit 설정 (001, 002.. 이렇게)
num_width = 3

file_list = os.listdir(directory_path)

# 파일명을 숫자에 매핑하고 정렬
file_dict = {}
for file_name in file_list:
    if file_name.startswith(prefix) and (file_name.endswith('.jpg') or file_name.endswith('.JPG')):
        file_idx = int(file_name[len(prefix):-4])
        file_dict[file_idx] = file_name
sorted_files = [file_dict[idx] for idx in sorted(file_dict.keys())]

# 파일명 변경 및 rename
for idx, file_name in enumerate(sorted_files):
    file_idx = start_idx + idx
    new_file_name = f'{prefix}{str(file_idx).zfill(num_width)}{os.path.splitext(file_name)[1]}'
    #new_file_name = f'{new_prefix}{str(file_idx).zfill(num_width)}{os.path.splitext(file_name)[1]}'  #파일명 변경시
    os.rename(os.path.join(directory_path, file_name),
              os.path.join(directory_path, new_file_name))
