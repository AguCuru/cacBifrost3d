/*  Card */
document.addEventListener("DOMContentLoaded", function() {
    const productsContainer = document.getElementById("products-container");

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
    const productsContainer = document.getElementById("products-container");

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
