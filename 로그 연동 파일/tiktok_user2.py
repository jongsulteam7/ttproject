import os
import csv
import shutil

# 입력 경로
folder_path = r'C:\Users\user\Desktop\video'

# 출력 폴더 경로
output_folder = r'C:\Users\user\Desktop\blind'

# 출력 폴더 생성
os.makedirs(output_folder, exist_ok=True)

# .csv 파일 경로
csv_file_path = os.path.join(folder_path, 'dataset_tiktok.csv')

# .csv 파일 열 'authorMeta/name'과 .jpg 파일 이름 매핑을 위한 딕셔너리
mapping_dict = {}

# .csv 파일 열 'authorMeta/name'과 .jpg 파일 이름 매핑
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        mapping_dict[row['authorMeta/name']] = row

# .csv 파일과 매핑된 .jpg 파일을 이동
matched_rows = []

for file_name in os.listdir(folder_path):
    if file_name.endswith('.jpg'):
        jpg_file_path = os.path.join(folder_path, file_name)

        for csv_file_name, csv_row in mapping_dict.items():
            if csv_file_name in file_name:
                # 파일 이동
                shutil.move(jpg_file_path, os.path.join(output_folder, file_name))
                matched_rows.append(csv_row)
                break
# 매핑된.csv파일의 사용자 이름 읽어온 후 출력
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in matched_rows:
        print(row['authorMeta/name'])