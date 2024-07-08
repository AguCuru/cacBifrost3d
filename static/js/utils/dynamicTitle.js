// ---------------- Dynamic Title ---------------- //
export function dynamicTitle() {
  document.addEventListener("DOMContentLoaded", function () {
    // Obtener el nombre de la página actual (sin la extensión)
    var currentPage = window.location.pathname.split("/").pop().split(".")[0];

    // Definir un objeto que mapee las páginas a sus títulos correspondientes
    var pageTitles = {
      index: "Inicio",
      productos: "Productos",
      nosotros: "Acerca de nosotros",
      login: "Login",
      registro: "Registrarse",
      // Agregar más páginas y títulos según sea necesario
    };

    // Obtener el título correspondiente a la página actual
    var pageTitle = pageTitles[currentPage] + " | Bifrost 3D";

    if (pageTitle.includes("undefined")) {
      pageTitle = "Inicio | Bifrost 3D";
    }

    // Actualizar el contenido del título en el head
    document.getElementById("dynamicTitle").innerText = pageTitle;
  });
}
