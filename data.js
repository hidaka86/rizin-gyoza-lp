// ===================================================================
// 価格・成分値の一元管理。確定値が出たらここだけ差し替える。
// HTML側は <span data-bind="キー">フォールバック値</span> で参照。
// 栄養値: 成分内容_プロテイン餃子_20260613.pdf(配合設計値)より
// ===================================================================
window.LP_DATA = {
  // 栄養成分(1個あたり・2026年6月時点の配合設計値)
  "nutrition.kcalPerPiece": "46",
  "nutrition.proteinPerPiece": "4.7",   // g/個
  "nutrition.fatPerPiece": "0.8",       // g/個
  "nutrition.carbsPerPiece": "5.2",     // g/個
  "nutrition.saltPerPiece": "0.2",      // g/個
  // 1食10個あたり(上記×10)
  "nutrition.proteinPerMeal": "47",
  "nutrition.fatPerMeal": "8",
  "nutrition.kcalPerMeal": "460",
  "nutrition.saltPerMeal": "2.0",
  "nutrition.chickenEquiv": "約200g",   // 鶏むね肉換算(47g÷約23g/100g)
  "nutrition.competitorProtein": "約2", // g/個(一般的な冷凍餃子・仮)

  // 価格(仮・すべて税込)
  "price.single": "3,980",
  "price.membersTotal": "11,940",
  "price.membersMonthly": "3,980",
  "price.premiumTotal": "33,000",
  "price.premiumMonthly": "2,750",
  "price.perMeal": "約100"
};
