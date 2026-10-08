**[한국어](#ko) · [English](#en) · [中文](#zh) · [日本語](#ja) · [O'zbekcha](#uz) · [Русский](#ru)**

---

<a id="ko"></a>
# Fish Market Data로 쉽게 따라하는 머신러닝

어시장에서 잰 물고기 1,554마리로, 물고기의 종을 맞히는 분류 모델을 버튼만 눌러 따라 배우는 교육용 웹 페이지입니다. 밤의 초파리 연구실에서 박사, 조수, 초파리 연구원이 함께합니다.

- 글: 안상선 ((주)M-Robo 대표)
- 라이선스: CC BY-NC 4.0 (비상업적 이용, 출처 표기 필수) — [LICENSE.md](LICENSE.md)

## 언어

한국어가 기본이며, 모든 페이지를 영어·중국어·일본어·우즈베크어·러시아어로도 볼 수 있습니다. 각 페이지 상단 메뉴의 언어 선택 상자로 바꿀 수 있고, 처음 방문하면 브라우저 언어에 맞는 버전으로 자동으로 이동합니다(고른 언어는 기억됩니다). 주소 뒤에 `?lang=en`처럼 붙여 직접 지정할 수도 있습니다.

| 언어 | 폴더 |
|---|---|
| 한국어 (기본) | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

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
├── index.html, answers.html, 1~4 편 .html   한국어(기본). 그림과 스크립트가 모두 파일 안에 들어 있다
├── en/ zh/ ja/ uz/ ru/   같은 이름의 번역 페이지 (영어·중국어·일본어·우즈베크어·러시아어)
├── code/      Colab·주피터에서 실행하는 scikit-learn 코드 (common.py와 f0~f4.py)
├── data/      fish_market_x10.csv
├── prompts/   코드·데이터를 바꿀 때 AI 도우미에게 주는 풀버전 프롬프트
├── LICENSE.md
└── .nojekyll
```

## 데이터

원 자료는 [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market)(물고기 7종 159마리의 무게·길이·높이·두께)입니다. 종별 평균과 분산을 유지하도록 정규분포를 이용해 증강해 1,590행을 만들었고, 무게가 0으로 적힌 1행과 완전히 같은 35행을 빼서 1,554마리를 씁니다. 같은 원본에서 증강된 물고기는 같은 `seed_id`를 가지며, 모든 점수는 이 묶음이 학습과 시험으로 갈리지 않게 나눠 계산했습니다.

---

<a id="en"></a>
# Easy Machine Learning with Fish Market Data

An educational website where you learn classification models that identify fish species, using 1,554 fish measured at a fish market — just by pressing buttons. The Doctor, the Assistant and the Fruit Fly Researcher keep you company in the Fruit Fly Lab at night.

- Author: Ahn Sangsun (CEO, M-Robo Co., Ltd.)
- License: CC BY-NC 4.0 (non-commercial use, attribution required) — [LICENSE.md](LICENSE.md)

## Languages

Korean is the default, and every page is also available in English, Chinese, Japanese, Uzbek and Russian. Use the language selector in the top menu of any page; on your first visit you are taken automatically to the version that matches your browser language (your choice is remembered). You can also add `?lang=en` (or `ko`, `zh`, `ja`, `uz`, `ru`) to the address.

| Language | Folder |
|---|---|
| 한국어 (default) | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

## Parts

| Part | File | Title |
|---|---|---|
| Home | `index.html` | The lab crew, the research map, a day in the lab |
| 1 | `1_classification_models.html` | Every classification model is a function (eight models, from rule-based to deep learning) |
| 2 | `2_improve_performance.html` | Before switching models: four ways to improve performance |
| 3 | `3_lab_models.html` | Fish Classification Lab ① Switching models |
| 4 | `4_lab_methods.html` | Fish Classification Lab ② Switching methods |
| Answers | `answers.html` | Answer key for educators (grading criteria for check questions, sample answers for assignments) |

## Folders

```
├── index.html, answers.html, parts 1–4 .html   Korean (default); all images and scripts are inside each file
├── en/ zh/ ja/ uz/ ru/   translated pages with the same file names
├── code/      scikit-learn code to run in Colab / Jupyter (common.py and f0–f4.py)
├── data/      fish_market_x10.csv
├── prompts/   full prompt to give an AI assistant when changing the code or data
├── LICENSE.md
└── .nojekyll
```

## Data

The source is [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market) (weight, lengths, height and width of 159 fish of 7 species). It was augmented with normal distributions that preserve each species' mean and variance to 1,590 rows; removing 1 row with weight 0 and 35 exact duplicates leaves 1,554 fish. Fish augmented from the same original share the same `seed_id`, and every score was computed with splits that never separate such a group between training and test.

---

<a id="zh"></a>
# 用 Fish Market 数据轻松学机器学习

这是一个教育网站：用在鱼市测量的 1,554 条鱼，只需点击按钮，就能一步步学习识别鱼种的分类模型。夜晚的果蝇研究室里，博士、助手和果蝇研究员与你同行。

- 作者：Ahn Sangsun（M-Robo 株式会社代表）
- 许可：CC BY-NC 4.0（非商业使用，须注明出处）— [LICENSE.md](LICENSE.md)

## 语言

默认语言为韩语，所有页面也提供英语、中文、日语、乌兹别克语和俄语版本。可通过每页顶部菜单中的语言选择框切换；首次访问时会根据浏览器语言自动跳转到相应版本（所选语言会被记住）。也可以在网址后加上 `?lang=zh` 直接指定。

| 语言 | 文件夹 |
|---|---|
| 한국어（默认） | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

## 篇章目录

| 篇 | 文件 | 标题 |
|---|---|---|
| 首页 | `index.html` | 研究室成员、研究地图、研究室的一天 |
| 1 | `1_classification_models.html` | 分类模型都是一个函数（从基于规则到深度学习的八种模型） |
| 2 | `2_improve_performance.html` | 更换模型之前：提升性能的四种方法 |
| 3 | `3_lab_models.html` | 鱼类分类实验室 ① 更换模型 |
| 4 | `4_lab_methods.html` | 鱼类分类实验室 ② 更换方法 |
| 答案 | `answers.html` | 教师用参考答案（练习题评分标准、作业示例答案） |

## 文件夹

```
├── index.html、answers.html、第 1~4 篇 .html   韩语（默认），图片和脚本都内嵌在文件中
├── en/ zh/ ja/ uz/ ru/   同名的翻译页面
├── code/      在 Colab / Jupyter 中运行的 scikit-learn 代码（common.py 与 f0~f4.py）
├── data/      fish_market_x10.csv
├── prompts/   修改代码或数据时交给 AI 助手的完整提示词
├── LICENSE.md
└── .nojekyll
```

## 数据

原始数据为 [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market)（7 种鱼共 159 条的重量、长度、体高和体宽）。在保持各鱼种均值和方差的前提下，用正态分布将其增强为 1,590 行，去掉重量记为 0 的 1 行和完全重复的 35 行后，使用 1,554 条鱼。由同一原始样本增强出的鱼具有相同的 `seed_id`，所有分数都在保证同组样本不会被拆分到训练集和测试集两边的前提下计算。

---

<a id="ja"></a>
# Fish Market Dataでやさしく学ぶ機械学習

魚市場で測った 1,554 匹の魚を使い、魚の種類を当てる分類モデルをボタンを押すだけで順に学べる教育用ウェブページです。夜のショウジョウバエ研究室で、博士・助手・ショウジョウバエ研究員が一緒に案内します。

- 著者：アン・サンソン（株式会社 M-Robo 代表）
- ライセンス：CC BY-NC 4.0（非営利利用、出典表示必須）— [LICENSE.md](LICENSE.md)

## 言語

韓国語が基本で、すべてのページを英語・中国語・日本語・ウズベク語・ロシア語でも読めます。各ページ上部メニューの言語選択で切り替えられ、初めて訪れたときはブラウザの言語に合わせたバージョンへ自動的に移動します（選んだ言語は記憶されます）。アドレスの末尾に `?lang=ja` のように付けて直接指定することもできます。

| 言語 | フォルダ |
|---|---|
| 한국어（基本） | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

## 編の一覧

| 編 | ファイル | タイトル |
|---|---|---|
| トップ | `index.html` | 研究室のメンバー、研究マップ、研究室の一日 |
| 1 | `1_classification_models.html` | 分類モデルはすべて一つの関数である（ルールベースからディープラーニングまで 8 つのモデル） |
| 2 | `2_improve_performance.html` | モデルを変える前に、性能を上げる 4 つの方法 |
| 3 | `3_lab_models.html` | 魚の分類実験室 ① モデルを変えてみる |
| 4 | `4_lab_methods.html` | 魚の分類実験室 ② 方法を変えてみる |
| 解答 | `answers.html` | 教育者向け解答（確認問題の採点基準、課題の解答例） |

## フォルダ

```
├── index.html、answers.html、第1〜4編 .html   韓国語（基本）。画像とスクリプトはすべてファイル内に含まれる
├── en/ zh/ ja/ uz/ ru/   同じファイル名の翻訳ページ
├── code/      Colab・Jupyter で実行する scikit-learn コード（common.py と f0〜f4.py）
├── data/      fish_market_x10.csv
├── prompts/   コードやデータを変えるときに AI アシスタントへ渡すフル版プロンプト
├── LICENSE.md
└── .nojekyll
```

## データ

元データは [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market)（7 種 159 匹の魚の重さ・長さ・体高・体幅）です。種ごとの平均と分散を保つよう正規分布で拡張して 1,590 行を作り、重さが 0 と記録された 1 行と完全に同じ 35 行を除いた 1,554 匹を使います。同じ元データから拡張された魚は同じ `seed_id` を持ち、すべてのスコアはこのグループが学習とテストに分かれないように分割して計算しました。

---

<a id="uz"></a>
# Fish Market Data bilan oson mashinaviy o'qitish

Baliq bozorida o'lchangan 1 554 ta baliq yordamida baliq turini aniqlaydigan klassifikatsiya modellarini faqat tugmalarni bosib, bosqichma-bosqich o'rganadigan o'quv veb-sahifasi. Tungi Drozofila laboratoriyasida Doktor, Yordamchi va Drozofila tadqiqotchisi sizga hamroh bo'ladi.

- Muallif: Ahn Sangsun (M-Robo kompaniyasi rahbari)
- Litsenziya: CC BY-NC 4.0 (notijorat foydalanish, manbani ko'rsatish majburiy) — [LICENSE.md](LICENSE.md)

## Tillar

Asosiy til — koreys tili; barcha sahifalarni ingliz, xitoy, yapon, o'zbek va rus tillarida ham o'qish mumkin. Har bir sahifaning yuqori menyusidagi til tanlagich orqali almashtiring; birinchi tashrifda brauzeringiz tiliga mos versiyaga avtomatik o'tasiz (tanlangan til eslab qolinadi). Manzil oxiriga `?lang=uz` kabi qo'shib, tilni to'g'ridan-to'g'ri ko'rsatish ham mumkin.

| Til | Papka |
|---|---|
| 한국어 (asosiy) | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

## Qismlar

| Qism | Fayl | Sarlavha |
|---|---|---|
| Bosh sahifa | `index.html` | Laboratoriya jamoasi, tadqiqot xaritasi, laboratoriyadagi bir kun |
| 1 | `1_classification_models.html` | Barcha klassifikatsiya modellari — bitta funksiya (qoidaga asoslangan modeldan chuqur o'qitishgacha sakkizta model) |
| 2 | `2_improve_performance.html` | Modelni almashtirishdan oldin: samaradorlikni oshirishning to'rt usuli |
| 3 | `3_lab_models.html` | Baliq klassifikatsiyasi laboratoriyasi ① Modelni almashtirib ko'rish |
| 4 | `4_lab_methods.html` | Baliq klassifikatsiyasi laboratoriyasi ② Usulni almashtirib ko'rish |
| Javoblar | `answers.html` | O'qituvchilar uchun javoblar (nazorat savollarini baholash mezonlari, topshiriqlarga namunaviy javoblar) |

## Papkalar

```
├── index.html, answers.html, 1–4-qism .html   koreys tilida (asosiy); rasmlar va skriptlar fayl ichida
├── en/ zh/ ja/ uz/ ru/   xuddi shu nomdagi tarjima sahifalari
├── code/      Colab / Jupyter'da ishlaydigan scikit-learn kodi (common.py va f0–f4.py)
├── data/      fish_market_x10.csv
├── prompts/   kod yoki ma'lumotni o'zgartirishda AI yordamchiga beriladigan to'liq prompt
├── LICENSE.md
└── .nojekyll
```

## Ma'lumotlar

Manba — [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market) (7 turdagi 159 ta baliqning og'irligi, uzunliklari, balandligi va qalinligi). Har bir turning o'rtacha qiymati va dispersiyasini saqlagan holda normal taqsimot yordamida 1 590 qatorga kengaytirildi; og'irligi 0 deb yozilgan 1 qator va to'liq takrorlangan 35 qator olib tashlanib, 1 554 ta baliq ishlatiladi. Bitta asl namunadan kengaytirilgan baliqlar bir xil `seed_id` ga ega va barcha ballar shu guruh o'quv va test to'plamlariga bo'linib ketmaydigan qilib hisoblangan.

---

<a id="ru"></a>
# Машинное обучение на данных Fish Market — просто и наглядно

Обучающий сайт, на котором по 1 554 рыбам, измеренным на рыбном рынке, вы шаг за шагом изучаете модели классификации, определяющие вид рыбы, — просто нажимая кнопки. В ночной Лаборатории дрозофил вас сопровождают Доктор, Ассистент и Исследователь-дрозофила.

- Автор: Ан Сансон (генеральный директор M-Robo Co., Ltd.)
- Лицензия: CC BY-NC 4.0 (некоммерческое использование, обязательное указание авторства) — [LICENSE.md](LICENSE.md)

## Языки

Основной язык — корейский; все страницы доступны также на английском, китайском, японском, узбекском и русском. Язык переключается в меню вверху каждой страницы; при первом посещении вы автоматически попадёте на версию, соответствующую языку браузера (выбор запоминается). Можно также добавить к адресу `?lang=ru`.

| Язык | Папка |
|---|---|
| 한국어 (основной) | `/` |
| English | `en/` |
| 中文 | `zh/` |
| 日本語 | `ja/` |
| O'zbekcha | `uz/` |
| Русский | `ru/` |

## Части

| Часть | Файл | Название |
|---|---|---|
| Главная | `index.html` | Команда лаборатории, карта исследований, один день в лаборатории |
| 1 | `1_classification_models.html` | Любая модель классификации — это функция (восемь моделей: от правил до глубокого обучения) |
| 2 | `2_improve_performance.html` | Прежде чем менять модель: четыре способа улучшить качество |
| 3 | `3_lab_models.html` | Лаборатория классификации рыб ① Меняем модель |
| 4 | `4_lab_methods.html` | Лаборатория классификации рыб ② Меняем метод |
| Ответы | `answers.html` | Ответы для преподавателей (критерии оценки проверочных вопросов, примеры ответов к заданиям) |

## Папки

```
├── index.html, answers.html, части 1–4 .html   корейский (основной); изображения и скрипты встроены в файлы
├── en/ zh/ ja/ uz/ ru/   переведённые страницы с теми же именами файлов
├── code/      код scikit-learn для Colab / Jupyter (common.py и f0–f4.py)
├── data/      fish_market_x10.csv
├── prompts/   полный промпт для ИИ-помощника при изменении кода или данных
├── LICENSE.md
└── .nojekyll
```

## Данные

Источник — [Kaggle Fish Market](https://www.kaggle.com/datasets/vipullrathod/fish-market) (вес, длины, высота и толщина 159 рыб 7 видов). С помощью нормального распределения, сохраняющего среднее и дисперсию каждого вида, данные расширены до 1 590 строк; после удаления 1 строки с весом 0 и 35 точных дубликатов используется 1 554 рыбы. Рыбы, полученные из одного исходного образца, имеют одинаковый `seed_id`, и все оценки вычислены с таким разбиением, при котором эта группа никогда не делится между обучающей и тестовой выборками.
