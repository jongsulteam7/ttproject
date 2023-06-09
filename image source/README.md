## Dataset 구성
본 데이터셋은 모델 학습용 이미지 데이터셋으로, 선정적(관계, 노출), 폭력적 이미지 데이터셋으로 구성되어 있습니다. <br>
모델 학습을 위해 각 범주를 다음과 같이 나누었으며, 나누는 기준은 <b>`방송통신심의위원회의 Safenet`</b> 등급 기준의 `15세 관람가 기준`입니다. 

```kotlin
1) 선정적 이미지 
    - 관계 이미지 / 비관계 이미지
    - 노출 이미지 / 비노출 이미지

2) 폭력적 이미지
    - 폭력적 이미지 / 비폭력적 이미지
```

### Dataset 별 수량
```kotlin
1) 선정적 이미지 
    - 관계 이미지(989) / 비관계 이미지(660) 
    - 노출 이미지(800) / 비노출 이미지(500)
    
2) 폭력적 이미지
    - 폭력적 이미지(500) / 비폭력적 이미지(511) 
```

### Dataset 출처
1) 선정적 이미지 
    - adult;Pornography Use;image classification method;Computer Vision;Image Processing;Pattern Recognition and Data Mining (https://figshare.com/articles/dataset/Adult_content_dataset/13456484 )
    - 비관계 이미지 일부 : Gokhan Tanisik, Cemil Zalluhoglu, Nazli Ikizler-Cinbis, Facial Descriptors for Human Interaction Recognition In Still Images, Pattern Recognition Letters, 2016, ISSN 0167-8655 (https://vision.cs.hacettepe.edu.tr/interaction_images/)

2) 폭력적 이미지
    - 구글링
    - 폭력 이미지 일부 : ⚠️(직접적인 살해 이미지가 있는 사이트로, 확인에 유의해 주세요)  https://www.documentingreality.com/forum/f10/


### Dataset 가공 사항
일부 이미지가 콜라주 형태로 혼재되어 있어 명확한 이미지 인식이 어렵기에, 단일 이미지 형태로 만들기 위해 이미지를 일부 잘라 사용하였으며 <br> 폴더별로 해당 범주에 해당하는 이미지들을 분류하였습니다. 
