'use strict';
const copyButton = document.querySelector('#copy-email');
const status = document.querySelector('#copy-status');
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText('yl10023@ic.ac.uk');
    status.textContent = 'Email copied.';
  } catch {
    status.textContent = 'Email: yl10023@ic.ac.uk';
  }
});
const navigationLinks = [...document.querySelectorAll('nav a')];
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navigationLinks.forEach(link => {
          if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    });
  }, { rootMargin: '-10% 0px -60% 0px', threshold: 0 });
  document.querySelectorAll('#research, #about, #contact').forEach(section => observer.observe(section));
}
