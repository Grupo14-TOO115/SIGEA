const el = document.getElementById('estado_civil');

const card = document.getElementById('card');

el.addEventListener('change', function handleChange(event) {
  if (event.target.value === 'casado') {
    card.style.display = 'block';
  } else {
    card.style.display = 'none';
  }
});