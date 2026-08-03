# RIZIN餃子 — 販売LP「Fight. Eat. Repeat.」

RIZIN公認の高タンパク冷凍餃子の販売LP(静的HTML/CSS/JS、将来Shopify移行想定)。
`~/Desktop/rizin-gyoza`(事業提案LP・機密系数値あり)とは別物。機密情報(配分モデル・原価・事業数値)は載せないこと。

## 構成

- `src/sections/*.html` — セクション断片(**編集はここ**)。FV/餃子の良さ/成分ロジック/選手/単品/サブスク/Tシャツ/FAQ/フッター法務 の9枚
- `build.py` — `python3 build.py` で `index.html` とClaude Design用プレビュー(`hero.html` など)を生成。ナビもここで管理
- `data.js` — **(仮)の価格・栄養成分値を一元管理**。確定値が出たらここだけ差し替え(HTML側は `data-bind` 属性で参照)
- `styles.css` / `main.js` — 共通スタイル・スクリプト(黒×赤×白、スマホファースト)
- `assets/` — 画像。選手写真・商品撮影素材はプレースホルダー運用中

## ワークフロー

1. `src/sections/` / `styles.css` / `data.js` を編集
2. `python3 build.py`
3. ローカル確認: launch.json の `rizin-gyoza-lp`(port 8940)。スマホ幅を優先確認
4. Claude Designへ同期: DesignSyncで finalize_plan → write_files
   - プロジェクト: 「RIZIN餃子 LP」 projectId `6edba41c-a6f1-49ff-bacd-f6a2284c8042`

## 他社比較のメモ(LP上は匿名表記)

- A社 = 味の素「プロテイン餃子」: たんぱく質 約4.2g/個・脂質 約1.4g/個(仮)
- B社 = マッスルギョーザ: たんぱく質 約2.2g/個・脂質 非公開(仮)
- 大阪王将のプロテイン餃子: 数値入手後に追加検討
- いずれも提案資料由来の参考値。公開前に各社公表値の再確認+比較広告の法務チェック必須

## 表現ルール

- 効果効能の断定表現(「筋肉がつく」「疲労回復」等)は使用禁止。一般論+成分事実のみ
- 価格はすべて税込表記で統一
- 選手写真・氏名・コメントは使用許諾取得まではダミーのまま(04-fighters.html冒頭のコメント参照)

## 後日差し替えリスト((仮)の解消)

1. 栄養成分表示データ(タンパク質・脂質・kcal)→ `data.js`
2. Members/Premiumの確定金額・期間・自動更新条件 → `data.js` + 06-plans.html
3. 工場・製法のこだわり文言 → 02-taste.html
4. 選手コメント・写真(許諾済み)→ 04-fighters.html
5. 商品・Tシャツの撮影素材 → 02/05/07 の `.ph` プレースホルダー
6. 特商法の正式表記 → 09-footer.html
7. LINE・購入ボタンの実URL
