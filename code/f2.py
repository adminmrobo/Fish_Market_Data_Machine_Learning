# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 2편 2장 · 스케일링과 학습률
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① 원래 단위 vs 표준화 ② 학습률 3가지의 손실 비교
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
from common import *
from sklearn.model_selection import GroupShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import log_loss

d = df[df["species"].isin(["Perch", "Roach"])]
tr, te = next(GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=0).split(d, groups=d["seed_id"]))
Xtr, Xte = d[FEATS].values[tr], d[FEATS].values[te]
ytr, yte = (d["species"].values[tr] == "Roach"), (d["species"].values[te] == "Roach")
print("특성의 크기 차이:", {f: round(float(d[f].std()), 1) for f in FEATS})

def run(Xa, Xb, eta, epochs=30):
    m = SGDClassifier(loss="log_loss", learning_rate="constant", eta0=eta, random_state=0)
    losses = []
    for _ in range(epochs):                     # partial_fit 한 번 = 1 에포크
        m.partial_fit(Xa, ytr, classes=[False, True])
        losses.append(log_loss(ytr, m.predict_proba(Xa), labels=[False, True]))
    return losses, m.score(Xb, yte)

sc = StandardScaler().fit(Xtr)
for label, Xa, Xb in [("원래 단위", Xtr, Xte), ("표준화", sc.transform(Xtr), sc.transform(Xte))]:
    for eta in [0.0001, 0.01, 0.1]:
        L, acc = run(Xa, Xb, eta)
        print(f"{label:<6} η={eta:<7} 손실: 1에포크 {L[0]:7.3f} → 30에포크 {L[-1]:7.3f}   시험 정확도 {acc:.3f}")
