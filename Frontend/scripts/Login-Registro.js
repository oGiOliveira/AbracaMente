document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const registroForm = document.getElementById('registroForm');

  if (registroForm) {
    registroForm.addEventListener('submit', e => {
      e.preventDefault();

      const nome = registroForm.nome.value.trim();
      const email = registroForm.email.value.trim();
      const senha = registroForm.senha.value.trim();
      const confirmarSenha = registroForm.confirmarSenha.value.trim();

      if (!nome || !email || !senha || !confirmarSenha) {
        alert('Por favor, preencha todos os campos.');
        return;
      }

      if (senha !== confirmarSenha) {
        alert('As senhas não coincidem.');
        return;
      }

      // Verifica se o e-mail já está cadastrado
      if (localStorage.getItem(email)) {
        alert('Este e-mail já está cadastrado.');
        return;
      }

      // Cria objeto com os dados do usuário
      const usuario = {
        nome: nome,
        email: email,
        senha: senha
      };

      // Armazena no localStorage
      localStorage.setItem(email, JSON.stringify(usuario));

      alert('Cadastro realizado com sucesso!');
      window.location.href = 'login.html';
    });
  }

  if (loginForm) {
    loginForm.addEventListener('submit', e => {
      e.preventDefault();

      const email = loginForm.email.value.trim();
      const senha = loginForm.senha.value.trim();

      if (!email || !senha) {
        alert('Por favor, preencha todos os campos.');
        return;
      }

      const usuario = localStorage.getItem(email);

      if (!usuario) {
        alert('Usuário não encontrado.');
        return;
      }

      const dados = JSON.parse(usuario);

      if (dados.senha !== senha) {
        alert('Senha incorreta.');
        return;
      }

      alert(`Bem-vindo, ${dados.nome}!`);
      // Aqui pode redirecionar para a área logada
      // Exemplo: window.location.href = 'dashboard.html';
    });
  }
});
