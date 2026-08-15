/* =====================================================================
   Memoria – Interaktivität (Vanilla)
   Ersetzt die Claude-Design-Runtime. Verhalten exakt wie im Export
   (siehe CLAUDE.md §4).
   ===================================================================== */

const reduceMotion = window.matchMedia(
  '(prefers-reduced-motion: reduce)',
).matches;
const MOBILE_QUERY = window.matchMedia('(max-width: 999px)');

function ready(fn: () => void) {
  if (document.readyState !== 'loading') fn();
  else document.addEventListener('DOMContentLoaded', fn);
}

/* --- Reveal-on-Scroll ------------------------------------------------ */
function setupReveal() {
  document.documentElement.classList.remove('om-nojs');
  const nodes = Array.from(
    document.querySelectorAll<HTMLElement>('[data-reveal]'),
  );
  if (!('IntersectionObserver' in window) || reduceMotion) {
    nodes.forEach((n) => n.classList.add('om-in'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add('om-in');
          io.unobserve(e.target);
        }
      });
    },
    { rootMargin: '0px 0px -6% 0px', threshold: 0.05 },
  );
  nodes.forEach((n) => io.observe(n));
  // Above-the-fold sofort einblenden.
  setTimeout(() => {
    nodes.forEach((n) => {
      if (n.getBoundingClientRect().top < window.innerHeight)
        n.classList.add('om-in');
    });
  }, 60);
}

/* --- Mobile-Menü ----------------------------------------------------- */
function setupMenu() {
  const btn = document.querySelector<HTMLButtonElement>('[data-menubtn]');
  const panel = document.querySelector<HTMLElement>('[data-menupanel]');
  if (!btn || !panel) return;
  const header = btn.closest<HTMLElement>('.site-header');

  const close = () => {
    panel.classList.remove('open');
    btn.classList.remove('open');
    header?.classList.remove('header-open');
    btn.setAttribute('aria-expanded', 'false');
  };
  const toggle = () => {
    const open = panel.classList.toggle('open');
    btn.classList.toggle('open', open);
    header?.classList.toggle('header-open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  };

  btn.addEventListener('click', toggle);
  panel
    .querySelectorAll('a')
    .forEach((a) => a.addEventListener('click', close));
  // Beim Wechsel auf Desktop das Menü schließen.
  MOBILE_QUERY.addEventListener('change', (e) => {
    if (!e.matches) close();
  });
}

/* --- Zitat-Slider ---------------------------------------------------- */
type Quote = { text: string; author: string };

function setupQuotes() {
  const box = document.querySelector<HTMLElement>('[data-quotebox]');
  const textEl = document.querySelector<HTMLElement>('[data-quotetext]');
  const authorEl = document.querySelector<HTMLElement>('[data-quoteauthor]');
  const prev = document.querySelector<HTMLButtonElement>('[data-quoteprev]');
  const next = document.querySelector<HTMLButtonElement>('[data-quotenext]');
  const dataEl = document.querySelector<HTMLScriptElement>('[data-quotes]');
  if (!box || !textEl || !authorEl || !dataEl) return;

  let quotes: Quote[] = [];
  try {
    quotes = JSON.parse(dataEl.textContent || '[]');
  } catch {
    return;
  }
  if (quotes.length === 0) return;

  let index = 0;
  let timer: number | undefined;

  const render = () => {
    const q = quotes[index] || quotes[0];
    textEl.textContent = q.text;
    authorEl.textContent = q.author;
  };

  const go = (dir: number) => {
    const apply = () => {
      index = (index + dir + quotes.length) % quotes.length;
      render();
      requestAnimationFrame(() => {
        box.style.opacity = '1';
      });
    };
    box.style.opacity = '0';
    window.setTimeout(apply, 500);
    restart();
  };

  const restart = () => {
    if (timer) window.clearInterval(timer);
    timer = window.setInterval(() => go(1), 8000);
  };

  prev?.addEventListener('click', () => go(-1));
  next?.addEventListener('click', () => go(1));
  render();
  restart();
}

/* --- Parallax (Kontakt-Bild) ---------------------------------------- */
function setupParallax() {
  const img = document.querySelector<HTMLElement>('[data-parallax]');
  if (!img || !img.parentElement || reduceMotion) return;

  const update = () => {
    const parent = img.parentElement!;
    const r = parent.getBoundingClientRect();
    const vh = window.innerHeight;
    if (r.bottom < -200 || r.top > vh + 200) return;
    const p = (vh - r.top) / (vh + r.height);
    img.style.transform = `translate3d(0, ${((p - 0.5) * 14).toFixed(2)}%, 0)`;
  };
  return update;
}

/* --- Mobile-Sticky-Bar ---------------------------------------------- */
function setupStickyBar() {
  const bar = document.querySelector<HTMLElement>('[data-mobilebar]');
  const cta = document.querySelector<HTMLElement>('[data-herocta]');
  if (!bar) return;

  const update = () => {
    const mobile = MOBILE_QUERY.matches;
    const ctaVisible = cta
      ? cta.getBoundingClientRect().bottom > 0
      : false;
    bar.classList.toggle('visible', mobile && !ctaVisible);
  };
  return update;
}

/* --- Kontaktformular (FormSubmit.co) --------------------------------- */
function setupForm() {
  const form = document.querySelector<HTMLFormElement>('[data-contactform]');
  const note = document.querySelector<HTMLElement>('[data-formnote]');
  const submit = form?.querySelector<HTMLButtonElement>('button[type="submit"]');
  if (!form || !note) return;

  // Ziel (E-Mail oder FormSubmit-Hash) steht als data-Attribut am Formular.
  const target = form.dataset.target || '';

  // Rücksprungziel für den klassischen Versand auf die aktuelle Domain setzen
  // (funktioniert so auf Entwicklungs- und Live-Domain gleichermaßen).
  const nextField = form.querySelector<HTMLInputElement>('[data-next]');
  if (nextField && !nextField.value) {
    nextField.value = `${window.location.origin}/?gesendet=1#kontakt`;
  }

  // Bestätigung anzeigen, wenn wir nach klassischem Versand zurückkommen.
  if (new URLSearchParams(window.location.search).get('gesendet') === '1') {
    note.textContent = 'Danke – wir melden uns so schnell wie möglich bei Ihnen.';
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (!target) {
      note.textContent =
        'Der Formularversand ist noch nicht eingerichtet. Bitte rufen Sie uns an: 06201 7303041.';
      return;
    }

    if (submit) submit.disabled = true;
    note.textContent = 'Wird gesendet …';

    // Fällt der AJAX-Weg aus (z. B. weil die Adresse bei FormSubmit noch nicht
    // aktiviert ist), senden wir klassisch ab. Dabei zeigt FormSubmit die
    // Aktivierungsseite an bzw. verschickt die Aktivierungs-Mail.
    const fallbackSubmit = (reason: unknown) => {
      console.warn('[Kontaktformular] AJAX-Versand fehlgeschlagen:', reason);
      note.textContent = 'Wird gesendet …';
      form.submit(); // nativer Submit – löst diesen Handler nicht erneut aus
    };

    try {
      const res = await fetch(
        'https://formsubmit.co/ajax/' + encodeURIComponent(target),
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
          },
          body: JSON.stringify(Object.fromEntries(new FormData(form).entries())),
        },
      );
      const json = await res.json().catch(() => null);
      // FormSubmit liefert success als String "true" oder Boolean true.
      if (json && (json.success === true || json.success === 'true')) {
        form.reset();
        note.textContent =
          'Danke – wir melden uns so schnell wie möglich bei Ihnen.';
        if (submit) submit.disabled = false;
      } else {
        fallbackSubmit(json?.message || `HTTP ${res.status}`);
      }
    } catch (err) {
      fallbackSubmit(err);
    }
  });
}

/* --- Copyright-Jahr automatisch --------------------------------------- */
function setupYear() {
  const y = String(new Date().getFullYear());
  document
    .querySelectorAll<HTMLElement>('[data-year]')
    .forEach((el) => (el.textContent = y));
}

/* --- Init ------------------------------------------------------------ */
ready(() => {
  setupReveal();
  setupMenu();
  setupQuotes();
  setupForm();
  setupYear();

  const parallax = setupParallax();
  const stickyBar = setupStickyBar();

  const onScroll = () => {
    parallax?.();
    stickyBar?.();
  };
  parallax?.();
  stickyBar?.();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', () => {
    stickyBar?.();
  });
});
