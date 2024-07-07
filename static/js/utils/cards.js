import data from "../data.js";

document.addEventListener("DOMContentLoaded", function () {
  let cardsContainer = document.getElementById("cards-container");

  // Iterar sobre el arreglo de productos y generar las cards dinámicamente
  data.forEach((producto) => {
    // Crear elementos HTML para la card
    let card = document.createElement("div");
    card.classList.add("card");

    let image = document.createElement("img");
    let path = "../../" + producto.image;
    image.src = path;
    image.alt = producto.producto;

    let title = document.createElement("h2");
    title.textContent = producto.producto;

    let description = document.createElement("p");
    description.textContent = producto.descripcion;

    let price = document.createElement("p");
    price.textContent = `Precio: ${producto.precio} pesos`;

    let stock = document.createElement("p");
    stock.textContent = `Stock disponible: ${producto.Stock}`;

    // Agregar elementos a la card
    card.appendChild(image);
    card.appendChild(title);
    card.appendChild(description);
    card.appendChild(price);
    card.appendChild(stock);

    // Agregar la card al contenedor de cards
    cardsContainer.appendChild(card);
  });
});
