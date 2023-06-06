<details>
<summary> 

> ### 두가지 모델 비교 

- **Sequential 모델:**
    - Keras라는 딥러닝 라이브러리에서 제공하는 API로, 간단하고 순차적인 딥러닝 모델을 만들 수 있게 해준다.
    - 레이어를 순차적으로 쌓아 구성하고, <u>각 레이어는 이전 레이어의 출력을 입력으로 받아</u> 처리한다.
    - <u><i>단순하고 직관적인 설계</i></u>를 위해 주로 사용되며, 비교적 작은 규모의 모델에 적합하다. 

<br>

- **VGG16 모델:**
    - 옥스퍼드 대학에서 개발한 딥러닝 아키텍처로, 이미지 인식 대회인 ImageNet Challenge에서 우수한 성능을 보여준 모델
    - 16개의 레이어로 구성된 깊은 신경망으로 합성곱(Convolution)과 풀링(Pooling) 레이어로 구성되어 있으며, 마지막에는 완전 연결층(Fully Connected Layer)으로 이어진다.
    - VGG16은 작은 필터 크기(3x3)를 사용하여 깊은 네트워크를 구성하고, 많은 필터(총 16개의 레이어에서 13개의 합성곱 레이어)를 사용하여 다양한 이미지 특징을 추출한다.
    - VGG16은 ImageNet 데이터셋으로 사전 훈련된 가중치를 제공하므로, 전이 학습(Transfer Learning)에 많이 사용된다.

<br><br>

# 최종 모델

> 💡 Training Value
>- loss: 훈련 손실 값
현재 배치에서 모델이 예측한 출력과 실제 레이블 사이의 차이 → `모델의 적합성`
>- accuracy: 훈련 정확도
>현재 배치에서 모델이 올바르게 분류한 샘플의 비율 → `모델의 성능`
>- val_loss: 검증 손실 값 
검증 데이터셋에서 모델의 예측과 실제 레이블 사이의 차이 → `일반화 성능`
>- val_accuracy: 검증 정확도
검증 데이터셋에서 모델이 올바르게 분류한 샘플의 비율 → `일반화 성능`
>- lr: 학습률(learning rate)
모델이 가중치를 업데이트하는 속도를 조절하는 하이퍼파라미터

### 선정성: 노출/비노출 분류
<div style="display: flex; justify-content: space-between;">
  <figure>
  <img alt="스크린샷 2023-06-06 오후 9 00 25" src="https://github.com/selfrescue/selfrescue/assets/130124454/30759e76-08d1-4434-9e9e-36725c4d99ce" style='width:30%;'>
    <figcaption>손실값</figcaption>
  </figure>
  <figure>
  <img alt="스크린샷 2023-06-06 오후 8 56 53" src="https://github.com/selfrescue/selfrescue/assets/130124454/2e4a8de8-163d-4641-88f5-c0ab4964df56" style='width: 30%;'>
    <figcaption>정확도</figcaption>
  <figure>
</div>

<br>

### 선정성: 관계/비관계 분류 
<div style="display: flex; justify-content: space-between;">
  <figure>
    <img alt="스크린샷 2023-06-06 오후 9 01 51" src="https://github.com/selfrescue/selfrescue/assets/130124454/9e4becda-adb9-4fab-ba65-e326047acfdd" style='width:30%;'>
    <figcaption>손실값</figcaption>
  </figure>
  <figure>
    <img alt="스크린샷 2023-06-06 오후 9 01 41" src="https://github.com/selfrescue/selfrescue/assets/130124454/e1aed142-4b14-46b5-b79e-0fbc631bd109" style='width: 30%;'>
    <figcaption>정확도</figcaption>
  </figure>
</div>

<br>

### 폭력성: 폭력/비폭력 분류
<div style="display: flex; justify-content: space-between;">
  <figure>
    <img alt="스크린샷 2023-06-06 오후 9 05 17" src="https://github.com/selfrescue/selfrescue/assets/130124454/e78e287a-ac39-4f98-abff-741341014808" style="width: 30%;">
    <figcaption>손실값</figcaption>
  </figure>
  <figure>
      <img alt="스크린샷 2023-06-06 오후 9 04 54" src="https://github.com/selfrescue/selfrescue/assets/130124454/0867fae7-4eeb-4343-a336-edcd85997d1f" style="width: 30%;">
    <figcaption>정확도</figcaption>
  </figure>
</div>
