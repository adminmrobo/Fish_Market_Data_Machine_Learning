# Fish Market Data로 쉽게 따라하는 머신러닝

어시장에서 잰 물고기 1,554마리로, 물고기의 종을 맞히는 분류 모델을 버튼만 눌러 따라 배우는 교육용 웹 페이지입니다. 밤의 초파리 연구실에서 박사, 조수, 초파리 연구원이 함께합니다.

- 글: 안상선 ((주)M-Robo 대표)
- 라이선스: CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수) — [LICENSE.md](LICENSE.md)

## 편 목록

| 편 | 파일 | 제목 |
|---|---|---|
| 처음 화면 | `index.html` | 연구실 식구들, 연구 지도, 연구실의 하루 |
| 1 | `1_classification_models.html` | 분류 모델은 모두 하나의 함수다 (규칙 기반부터 딥러닝까지 여덟 모델) |
| 2 | `2_improve_performance.html` | 모델을 바꾸기 전에, 성능을 올리는 네 가지 방법 |
| 3 | `3_lab_models.html` | 물고기 분류 실험실 ① 모델 바꿔 보기 |
| 4 | `4_lab_methods.html` | 물고기 분류 실험실 ② 방법 바꿔 보기 |
| 정답 | `answers.html` | 교육자용 정답 (확인 문제 채점 기준, 과제 예시 답안) |

## 폴더

```
├── index.html, answers.html, 1~4 편 .html   그림과 스크립트가 모두 파일 안에 들어 있다
├── code/      Colab·주피터에서 실행하는 scikit-learn 코드 (common.py와 f0~f4.py)
├── data/      fish_market_x10.csv
├── prompts/   코드·데이터를 바꿀 때 AI 도우미에게 주는 풀버전 프롬프트
├── LICENSE.md
└── .nojekyll
```

## 데이터

원 자료는 [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market)(물고기 7종 159마리의 무게·길이·높이·두께)입니다. 종별 평균과 분산을 유지하도록 정규분포를 이용해 증강해 1,590행을 만들었고, 무게가 0으로 적힌 1행과 완전히 같은 35행을 빼서 1,554마리를 씁니다. 같은 원본에서 증강된 물고기는 같은 `seed_id`를 가지며, 모든 점수는 이 묶음이 학습과 시험으로 갈리지 않게 나눠 계산했습니다.

## GitHub Pages로 배포하기

1. github.com → **New repository** → 저장소 이름 입력 → **Public** → README 체크 해제 → 만들기
2. **uploading an existing file** → 압축을 푼 폴더의 **내용물 전체**를 끌어다 놓기 → Commit
3. **Settings → Pages** → Branch `main`, 폴더 `/ (root)` → Save
4. 1~3분 뒤 `https://<아이디>.github.io/<저장소 이름>/`

고칠 때는 같은 이름의 파일을 다시 올려 덮어씁니다. 바뀐 내용이 안 보이면 강력 새로고침(Ctrl + F5)을 합니다.
