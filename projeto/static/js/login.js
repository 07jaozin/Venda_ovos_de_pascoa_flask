const container = document.querySelector('.container');
const registerBtn = document.querySelector('.register-btn');
const loginBtn = document.querySelector('.login-btn');
const tel = document.querySelectorAll('.tel');
const inputs = document.querySelectorAll('.input');

registerBtn.addEventListener('click', () => {
    container.classList.add('active');
    inputs.forEach( input =>{
        input.value = '';
    }
    );
})

loginBtn.addEventListener('click', () => {
    container.classList.remove('active');
    inputs.forEach( input =>{
        input.value = '';
    });
})


let total_input = 0;  
let todos_botoes = document.querySelectorAll('.tel');
todos_botoes.forEach( botao => {
botao.addEventListener("keydown", function(event){
    const teclasPermitidas = ["Backspace", "Delete", "ArrowLeft", "ArrowRight", "Tab"];

    // Se a tecla digitada não for um número (0-9) e não estiver na lista de teclas permitidas, bloqueia
    if (!event.key.match(/[0-9]/) && !teclasPermitidas.includes(event.key)) {
        event.preventDefault();
    }
    else if(event.key === " "){
        event.preventDefault();
    }
});
});
document.addEventListener("DOMContentLoaded", function() {
    const nomeLogin = document.getElementById('nome-login');
    const telefoneLogin = document.getElementById('telefone-login');
    const btnEntrar = document.getElementById('btn-entrar');
    
    const nome = document.getElementById('nome');
    const telefone = document.getElementById('telefone');
    const btnCadastrar = document.getElementById('btn-cadastrar');

    telefone.addEventListener("input", (event) => {
        let input = event.target.value;

    // Remove tudo que não for número
    input = input.replace(/\D/g, '');

    // Formata o número conforme o comprimento
    if (input.length <= 2) {
        input = `(${input}`;
    } else if (input.length <= 7) {
        input = `(${input.slice(0, 2)}) ${input.slice(2)}`;
    } else if (input.length <= 10) {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7)}`;
    } else {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7, 11)}`;
    }

    // Aplica a formatação correta e limpa os caracteres extras
    event.target.value = input;
    });
    telefoneLogin.addEventListener("input", (event) => {
        let input = event.target.value;

    // Remove tudo que não for número
    input = input.replace(/\D/g, '');

    // Formata o número conforme o comprimento
    if (input.length <= 2) {
        input = `(${input}`;
    } else if (input.length <= 7) {
        input = `(${input.slice(0, 2)}) ${input.slice(2)}`;
    } else if (input.length <= 10) {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7)}`;
    } else {
        input = `(${input.slice(0, 2)}) ${input.slice(2, 7)}-${input.slice(7, 11)}`;
    }

    // Aplica a formatação correta e limpa os caracteres extras
    event.target.value = input;
    });
    // Função para validar o telefone
    function validarTelefone(telefone) {
        return telefone.length === 15;
    }

   
    function verificarCampos() {
        
        if (nomeLogin.value && telefoneLogin.value && validarTelefone(telefoneLogin.value)) {
            btnEntrar.disabled = false;
            btnEntrar.classList.remove('desabilitado');
        } else {
            btnEntrar.disabled = true;
            btnEntrar.classList.add('desabilitado');

        }

       
        if (nome.value && telefone.value && validarTelefone(telefone.value)) {
            btnCadastrar.disabled = false;
            btnCadastrar.classList.remove('desabilitado');
        } else {
            btnCadastrar.disabled = true;
            btnCadastrar.classList.add('desabilitado');
        }
    }

    // Adicionando eventos para monitorar mudanças nos campos
    nomeLogin.addEventListener('input', verificarCampos);
    telefoneLogin.addEventListener('input', verificarCampos);
    nome.addEventListener('input', verificarCampos);
    telefone.addEventListener('input', verificarCampos);

    // Chamando a função ao carregar a página para garantir que os botões estejam corretamente configurados
    verificarCampos();
});
