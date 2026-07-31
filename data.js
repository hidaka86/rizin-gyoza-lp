// ===================================================================
// (仮)数値の一元管理。確定値が出たらここだけ差し替える。
// HTML側は <span data-bind="キー">フォールバック値</span> で参照。
// ===================================================================
window.LP_DATA = {
  // 栄養成分(仮)
  "nutrition.proteinPerPiece": "4",      // g/個
  "nutrition.proteinPerMeal": "40",      // g/10個
  "nutrition.chickenEquiv": "約200g",    // 鶏むね肉換算
  "nutrition.competitorProtein": "約2",  // g/個(一般的な冷凍餃子)
  "nutrition.fatPerMeal": "12",          // g/10個
  "nutrition.kcalPerMeal": "350",        // kcal/10個

  // 価格(仮・すべて税込)
  "price.single": "3,980",
  "price.membersTotal": "11,940",
  "price.membersMonthly": "3,980",
  "price.premiumTotal": "33,000",
  "price.premiumMonthly": "2,750",
  "price.perMeal": "約100"
};
