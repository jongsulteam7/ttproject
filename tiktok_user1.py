import os
import shutil
import csv

# 원본 폴더 경로 설정
source_folder_path = "C:/Users/user/Desktop/video"

# 대상 폴더 경로 설정
destination_folder_path = "C:/Users/user/Desktop/blind"

# 원본 폴더 내의 파일 목록 가져오기
file_list = os.listdir(source_folder_path)

# jpg와 csv 파일 모두 이동 및 CSV 파일 정보 읽어오기
for file_name in file_list:
    if file_name.endswith(".jpg") or file_name.endswith(".csv"):
        # 파일의 전체 경로 구성
        source_file_path = os.path.join(source_folder_path, file_name)
        destination_file_path = os.path.join(destination_folder_path, file_name)
        
        # 파일 이동
        shutil.move(source_file_path, destination_file_path)
        
        # CSV 파일일 경우 내용 읽어오기
        if file_name.endswith(".csv"):
            with open(destination_file_path, "r", encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)  # 헤더 가져오기

                # 열 인덱스 확인
                name_index = header.index("authorMeta/name")

                for row in csv_reader:
                    if len(row) > name_index:
                        # 열 이름이 "authorMeta/name"인 행만 가져오기
                        name = row[name_index]
                        print(name)

