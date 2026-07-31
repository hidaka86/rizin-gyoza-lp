// (仮)数値の流し込み — data.js の LP_DATA を data-bind 属性へ反映
(function () {
  var data = window.LP_DATA || {};
  document.querySelectorAll("[data-bind]").forEach(function (el) {
    var key = el.getAttribute("data-bind");
    if (Object.prototype.hasOwnProperty.call(data, key)) el.textContent = data[key];
  });
})();

// Reveal on scroll
(function () {
  var els = document.querySelectorAll(".reveal");
  if (document.body.classList.contains("ds-preview") || !("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("is-in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  els.forEach(function (el) { io.observe(el); });
})();

// Mobile nav toggle
(function () {
  var toggle = document.getElementById("navToggle");
  var links = document.getElementById("navLinks");
  if (!toggle || !links) return;
  toggle.addEventListener("click", function () {
    var open = links.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
  links.addEventListener("click", function (e) {
    if (e.target.tagName === "A") links.classList.remove("is-open");
  });
})();
