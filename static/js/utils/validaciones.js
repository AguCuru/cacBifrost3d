// ---------------- Validacion Resgitro---------------- //

function validateRegister() {
  // validacione form register.js

  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formRegister");

    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Evitar que el formulario se envíe automáticamente

      // Validar el nombre
      const firstname = document.getElementById("firstname");
      const errorFirstname = document.getElementById("error-firstname");
      if (firstname.value.trim() === "") {
        errorFirstname.textContent = "Por favor, ingresa tu nombre.";
        firstname.focus();
        return false;
      } else {
        errorFirstname.textContent = "";
      }

      // Validar el apellido
      const lastname = document.getElementById("lastname");
      const errorLastname = document.getElementById("error-lastname");
      if (lastname.value.trim() === "") {
        errorLastname.textContent = "Por favor, ingresa tu apellido.";
        lastname.focus();
        return false;
      } else {
        errorLastname.textContent = "";
      }

      // Validar el email
      const email = document.getElementById("email");
      const errorEmail = document.getElementById("error-email");
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email.value.trim())) {
        errorEmail.textContent = "Por favor, ingresa un email válido.";
        email.focus();
        return false;
      } else {
        errorEmail.textContent = "";
      }

      // Validar la contraseña
      const password = document.getElementById("password");
      const errorPassword = document.getElementById("error-password");
      if (password.value.trim() === "") {
        errorPassword.textContent = "Por favor, ingresa tu contraseña.";
        password.focus();
        return false;
      } else {
        errorPassword.textContent = "";
      }

      // Validar que las contraseñas coincidan
      const password2 = document.getElementById("password2");
      const errorPassword2 = document.getElementById("error-password2");
      if (password2.value.trim() !== password.value.trim()) {
        errorPassword2.textContent = "Las contraseñas no coinciden.";
        password2.focus();
        return false;
      } else {
        errorPassword2.textContent = "";
      }

      // Validar la fecha de nacimiento
      // Obtener la fecha de nacimiento del campo
      const birthdateInput = document.getElementById("birthdate");
      const birthdate = new Date(birthdateInput.value);

      // Obtener la fecha actual
      const today = new Date();

      // Calcular la edad restando el año actual menos el año de nacimiento
      const age = today.getFullYear() - birthdate.getFullYear();

      // Si el mes actual es menor que el mes de nacimiento, o si es el mismo mes pero el día actual es menor que el día de nacimiento, se resta un año
      if (
        today.getMonth() < birthdate.getMonth() ||
        (today.getMonth() === birthdate.getMonth() &&
          today.getDate() < birthdate.getDate())
      ) {
        age--;
      }

      // Si la edad es menor de 18, muestra un mensaje de error
      if (age < 18) {
        const errorBirthdate = document.getElementById("error-birthdate");
        errorBirthdate.textContent = "Debes ser mayor de 18 años.";
        birthdateInput.focus(); // Dar foco al campo de fecha de nacimiento
        return false;
      } else {
        // Si la edad es 18 o mayor, elimina cualquier mensaje de error
        const errorBirthdate = document.getElementById("error-birthdate");
        errorBirthdate.textContent = "";
      }

      // Validar el país (puedes agregar tu lógica de validación aquí)

      // Validar los términos y condiciones
      const terms = document.getElementById("terms");
      const errorTerms = document.getElementById("error-terms");
      if (!terms.checked) {
        errorTerms.textContent = "Debes aceptar los términos y condiciones.";
        terms.focus();
        return false;
      } else {
        errorTerms.textContent = "";
      }

      // Si todas las validaciones son exitosas, el formulario se enviará normalmente
      form.submit();
    });
  });
}
validateRegister();
// ---------------- Validacion Login ---------------- //

function validateLogin() {
  // validacione form login.js

  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("formLogin");

    form.addEventListener("submit", function (event) {
      event.preventDefault(); // Evitar que el formulario se envíe automáticamente

      // Validar el email
      const email = document.getElementById("email");
      const errorEmail = document.getElementById("error-email");
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email.value.trim())) {
        errorEmail.textContent = "Por favor, ingresa un email válido.";
        email.focus();
        return false;
      } else {
        errorEmail.textContent = "";
      }

      // Validar la contraseña
      const password = document.getElementById("password");
      const errorPassword = document.getElementById("error-password");
      if (password.value.trim() === "") {
        errorPassword.textContent = "Por favor, ingresa tu contraseña.";
        password.focus();
        return false;
      } else {
        errorPassword.textContent = "";
      }

      // Si todas las validaciones son exitosas, el formulario se enviará normalmente
      form.submit();
    });
  });
}
validateLogin();
