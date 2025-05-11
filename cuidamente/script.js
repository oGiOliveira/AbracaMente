document.addEventListener('DOMContentLoaded', () => {
  // Botão de alerta
  const alertButton = document.getElementById('alertButton');
  if (alertButton) {
    alertButton.addEventListener('click', () => {
      alert('Você clicou no botão!');
    });
  }

  // Botões da FAQ
  const faqButtons = document.querySelectorAll('.faq-item button');
  faqButtons.forEach(button => {
    button.addEventListener('click', () => {
      const resposta = button.nextElementSibling;
      resposta.style.display = resposta.style.display === 'block' ? 'none' : 'block';
    });
  });
});

