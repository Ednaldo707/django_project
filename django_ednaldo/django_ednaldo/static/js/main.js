// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    // 1. Funcionalidade do Menu Mobile
    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            const icon = menuToggle.querySelector('i');
            
            // Troca o ícone (Hamburger <-> X)
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }

    // 2. Alerta de Confirmação para Rotas Futuras (Exemplo)
    const cardsParaDesenvolver = document.querySelectorAll('.homepage-grid a:not([href*="eventos"])');

    cardsParaDesenvolver.forEach(card => {
        card.addEventListener('click', function(e) {
            // Verifica se o link ainda está apontando para '#'
            if (this.getAttribute('href') === '#') {
                e.preventDefault();
                const titulo = this.querySelector('h2').textContent;
                
                // Exemplo de alerta simples
                alert(`A seção "${titulo}" será implementada em breve. Aguarde as próximas atualizações!`);
            }
        });
    });

    // 3. Exemplo de Alerta em Detalhe do Evento (se fosse uma página de inscrição)
    // Se você tivesse um botão .btn-inscrever, o código seria similar:
    /*
    const btnInscrever = document.getElementById('btn-inscrever');
    if (btnInscrever) {
        btnInscrever.addEventListener('click', function(e) {
            e.preventDefault();
            const confirmacao = confirm('Deseja realmente se inscrever neste evento?');
            if (confirmacao) {
                // Lógica de inscrição (ex: submit de formulário)
                alert('Inscrição realizada com sucesso!');
            }
        });
    }
    */
});