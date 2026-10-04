# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 2편 3장 · 특성 공학과 L1 규제
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① 비율 특성 만들기 ② L1 규제 강도별 남은 특성
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
from common import *
from sklearn.model_selection import StratifiedGroupKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

d = df[df["species"].isin(["Perch", "Roach"])].copy()
# 새 특성 만들기 (특성 공학): 크기와 상관없는 "체형" 비율
d["height_ratio"] = d["height_cm"] / d["length2_cm"]           # 높이 ÷ 길이: 통통한 정도
d["width_ratio"] = d["width_cm"] / d["length2_cm"]             # 두께 ÷ 길이
d["plumpness"] = np.cbrt(d["weight_g"]) / d["length2_cm"]      # 무게의 세제곱근 ÷ 길이: 살집
d["tail_ratio"] = (d["length3_cm"] - d["length2_cm"]) / d["length2_cm"]   # 꼬리 길이 ÷ 몸길이
yy, gg = d["species"], d["seed_id"]
cv = StratifiedGroupKFold(5, shuffle=True, random_state=0)
logit = lambda **kw: make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000, **kw))

sets = {"길이·높이 (2개)": ["length2_cm", "height_cm"],
        "길이·높이 + 체형 비율": ["length2_cm", "height_cm", "height_ratio"],
        "길이·높이 + 꼬리 비율": ["length2_cm", "height_cm", "tail_ratio"],
        "원래 특성 6개": FEATS,
        "6개 + 비율 3개 (9개)": FEATS + ["height_ratio", "width_ratio", "plumpness"]}
print(f"기준선 (모두 농어라고 답하기): {(yy == 'Perch').mean():.3f}")
for name, cols in sets.items():
    s = cross_val_score(logit(), d[cols], yy, cv=cv, groups=gg)
    print(f"{name:<22} {s.mean():.3f} ± {s.std():.3f}")

cols = sets["6개 + 비율 3개 (9개)"]
print("\nL1 규제 강도에 따른 계수 (C가 작을수록 강한 규제)")
for C in [10, 1, 0.1]:
    m = logit(penalty="l1", C=C, solver="liblinear").fit(d[cols], yy)
    w = m[-1].coef_.ravel()
    kept = [f"{c}:{v:+.2f}" for c, v in zip(cols, w) if abs(v) > 1e-6]
    acc = cross_val_score(logit(penalty="l1", C=C, solver="liblinear"), d[cols], yy, cv=cv, groups=gg).mean()
    print(f"C={C:<4} 남은 특성 {len(kept)}/9  교차검증 {acc:.3f}  {', '.join(kept)}")
