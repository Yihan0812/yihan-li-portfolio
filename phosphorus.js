'use strict';
// Every mechanism remains visible when JavaScript is unavailable.
const explorer = document.querySelector('.mechanism-explorer');
if (explorer) {
  const tabs = [...explorer.querySelectorAll('[role="tab"]')];
  const views = [...explorer.querySelectorAll('[data-view]')];
  function select(tab, focus = false) {
    tabs.forEach(t => { const active = t === tab; t.setAttribute('aria-selected', String(active)); t.tabIndex = active ? 0 : -1; });
    views.forEach(v => { v.hidden = v.dataset.view !== tab.dataset.panel; });
    if (focus) tab.focus();
  }
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => select(tab));
    tab.addEventListener('keydown', e => {
      const moves = {ArrowRight: (i + 1) % tabs.length, ArrowLeft: (i - 1 + tabs.length) % tabs.length, Home: 0, End: tabs.length - 1};
      if (e.key in moves) { e.preventDefault(); select(tabs[moves[e.key]], true); }
    });
  });
  select(tabs[0]);
}
