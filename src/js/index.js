// index.js
document.addEventListener("DOMContentLoaded", function() {
    // Obtener el nombre de la página actual (sin la extensión)
    var currentPage = window.location.pathname.split('/').pop().split('.')[0];
    
    // Definir un objeto que mapee las páginas a sus títulos correspondientes
    var pageTitles = {
        'index': 'Página de inicio',
        'productos': 'Nuestros productos',
        'nosotros': 'Acerca de nosotros',
        'login': 'Iniciar sesión',
        'registro': 'Registrarse'
        // Agrega más páginas y títulos según sea necesario
    };
    
    // Obtener el título correspondiente a la página actual
    var pageTitle = pageTitles[currentPage] || 'Bifrost 3D';
    
    // Actualizar el contenido del título en el head
    document.getElementById('dynamicTitle').innerText = pageTitle;
});
