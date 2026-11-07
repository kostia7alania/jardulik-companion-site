(() => {
  const botTarget = document.querySelector('[data-bot-target]');
  if (botTarget) {
    const destination = new URL(botTarget.href);
    if (new URLSearchParams(window.location.search).get('source') === 'guide_connect') {
      destination.searchParams.set('start', 'guide_connect');
    }
    window.location.replace(destination.href);
    return;
  }

  const next = document.querySelector('#demo-next');
  const favorite = document.querySelector('#demo-favorite');
  if (!next || !favorite) return;

  const profiles = [
    { name: 'Алина, 26', place: 'Владикавказ · 170 см', bio: 'Люблю прогулки в горах, хорошие книги и разговоры, после которых забываешь смотреть на время.', goal: 'Серьёзные отношения' },
    { name: 'Ксения, 27', place: 'Санкт-Петербург · 168 см', bio: 'Могу показать любимые книжные, приготовить завтрак и увлечённо рассказывать про последнюю поездку.', goal: 'Знакомства и общение' },
  ];
  let current = 0;
  const saved = new Set();
  const status = document.querySelector('#demo-status');

  const updateFavorite = () => {
    const isSaved = saved.has(current);
    favorite.setAttribute('aria-pressed', String(isSaved));
    favorite.querySelector('span').textContent = isSaved ? 'В избранном' : 'В избранное';
  };

  favorite.addEventListener('click', () => {
    if (saved.has(current)) saved.delete(current);
    else saved.add(current);
    updateFavorite();
    status.textContent = saved.has(current)
      ? 'Пример: анкета добавлена в избранное. Данные сервиса не менялись.'
      : 'Пример: анкета убрана из избранного. Данные сервиса не менялись.';
  });

  next.addEventListener('click', () => {
    current = (current + 1) % profiles.length;
    const profile = profiles[current];
    document.querySelector('#demo-name').textContent = profile.name;
    document.querySelector('#demo-place').textContent = profile.place;
    document.querySelector('#demo-bio').textContent = profile.bio;
    document.querySelector('#demo-goal').textContent = profile.goal;
    updateFavorite();
    status.textContent = `Пример: ${profile.name}. Все данные вымышлены.`;
  });
})();
