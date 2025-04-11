 

 // Inicializar o contador global para o total de ovos
 let totalQuantidade = 0;
    
 // Obter todos os botões "menos" e "mais"
 const buttons = document.querySelectorAll('.menosTres, .maisTres');

 // Adicionar comportamento para os botões de quantidade
 buttons.forEach(button => {
     button.addEventListener('click', function() {
         const ovoId = this.getAttribute('data-ovo-id');
         const quantidadeInput = document.getElementById('quantidadeTres_' + ovoId);
         
         if (!quantidadeInput) {
             console.error("Elemento de quantidade não encontrado para ovo ID:", ovoId);
             return;
         }

         let quantidade = parseInt(quantidadeInput.value);
         document.querySelector('#enviarTres').disabled = true
         if (this.classList.contains('menosTres')) {
             if (quantidade > 0) {
                 quantidadeInput.value = quantidade - 1;
                 totalQuantidade--;  // Decrementa o total de ovos selecionados
             }
         } else if (this.classList.contains('maisTres')) {
             if (totalQuantidade < 3) {
                 
                 quantidadeInput.value = quantidade + 1;
                 totalQuantidade++;  // Incrementa o total de ovos selecionados
             };
             
         }
         if(totalQuantidade == 3){
                    
                 let mais = document.querySelectorAll('.maisTres');
                 mais.forEach( classe => {
                     classe.classList.add('disabilitado');
                 })
                 document.querySelector('#enviarTres').disabled = false
             }
         else if(totalQuantidade < 3){
             
                 let mais = document.querySelectorAll('.maisTres');
                 mais.forEach( classe => {
                     classe.classList.remove('disabilitado');
                     window.href = '/itens#enviarTres'
                 })
             }
     });
 });
 let totalQuantidadeSeis = 0;
    
 // Obter todos os botões "menos" e "mais"
 const buttonsSeis = document.querySelectorAll('.menosSeis, .maisSeis');

 // Adicionar comportamento para os botões de quantidade
 buttonsSeis.forEach(button => {
     button.addEventListener('click', function() {
         const ovoId = this.getAttribute('data-ovo-id');
         const quantidadeInput = document.getElementById('quantidadeSeis_' + ovoId);
         
         if (!quantidadeInput) {
             console.error("Elemento de quantidade não encontrado para ovo ID:", ovoId);
             return;
         }

         let quantidade = parseInt(quantidadeInput.value);
         document.querySelector('#enviarSeis').disabled = true
         if (this.classList.contains('menosSeis')) {
             if (quantidade > 0) {
                 quantidadeInput.value = quantidade - 1;
                 totalQuantidadeSeis--;  // Decrementa o total de ovos selecionados
             }
         } else if (this.classList.contains('maisSeis')) {
             if (totalQuantidadeSeis < 6) {
                 
                 quantidadeInput.value = quantidade + 1;
                 totalQuantidadeSeis++;  // Incrementa o total de ovos selecionados
             };
             
         }
         if(totalQuantidadeSeis == 6){
                    
                 let mais = document.querySelectorAll('.maisSeis');
                 mais.forEach( classe => {
                     classe.classList.add('disabilitado');
                 })
                 document.querySelector('#enviarSeis').disabled = false
             }
         else if(totalQuantidadeSeis < 6){
             
                 let mais = document.querySelectorAll('.maisSeis');
                 mais.forEach( classe => {
                     classe.classList.remove('disabilitado');
                      window.href = '/itens#enviarSeis'
                 })
                 
             }
     });
 });

 document.getElementById('enviarSeis').addEventListener("click", () => {
   document.getElementById('enviarSeis').onsubmit;
 })
 document.getElementById('enviarTres').addEventListener("click", () => {
   document.getElementById('enviarTres').onsubmit;
 })
 function adicionaCarrinho(event, element){
   
   
    event.preventDefault(); 
    let id = element.getAttribute('data-id');
    
    element.classList.add("adicionado");
    setTimeout(() => {
        element.classList.remove("adicionado");
        console.log('aqui')
    }, 3850)

    console.log(id)
    fetch(`/adiciona_carrinho/${id}`)
        .then(() => {
                console.log('certo')
        })
        .catch(error =>{
            console.log('erro')
        });
}
 