/* Truevine Express Limited: site behaviour. No dependencies. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var body = document.body;
  var header = document.querySelector(".site-header");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Header state on scroll */
  function onScroll() {
    if (!header) return;
    header.classList.toggle("is-scrolled", window.scrollY > 24);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* Mobile menu */
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  function setMenu(open) {
    body.classList.toggle("menu-open", open);
    if (toggle) toggle.setAttribute("aria-expanded", String(open));
    if (menu) { if (open) menu.removeAttribute("inert"); else menu.setAttribute("inert", ""); }
    if (open && menu) { var first = menu.querySelector("a"); if (first) first.focus({ preventScroll: true }); }
  }
  if (toggle) toggle.addEventListener("click", function () { setMenu(!body.classList.contains("menu-open")); });
  if (menu) menu.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && body.classList.contains("menu-open")) { setMenu(false); toggle && toggle.focus(); }
  });
  window.addEventListener("resize", function () { if (window.innerWidth > 1100 && body.classList.contains("menu-open")) setMenu(false); });

  /* Reveal on scroll */
  var items = document.querySelectorAll(".reveal");
  if (reduced || !("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* Pause SVG (SMIL) animations for reduced motion */
  if (reduced) document.querySelectorAll("svg").forEach(function (s) { if (s.pauseAnimations) s.pauseAnimations(); });

  /* Footer year */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* Contact form: AJAX submit to FormSubmit, with plain POST fallback when JS is off */
  var form = document.getElementById("consult-form");
  if (form) {
    var status = form.querySelector(".form-status");
    var btn = form.querySelector('button[type="submit"]');
    var btnLabel = btn ? btn.innerHTML : "";
    function show(kind, msg) { status.className = "form-status " + kind; status.textContent = msg; status.setAttribute("role", kind === "err" ? "alert" : "status"); }

    /* Pre-select a service from ?service= */
    var q = new URLSearchParams(location.search).get("service");
    if (q) { var opt = form.querySelector('input[name="Service"][value="' + q + '"]'); if (opt) opt.checked = true; }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (form.querySelector('input[name="_honey"]').value) return;
      var data = {};
      new FormData(form).forEach(function (v, k) {
        if (k === "Service") { data[k] = data[k] ? data[k] + ", " + v : v; } else { data[k] = v; }
      });
      if (!data.Service) data.Service = "Not specified";
      btn.disabled = true;
      btn.innerHTML = "Sending&hellip;";
      fetch(form.getAttribute("data-ajax"), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (res.ok && (res.j.success === "true" || res.j.success === true)) {
            form.reset();
            show("ok", "Thank you. Your request is with our team and we will reply within one business day. For anything urgent, call 0703 590 9781.");
          } else {
            throw new Error((res.j && res.j.message) || "Submission failed");
          }
        })
        .catch(function () {
          show("err", "We could not send your message just now. Please email truevineexpressltd@gmail.com or call 0703 590 9781 and we will pick it up straight away.");
        })
        .finally(function () { btn.disabled = false; btn.innerHTML = btnLabel; });
    });
  }
})();
