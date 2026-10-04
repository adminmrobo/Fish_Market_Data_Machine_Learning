# Fish Market Data로 쉽게 따라하는 머신러닝 · 글 안상선 · CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수)
# ===============================================================
# 1편 · 물고기 7종으로 모델 비교하기
#  - 라이브러리: pandas, numpy, scikit-learn
#  - 실행 확인: scikit-learn 1.8 (CPU)
#  - 하는 일: ① 7종·특성 6개 ② 원본 묶음 단위 5겹 교차검증으로 7개 모델 비교
#  - 데이터: Kaggle Fish Market(https://www.kaggle.com/datasets/vipullrathod/fish-market)을 정규분포를 고려해 증강한 1,554마리
# ===============================================================
from common import *
from sklearn.model_selection import StratifiedGroupKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import LinearSVC, SVC
from sklearn.neural_network import MLPClassifier

cv = StratifiedGroupKFold(5, shuffle=True, random_state=0)   # 같은 물고기(seed_id)는 한쪽에만
scaled = lambda m: make_pipeline(StandardScaler(), m)
models = {
    "KNN (k=5)":            scaled(KNeighborsClassifier(n_neighbors=5)),
    "의사결정나무 (깊이 5)":    DecisionTreeClassifier(max_depth=5, random_state=0),
    "퍼셉트론":               scaled(Perceptron(random_state=0)),
    "로지스틱 회귀":           scaled(LogisticRegression(max_iter=5000)),
    "선형 SVM":              scaled(LinearSVC(C=1.0, max_iter=20000)),
    "커널 SVC (RBF)":        scaled(SVC(kernel="rbf", C=1.0)),
    "MLP (32-32, ReLU)":    scaled(MLPClassifier(hidden_layer_sizes=(32, 32), max_iter=3000, random_state=0)),
}
print(f"기준선 (가장 많은 농어만 답하기): {(y == 'Perch').mean():.3f}")
for name, m in models.items():
    s = cross_val_score(m, X, y, cv=cv, groups=groups)
    print(f"{name:<18} {s.mean():.3f} ± {s.std():.3f}")
