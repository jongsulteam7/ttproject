# jongsulteam7

<details>
<summary>🖥 <b>commit log</b></summary><br>

<b>[0511]</b> `혜연` 테스트용 틱톡 비디오 업로드 완료

1) tiktok videos > 건전, 선정, 폭력 폴더로 구분
2) 건전 동영상 80개, 선정 동영상 - 관계 동영상 5개, 선정 동영상 - 노출 동영상 5개, 폭력 동영상 10개로 총 8:1:1 비율로 구성
3) 관계 동영상, 노출 동영상 일부는 틱톡 자체 어플이 아닌 트위터와 같은 외부 어플에서 아카이브된 내용을 사용하였으며, <br>이외 영상은 모두 틱톡에서 가져옴
4) 모든 영상을 약 20초 내외로 하기 위해 일부 동영상 길이를 조정한 부분이 있음

<b>[0511]</b> `인경` CNN 테스트 파일 업로드 완료
- data augmentation 추가 필요
- 남는 이미지로 테스트 진행 예정

<b>[0512]</b> `윤아` 모델링 학습용 이미지 업로드 완료
: 새로운 모델링 학습 이미지 폴더안에 해당 내용 추가

<b>[~0529</b>] Sequentail, VGG 모델로 세분화해 개발 진행 <br>
    - `도현` : VGG <br>
    - `인경` : Sequential

<b>[0529]</b> `혜연` 테스트용 틱톡 비디오/선정 이미지 보완 및 추가  
1) tiktok videos > 선정 동영상 일부 수정 (갯수 변동X, 총 5장)
2) tiktok videos > 건전 동영상 일부 수정 (갯수 변동X)
3) 모델 학습용 이미지 소스 >  선정적 이미지 소스 일부 수정 및 300장 추가 (총 800장)
    - 애매한 부분 삭제하고 확실한 이미지로 수정
    - 여성 노출로 치중된 부분 있어 남성 노출 이미지 추가
    - 일부 보완 + 300장 추가
4) 모델 학습용 이미지 소스 >  비선정적 이미지 소스 일부 수정 및 300장 추가 (총 800장)
    - 애매한 부분 삭제하고 확실한 이미지로 수정
    - 크기 너무 작은 이미지들 삭제
    - 일부 보완 + 300장 추가
    
<b>[0602]</b> `혜연` 비노출 이미지 데이터셋 보완: 수량 500개로 조정 (노출 심한 이미지 삭제 및 일반 복장 착용 이미지 추가)     
    
<b>[0606]</b> `윤아` 연동 로그 파일 소스 + csv 파일 '로그 연동 파일' 폴더로 정리    
`도현` 동영상 테스트 파일 업로드 <br>
`인경` cnn_sequential 최종 모델 업로드

<b>[~0608]</b>
`윤아` 프레임화, 로그 연동 코드 점검 및 최종 보완 <br>
`도현` VGG 클래스별 테스트, 분류 모델 구현<br>
`인경` Sequential 클래스별 테스트, 분류 모델 구현 <br>
`혜연` 오차 범위 테스트, 로그-blind 연동

<b>[0610]</b> `혜연` `윤아` `도현` `인경` 최종 코드 제외 파일 및 디렉토리 정리

</details> 

- - -
## 📃 소개
<p align="center">
  <img src="https://github.com/selfrescue/selfrescue/assets/130124454/665ba540-e8ba-4656-a5ee-49c2db1a298a" width="630px">
</p>

`한국외국어대학교 글로벌캠퍼스 Software&AI` 전공 2023년 1학기 `종합설계 수업의 7조` 깃허브 페이지입니다!

저희는 SNS 앱 <img src="https://img.shields.io/badge/tiktok-000000?style=flat&logo=tiktok&logoColor=white"/>에서의 *선정적이거나, 폭력적인 영상들을 필터링 하는 모델* 을 주제로 프로젝트를 진행하였습니다.

## 🧑‍🤝‍🧑 팀원
7조 팀원들을 소개합니다( ˃ᴗ˂ )
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<table>
  <tr>
    <td align="center">
    <a href="https://github.com/selfrescue">
    <img src="https://github.com/selfrescue.png" width="150px;" alt="혜연"/>
    <br />
    <sub>
    <b>유혜연</b><br>
    <b> :bulb: PM, 데이터 수집 및 가공</b>
    </sub>
    </a>
    <br />
    <td align="center">
    <a href="https://github.com/YooongA">
    <img src="https://github.com/YooongA.png" width="150px;" alt="윤아"/>
    <br />
    <sub>
    <b>이윤아</b><br>
    <b> :mag: 데이터 수집 및 가공, 로그 파일 연동</b>
    </sub>
    </a>
    <td align="center">
    <a href="https://github.com/dony1220">
    <img src="https://github.com/dony1220.png" width="150px;" alt="도현"/>
    <br />
    <sub>
    <b>김도현</b><br>
    <b>🌟 모델링</b>
    </sub>
    </a>
    <br />
    </td>
    <td align="center">
    <a href="https://github.com/InKyungWoo">
    <img src="https://github.com/InKyungWoo.png" width="150px;" alt="인경"/>
    <br />
    <sub>
    <b>Inkyung Woo</b><br>
    <b>🌟 모델링</b>
    </sub>
    </a>
    <br />
    </td>    
    <br />
    </td>    
  </tr>
</table>

## 🧰 툴
<table>
  <tr>
    <td align="center">
    <a href=''>
    <img src="https://github.com/selfrescue/selfrescue/assets/130124454/3ae060ca-8f5f-4ca7-a880-3168cb5deaec" width="150px;" alt='Google Colab'/>
    <br />
    <sub>
    <b>Google Colab</b><br>
    <b> 💻 모델링 설계 </b>
    </sub>
    </a>
    <br />
    </td>
    <td align='center'>
    <a href='https://spiral-moose-c33.notion.site/7e97e0c8815d4acf815ffa0c885348a4?pvs=4'>
    <img src='https://github.com/selfrescue/selfrescue/assets/130124454/189b7c67-88a0-49c6-9682-1aecef0533e2' width="150px;" alt="Notion"/>
    <br />
    <sub>
    <b>Notion</b><br>
    <b> 📆 일정 관리, 역할 분배, 회의록 공유</b>
    </sub>
    </a>
    <br />
    </td>
    <td align="center">
    <a href='https://discord.gg/KJWkZJg4'>
    <img src='https://github.com/selfrescue/selfrescue/assets/130124454/cf370aee-98cc-4546-a1b3-a68884994a20' width="150px;" alt="Discord"/>
    <br />
    <sub>
    <b>Discord</b><br>
    <b> ✏️ 스터디 및 중간 미팅 진행</b>
    </sub>
    </a>
    <br />
    </td>
    <td align="center">
    <a href=''>
    <img src="https://github.com/selfrescue/selfrescue/assets/130124454/76109cbe-7af1-4494-ae52-3abbdd09fdf2" width="150px;" alt="Google Meet"/>
    <br />
    <sub>
    <b>Google Meet</b><br>
    <b>✏️ 비대면 회의 진행</b>
    </sub>
    </a>
    <br />
    </td>    
    <td align="center">
    <a href=''>
    <img src="https://github.com/selfrescue/selfrescue/assets/130124454/d657cc6e-e8a1-4c48-9988-3ba3cf8f6c63" width="150px;" alt="Google Drive"/>
    <br />
    <sub>
    <b>Google Drive</b><br>
    <b> 📹 구현 영상 및 모델 파일 업로드 </b>
    </sub>
    </a>
    <br />
    </td>
  </tr>
</table>
  
#### [Notion 페이지 링크](https://spiral-moose-c33.notion.site/7e97e0c8815d4acf815ffa0c885348a4?pvs=4) : 전체 프로젝트 R&R 및 회의록 관리 페이지입니다.
#### [GoogleDrive 링크](https://drive.google.com/drive/folders/1BYTg3gTPLE2lTy0RrNSjG9CHcRoApqJN?usp=drive_link) : 모델의 크기가 커 깃허브에 업로드가 불가하기에 설계한 모델은 깃허브가 아닌 드라이브에 업로드하였습니다. 

## 📝 모델 구조
![제목을 입력해주세요_-004](https://github.com/jongsulteam7/ttproject/assets/130124454/9b82aee0-54e2-48ce-98b4-9aad679f68a9)

