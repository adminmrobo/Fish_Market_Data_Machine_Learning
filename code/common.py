# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 공통 · 데이터 불러오기와 정리 (모든 코드가 함께 씀)
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① CSV 읽기 ② 무게 0인 행·중복 행 빼기
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
import pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
# 데이터 불러오기와 정리: 무게 0인 행과 완전히 같은 행을 뺀다
df = pd.read_csv("../data/fish_market_x10.csv")  # [내 데이터로 바꾸려면] 경로와 열 이름을 바꾼다
df = df[df["weight_g"] > 0].drop_duplicates().reset_index(drop=True)
FEATS = ["weight_g", "length1_cm", "length2_cm", "length3_cm", "height_cm", "width_cm"]
X, y, groups = df[FEATS], df["species"], df["seed_id"]   # seed_id: 같은 물고기에서 만든 복제본 묶음
