const form = document.getElementById("form");
const CPF = document.getElementById("CPF");
const Senha = document.getElementById("Senha");

form.addEventListener("submit", (event) => {
  let isValid = true;

  if (CPF.value.trim() === "") {
    errorInput(CPF, "Campo obrigatório*");
    isValid = false;
  } else {
    clearError(CPF);
  }

  if (Senha.value.trim() === "") {
    errorInput(Senha, "Campo obrigatório*");
    isValid = false;
  } else {
    clearError(Senha);
  }

  if (!isValid) {
    event.preventDefault();
  }
});

CPF.addEventListener("keypress", () => {
  let CPFLength = CPF.value.length;
  if (CPFLength === 3 || CPFLength === 7) {
    CPF.value += ".";
  } else if (CPFLength === 11) {
    CPF.value += "-";
  }
});

function errorInput(input, message) {
  const formItem = input.parentElement;
  const textMessage = formItem.querySelector("a");
  textMessage.innerText = message;
  formItem.className = "formulario error";
}

function clearError(input) {
  const formItem = input.parentElement;
  const textMessage = formItem.querySelector("a");
  textMessage.innerText = "";
  formItem.className = "formulario";
}
