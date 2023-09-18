function youreSure() {
if (confirm("Você tem certeza?")) {
  return true;
} else {
  return false;
}
}

function toggleOptions(bikeID) {
  const bikeArticle = document.querySelector(`.bikes[value="${bikeID}"]`);
  const opcoesArticle = document.querySelector(`.opcoes[value="${bikeID}"]`);

  if (!bikeArticle.classList.contains('hidden')) {
    bikeArticle.classList.add('hidden');
    opcoesArticle.classList.remove('hidden');
  } else {
    opcoesArticle.classList.add('hidden');
    bikeArticle.classList.remove('hidden');
  }
}

const bikeButtons = document.querySelectorAll('.button-light#bike-button');
bikeButtons.forEach((button) => {
  const bikeID = button.parentElement.getAttribute('value')
  button.addEventListener('click', () => toggleOptions(bikeID));
});

const opcoesButtons = document.querySelectorAll('.button-light#opcoes-button');
opcoesButtons.forEach((button) => {
  const bikeID = button.parentElement.getAttribute('value');
  button.addEventListener('click', () => toggleOptions(bikeID));
});