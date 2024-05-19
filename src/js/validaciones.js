// validaciones.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formRegister");

    form.addEventListener("submit", function(event) {
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

        // Validar la fecha de nacimiento (puedes agregar tu lógica de validación aquí)

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
