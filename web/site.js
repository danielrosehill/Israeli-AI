// Filter the cards on the current page as you type. Purely client side; the
// header input is present on every page and hides non-matching cards, then
// hides any section heading / grid left with nothing under it.
(function () {
  var input = document.getElementById('site-search');
  if (!input) return;

  var cards = Array.prototype.slice.call(document.querySelectorAll('[data-entry], .nav-card'));
  if (!cards.length) {
    input.placeholder = 'Filter…';
    input.disabled = true;
    return;
  }

  var empty = document.createElement('p');
  empty.className = 'no-results';
  empty.textContent = 'No entries on this page match that filter.';
  document.getElementById('main').appendChild(empty);

  var haystacks = cards.map(function (c) {
    return (c.textContent || '').toLowerCase();
  });

  function apply() {
    var q = input.value.trim().toLowerCase();
    var shown = 0;

    cards.forEach(function (card, i) {
      var hit = !q || haystacks[i].indexOf(q) !== -1;
      card.style.display = hit ? '' : 'none';
      if (hit) shown++;
    });

    // Collapse grids and their preceding heading when everything in them is hidden.
    document.querySelectorAll('.card-grid, .nav-grid').forEach(function (grid) {
      var any = Array.prototype.some.call(grid.children, function (c) {
        return c.style.display !== 'none';
      });
      grid.style.display = any ? '' : 'none';
      var heading = grid.previousElementSibling;
      while (heading && !/^H[1-6]$/.test(heading.tagName)) {
        heading = heading.previousElementSibling;
      }
      if (heading && heading.className.indexOf('section-heading') !== -1) {
        heading.style.display = any || !q ? '' : 'none';
      }
    });

    empty.classList.toggle('show', q !== '' && shown === 0);
  }

  input.addEventListener('input', apply);

  // "/" focuses the filter, Escape clears it.
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== input) {
      e.preventDefault();
      input.focus();
    } else if (e.key === 'Escape' && document.activeElement === input) {
      input.value = '';
      apply();
      input.blur();
    }
  });
})();
