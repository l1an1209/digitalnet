// Menu mobile
const nav = document.querySelector('.main-nav');
const toggle = document.querySelector('.nav-toggle');
if (nav && toggle) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
}

// Header shrink on scroll + back-to-top visibility
const header = document.querySelector('.site-header');
const backToTop = document.querySelector('.back-to-top');
const onScroll = () => {
  const y = window.scrollY || document.documentElement.scrollTop;
  if (header) header.classList.toggle('scrolled', y > 12);
  if (backToTop) backToTop.classList.toggle('show', y > 300);
};
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Active nav link based on hash
const setActiveLink = () => {
  const hash = location.hash || '#topo';
  document.querySelectorAll('.nav-list a').forEach(a => a.classList.toggle('active', a.getAttribute('href') === hash));
};
window.addEventListener('hashchange', setActiveLink);
setActiveLink();

// Abas de preços (placeholder para possível futura separação)
document.querySelectorAll('.pricing-tabs .tab-button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.pricing-tabs .tab-button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    // Aqui você pode filtrar cards por data-attr se desejar.
  });
});

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
        history.replaceState(null, '', id);
        setActiveLink();
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
  const steps = 50; const inc = Math.max(1, Math.floor(target / steps));
  const tick = () => {
    current += inc;
    if (current >= target) { el.textContent = String(target); return; }
    el.textContent = String(current);
    requestAnimationFrame(tick);
  };
  const io = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { tick(); io.disconnect(); }
  });
  io.observe(el);
});

// Coverage search filter
const coverageSearch = document.querySelector('.coverage-search');
const coverageList = document.querySelector('#coverageList');
const coverageCount = document.querySelector('.coverage-count');
if (coverageSearch && coverageList) {
  const items = Array.from(coverageList.querySelectorAll('.coverage-item'));
  const update = () => {
    const q = coverageSearch.value.trim().toLowerCase();
    let visible = 0;
    items.forEach(li => {
      const show = !q || li.dataset.name.includes(q);
      li.style.display = show ? '' : 'none';
      if (show) visible += 1;
    });
    if (coverageCount) coverageCount.textContent = visible === items.length ? `${visible} bairros` : `${visible} encontrados`;
  };
  coverageSearch.addEventListener('input', update);
  update();
}

// CEP checker -> direciona para WhatsApp com CEP
const cepForm = document.getElementById('cepForm');
const cepInput = document.getElementById('cepInput');
const cepError = document.getElementById('cepError');
const city = document.querySelector('#cobertura .coverage')?.dataset.city || '';
function normalizeCEP(v){
  const n = (v||'').replace(/\D/g,'').slice(0,8);
  if (n.length >= 5) return n.slice(0,5)+'-'+n.slice(5);
  return n;
}
if (cepInput){
  cepInput.addEventListener('input',()=>{cepInput.value = normalizeCEP(cepInput.value)});
}
if (cepForm){
  cepForm.addEventListener('submit', async ()=>{
    if (!cepInput) return;
    const raw = (cepInput.value||'').replace(/\D/g,'');
    if (raw.length !== 8){
      if (cepError) cepError.textContent = 'CEP inválido. Use 8 dígitos.';
      return;
    }
    if (cepError) cepError.textContent = '';
    const formatted = normalizeCEP(raw);
    const resultBox = document.getElementById('cepResult');
    const logEl = document.getElementById('cepLogradouro');
    const bairroEl = document.getElementById('cepBairro');
    const cidEl = document.getElementById('cepCidade');
    const statusEl = document.getElementById('cepStatus');
    try{
      const resp = await fetch(`https://viacep.com.br/ws/${raw}/json/`);
      const data = await resp.json();
      if (data.erro){
        if (cepError) cepError.textContent = 'CEP não encontrado.';
        if (resultBox) resultBox.hidden = true;
        return;
      }
      if (resultBox) resultBox.hidden = false;
      if (logEl) logEl.textContent = data.logradouro || '—';
      if (bairroEl) bairroEl.textContent = data.bairro || '—';
      if (cidEl) cidEl.textContent = `${data.localidade || ''}/${data.uf || ''}`;
      const items = document.querySelectorAll('#coverageList .coverage-item');
      let matched = false;
      items.forEach(li => {
        const isMatch = data.bairro && li.dataset.name === String(data.bairro).toLowerCase();
        li.style.outline = isMatch ? '2px solid var(--primary)' : '';
        if (isMatch) matched = true;
      });
      if (statusEl) statusEl.textContent = matched ? 'Bairro atendido pela Digital Net.' : 'Bairro não listado. Consulte nossa equipe no WhatsApp.';
      const msg = encodeURIComponent(`Olá! Meu CEP é ${formatted} (${data.logradouro || ''}, ${data.bairro || ''}, ${data.localidade || ''}/${data.uf || ''}). Gostaria de saber se há cobertura em ${city}.`);
      const wa = document.querySelector('.contact-methods a[href^="https://wa.me/"]');
      const base = wa ? wa.getAttribute('href').split('?')[0] : `https://wa.me/`;
      const url = `${base}?text=${msg}`;
      window.open(url, '_blank');
    }catch(e){
      if (cepError) cepError.textContent = 'Falha ao consultar CEP. Tente novamente.';
      if (resultBox) resultBox.hidden = true;
    }
  });
}

