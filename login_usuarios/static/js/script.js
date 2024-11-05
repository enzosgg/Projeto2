const form = document.getElementById("form");
const CPF = document.getElementById("CPF");
const Senha = document.getElementById("Senha");
const errorMessage = document.getElementById("error-message"); 

if (errorMessage && errorMessage.innerText.trim() !== "") {
  errorMessage.style.display = "block"; 
  errorMessage.style.color = "red";
}


form.addEventListener("submit", (event) => {
  event.preventDefault();
  checkForm();
})

CPF.addEventListener("blur", () => {
  checkInputCPF();
})

Senha.addEventListener("blur", () => {
  checkInputSenha();
})

CPF.addEventListener("keypress", (event) => {
  const charCode = event.which ? event.which : event.keyCode;
  
  if (charCode < 48 || charCode > 57) {
    event.preventDefault();
  }

  let CPFLength = CPF.value.length;
  if (CPFLength === 3 || CPFLength === 7) {
    CPF.value += ".";
  } else if (CPFLength === 11) {
    CPF.value += "-";
  }
});


function checkInputCPF(){
  const CPFValue = CPF.value;

  if(CPFValue === ""){
    errorInput(CPF, "*Campo obrigatório")
  }else{
    const formItem = CPF.parentElement;
    formItem.className = "formulario"
  }

}

function checkInputSenha(){
  const SenhaValue = Senha.value;

  if(SenhaValue === ""){
    errorInput(Senha, "*Campo obrigatório")
  }else{
    const formItem = Senha.parentElement;
    formItem.className = "formulario"
  }
}

function checkForm(){
  checkInputCPF();
  checkInputSenha();

  const formItems = form.querySelectorAll(".formulario");

  const isValid = [...formItems].every( (item) => {
    return item.className === "formulario";
  });

  if (isValid) {

    form.submit(); 
  }
}


function errorInput(input, message){
  const formItem = input.parentElement;
  const textMessage = formItem.querySelector("a")

  textMessage.innerText = message;

  formItem.className = "formulario error"
}