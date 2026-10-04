# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 2편 1장 · 데이터 분할과 누수
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① 행 단위·묶음 단위·원본만 분할 비교
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
from common import *
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

print(df.groupby("species").agg(행=("seed_id", "size"), 물고기=("seed_id", "nunique")).sort_values("행", ascending=False).T)

models = {"KNN (k=1)": make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=1)),
          "로지스틱 회귀": make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000)),
          "의사결정나무": DecisionTreeClassifier(random_state=0)}
plain = StratifiedKFold(5, shuffle=True, random_state=0)          # 행 단위로 섞어 나눔 (누수)
grouped = StratifiedGroupKFold(5, shuffle=True, random_state=0)   # 같은 seed_id는 한쪽에만
orig = df[df["source"] == "original"]
print(f"\n{'모델':<10}{'행 단위 분할':>10}{'물고기 단위 분할':>12}{'원본만 (158마리)':>12}")
for name, m in models.items():
    a = cross_val_score(m, X, y, cv=plain).mean()
    b = cross_val_score(m, X, y, cv=grouped, groups=groups).mean()
    c = cross_val_score(m, orig[FEATS], orig["species"], cv=StratifiedKFold(5, shuffle=True, random_state=0)).mean()
    print(f"{name:<10}{a:>10.3f}{b:>12.3f}{c:>12.3f}")
