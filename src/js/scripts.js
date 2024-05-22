/*  Card */
document.addEventListener("DOMContentLoaded", function() {
    const productsContainer = document.getElementById("products-padel-container");

    padel.slice(0, 3).forEach(function(product) { // Limitar a los primeros 3 productos
        const card = createCard(product);
        productsContainer.appendChild(card);
    });
});

function createCard(product) {
    const card = document.createElement("div");
    card.classList.add("card");

    const image = document.createElement("img");
    image.src = product.image;
    image.alt = product.producto;
    card.appendChild(image);

    const details = document.createElement("div");
    details.classList.add("details");

    const name = document.createElement("p");
    name.classList.add("product-name");
    name.textContent = `Producto: ${product.producto}`;
    details.appendChild(name);

    const price = document.createElement("p");
    price.classList.add("price");
    price.textContent = `Precio: ${product.precio}`;
    details.appendChild(price);

    const description = document.createElement("p");
    description.classList.add("description");
    description.textContent = `Descripción: ${product.descripcion}`;
    details.appendChild(description);

    card.appendChild(details);

    return card;
}

document.addEventListener("DOMContentLoaded", function() {
    const productsContainer = document.getElementById("products-qr-container");

    codigosQr.slice(0, 3).forEach(function(product) { // Limitar a los primeros 3 productos
        const card = createCard(product);
        productsContainer.appendChild(card);
    });
});

function createCard(product) {
    const card = document.createElement("div");
    card.classList.add("card");

    const image = document.createElement("img");
    image.src = product.image;
    image.alt = product.producto;
    card.appendChild(image);

    const details = document.createElement("div");
    details.classList.add("details");

    const name = document.createElement("p");
    name.classList.add("product-name");
    name.textContent = `Producto: ${product.producto}`;
    details.appendChild(name);

    const price = document.createElement("p");
    price.classList.add("price");
    price.textContent = `Precio: ${product.precio}`;
    details.appendChild(price);

    const description = document.createElement("p");
    description.classList.add("description");
    description.textContent = `Descripción: ${product.descripcion}`;
    details.appendChild(description);

    card.appendChild(details);

    return card;
}

/* short youtube */
function onYouTubeIframeAPIReady() {
    var players = document.querySelectorAll('.youtube-shortcode');
    for (var i = 0; i < players.length; i++) {
        var player = new YT.Player(players[i], {
            height: '315',
            width: '560',
            videoId: players[i].dataset.embed,
        });
    }
}

/* card unica con video */

document.addEventListener("DOMContentLoaded", function () {
    const productsContainer = document.getElementById("section-video");

    // Itera sobre los productos de la categoría "codigosQr" y muestra el primer objeto con video
    let videoFound = false;
    codigosQr.forEach(function (product) {
        if (product.video && !videoFound) {
            const card = createVideoCard(product);
            productsContainer.appendChild(card);
            videoFound = true; // Marca que se ha encontrado un video
        }
    });
});


function createVideoCard(product) {
    const card = document.createElement("div");
    card.classList.add("card-video");

    const details = document.createElement("div");
    details.classList.add("details");

    const name = document.createElement("p");
    name.classList.add("product-name");
    name.textContent = `Producto: ${product.producto}`;
    details.appendChild(name);

    const price = document.createElement("p");
    price.classList.add("price");
    price.textContent = `Precio: ${product.precio}`;
    details.appendChild(price);

    const description = document.createElement("p");
    description.classList.add("description");
    description.textContent = `Descripción: ${product.descripcion}`;
    details.appendChild(description);

    card.appendChild(details);

    if (product.video) {
        const videoContainer = document.createElement("div");
        videoContainer.classList.add("video-container");

        const video = document.createElement("iframe");
        video.src = product.video;
        video.title = product.producto;
        video.allowFullscreen = true;
        video.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        video.referrerPolicy="strict-origin-when-cross-origin" 
        // Establecer ancho y altura del contenedor del video
        videoContainer.style.width = "100%";
        videoContainer.style.height = "500px"; // Puedes ajustar la altura según tus necesidades

        // Agregar el iframe al contenedor
        videoContainer.appendChild(video);

        card.appendChild(videoContainer);
    } else {
        const noVideoMessage = document.createElement("p");
        noVideoMessage.textContent = "No hay video disponible";
        card.appendChild(noVideoMessage);
    }

    return card;
}

// Arreglos de productos
let productos = [padel, reposteria, codigosQr, llaveros, varios];

// Función para mostrar productos
function mostrarProductos() {
    const container = document.getElementById("todos-productos-container");

    // Limpiar el contenedor antes de agregar nuevos productos
    container.innerHTML = "";

    // Iterar sobre cada arreglo de productos
    productos.forEach((categoria) => {
        // Iterar sobre cada producto de la categoría
        categoria.forEach((producto) => {
            // Crear una tarjeta para el producto
            const card = createCard(producto);
            // Agregar la tarjeta al contenedor
            container.appendChild(card);
        });
    });
}

// Llamar a la función para mostrar productos
mostrarProductos();



