let inputNome = document.querySelector('#nome')
let inputEmail = document.querySelector('#email')
let textareaMensagem = document.querySelector('#mensagem')
let button = document.querySelector('#enviar')
let show_button = document.querySelector('#carregamento')
let form = document.querySelector('form')
let tituloForm = document.querySelector('#tituloFormulario')
let input = document.querySelectorAll('input')
let check_nome 
let check_email 
let check_mensagem 

inputNome.addEventListener('keyup',()=>{
   
    if(inputNome.value.length >2){
        inputNome.style.borderColor = "green"
        check_nome = true
    } else {
    inputNome.style.borderColor = "red"
    check_nome = false 
    }

    if(inputNome.value == ""|| inputNome.value == null){
        inputNome.style.borderColor = "#ccc"
    }
    if(check_nome && check_email && check_mensagem){
        button.style.display = 'block'
    } else {
        button.style.display = 'none'
    }

})

inputEmail.addEventListener("keyup", ()=>{

    if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1  ){

        inputEmail.style.borderColor = 'red'
        check_email = false
    } else {
        inputEmail.style.borderColor = 'green'
        
        if(inputEmail.style.borderColor = 'green'){
            check_email = true
        }
    
        
    }
    
    
    if(inputEmail.value == "" || inputEmail.value == null){
        inputEmail.style.borderColor = '#ccc'
    }

    if(check_nome && check_email && check_mensagem){
        button.style.display = 'block'
    } else {
        button.style.display = 'none'
    }}
)

textareaMensagem.addEventListener('keydown', () =>{

    if(textareaMensagem.value.length <=100 && textareaMensagem.value.length >0){

        textareaMensagem.style.borderColor = 'green'
        check_mensagem = true
    }else{
        textareaMensagem.style.borderColor = 'red'
        check_mensagem = false
    }   
    
     

    if(textareaMensagem.value == "" || textareaMensagem.value == null){

        textareaMensagem.style.borderColor = "#ccc"
    }

    if(check_nome && check_email && check_mensagem){
        button.style.display = 'block'
    } else {
        button.style.display = 'none'
    }
})



form.addEventListener('submit', ()=>{

    if(inputEmail.style.borderColor == 'green' && inputNome.style.borderColor == "green"&& textareaMensagem.style.borderColor == 'green'){
    show_button.style.display = 'flex'
    form.style.display = 'none'
    tituloFormulario.style.display = 'none'
    // button.style.display = 'block'
    } else {
    alert('Preencha todos os campos')


    }   
    
})
