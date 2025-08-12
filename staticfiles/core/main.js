// Menu mobile
const nav = document.querySelector('.main-nav');
const toggle = document.querySelector('.nav-toggle');
if (nav && toggle) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
}

// Accordion FAQ
document.querySelectorAll('[data-accordion] .item .q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.item');
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!expanded));
    item.classList.toggle('open');
  });
});

// Reveal on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));

// Back to top smooth
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    const id = link.getAttribute('href');
    if (id && id.length > 1) {
      const target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });
});

// Theme toggle
const toggleTheme = document.querySelector('.toggle-theme');
const applyTheme = (t) => document.body.classList.toggle('light', t === 'light');
const saved = localStorage.getItem('theme');
if (saved) applyTheme(saved);
if (toggleTheme) {
  toggleTheme.addEventListener('click', () => {
    const isLight = document.body.classList.toggle('light');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
    toggleTheme.setAttribute('aria-pressed', String(isLight));
  });
}

// Simple animated counter
document.querySelectorAll('[data-count]').forEach(el => {
  const target = Number(el.getAttribute('data-count')) || 0;
  let current = 0;
  const step = Math.ceil(target / 60);
  const tick = () => {
    current += step;
    if (current >= target) { el.textContent = String(target); return; }
    el.textContent = String(current);
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { tick(); io.disconnect(); }
  });
  io.observe(el);
});

