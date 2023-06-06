<details>
<summary> #Issue : Image truncated, accuracy</summary><br>

- try1. PIL 라이브러리로 파일 손상 검사 돌려봄 → 이미지 손상은 X
- try2. `ImageFile.LOAD_TRUNCATED_IMAGES = True` 설정
    - 트레이닝 돌리면 돌아는 가는데 예상보다 더 **accuracy가 낮게나옴**
    - 이미지가 잘려서 파일 일부만 입력으로 들어가서인듯
- try3. 데이터 형상 상수 정의 - 사진 크기 설정
    - 코랩(GPU) - 세션이 자꾸 죽음
    - 주피터(CPU) - 600*600 으로 돌리면 → ETA: 4시간 이상
        - 집가서 서브 노트북으로 돌려보기…
    - image size=256*256, batch size=10/5, epoch=3
    - image size=512*512, batch size=5, epoch=10
  
    - image size=256*256, batch size=5, epoch=10

    - **image size=256*256, batch size=8, epoch=10 `best`**    
    - image size=256*256, batch size=16, epoch=10      
    - image size=256*256, batch size16, epoch=30
        - 30으로 돌렸는데 다 안돌아감


        
    - image size=256*256, batch size=32, epoch=10
        
- try4. 이미지 resize
- 1000*1000 돌려본 결과 공유 → 데이터 더 수집해야할지 말지
    - 코랩에서는 세션 죽음, RAM 부족
    - CNN 모델에서 일반적으로 작은 이미지를 사용하는 이유
        
        <u>모델 복잡성:</u> CNN 모델은 보통 이미지의 로컬 패턴과 구조를 학습하기 위해 작은 합성곱 필터를 사용합니다. 작은 이미지에서도 로컬 패턴을 잘 파악할 수 있으며, 이미지를 크게 하면 이러한 로컬 패턴이 희석될 수 있습니다. 따라서 작은 이미지 크기로 충분한 성능을 얻을 수 있습니다.
        
        <u>Overfitting의 위험 감소:</u> 큰 이미지를 사용하면 모델이 작은 세부 사항에 더 많이 fitting되는 경향이 있습니다. 작은 이미지에서는 학습 데이터의 다양성을 잘 반영하고 일반화된 모델을 학습하는 데 도움이 될 수 있습니다.
        
        라고 합니다.. </details><br>


# 최종 모델

## 선정성: 노출/비노출 분류



## 선정성: 관계/비관계 분류 


## 폭력성: 폭력/비폭력 분류