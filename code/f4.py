# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 2편 4장 · 여러 알고리즘 혼합
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① 보팅·배깅·랜덤 포레스트·부스팅 ② 비율 특성 추가와 비교
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
from common import *
from sklearn.model_selection import StratifiedGroupKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier, BaggingClassifier, RandomForestClassifier, GradientBoostingClassifier

cv = StratifiedGroupKFold(5, shuffle=True, random_state=0)
logit = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
knn = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
models = {
    "의사결정나무 (단독)": DecisionTreeClassifier(random_state=0),
    "KNN (단독)": knn,
    "로지스틱 회귀 (단독)": logit,
    "보팅 (위 세 모델, soft)": VotingClassifier([("tree", DecisionTreeClassifier(max_depth=5, random_state=0)), ("knn", knn), ("lr", logit)], voting="soft"),
    "배깅 (나무 200그루)": BaggingClassifier(DecisionTreeClassifier(), n_estimators=200, random_state=0),
    "랜덤 포레스트 (200그루)": RandomForestClassifier(n_estimators=200, random_state=0),
    "그래디언트 부스팅": GradientBoostingClassifier(random_state=0),
}
for name, m in models.items():
    s = cross_val_score(m, X, y, cv=cv, groups=groups)
    print(f"{name:<18} {s.mean():.3f} ± {s.std():.3f}")

# 모델을 묶는 대신 특성을 더하면? (3장의 체형 비율과 꼬리 비율)
d = df.copy()
d["height_ratio"] = d["height_cm"] / d["length2_cm"]
d["tail_ratio"] = (d["length3_cm"] - d["length2_cm"]) / d["length2_cm"]
cols = FEATS + ["height_ratio", "tail_ratio"]
print("\n특성 8개 (원래 6개 + 비율 2개)")
for name in ["로지스틱 회귀 (단독)", "랜덤 포레스트 (200그루)"]:
    s = cross_val_score(models[name], d[cols], d["species"], cv=cv, groups=d["seed_id"])
    print(f"{name:<18} {s.mean():.3f} ± {s.std():.3f}")
