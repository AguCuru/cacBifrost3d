// funciona a medias, carga data.js pero no muestra las imagenes

const scripts = [
  "./src/js/index.js",
  "./src/js/data.js",
  "./src/js/scripts.js",
  "./src/js/index.js",
  "./src/js/fragments/headIndeax.js",
  "./src/js/fragments/headerIndex.js",
  "./src/js/fragments/footer.js",
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
];

function loadScripts(scriptUrls) {
  scriptUrls.forEach((src) => {
    // Verifica si el script ya está en el documento para evitar duplicados
    if (!document.querySelector(`script[src="${src}"]`)) {
      console.log(`Intentando cargar script: ${src}`); // Mensaje de depuración
      const script = document.createElement("script");
      script.src = src;
      if (src.includes("bootstrap")) {
        script.integrity =
          "sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz";
        script.crossOrigin = "anonymous";
      }
      script.onload = () => console.log(`Script cargado: ${src}`); // Mensaje de depuración
      script.onerror = () => console.error(`Error al cargar el script: ${src}`); // Mensaje de depuración
      document.body.appendChild(script);
    } else {
      console.log(`Script ya cargado: ${src}`); // Mensaje de depuración
    }
  });
}

// Llamar a la función para cargar los scripts
loadScripts(scripts);
