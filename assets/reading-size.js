/* Reading preference is local to this browser; storage failure is harmless. */
(() => {
  const key = 'loptr-reading-size';
  let large = false;
  try { large = localStorage.getItem(key) === 'large'; } catch {}
  const apply = () => {
    document.documentElement.dataset.readingSize = large ? 'large' : 'default';
    document.querySelectorAll('[data-reading-toggle]').forEach(button => {
      button.hidden = false;
      button.setAttribute('aria-pressed', String(large));
    });
  };
  apply();
  document.querySelectorAll('[data-reading-toggle]').forEach(button => {
    button.addEventListener('click', () => {
      large = !large;
      apply();
      try { localStorage.setItem(key, large ? 'large' : 'default'); } catch {}
    });
  });
})();
