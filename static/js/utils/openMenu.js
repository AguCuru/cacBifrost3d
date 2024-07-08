function openMenu() {
  document.getElementById("menu-icon").addEventListener("click", function () {
    document.querySelector(".navlist").classList.toggle("open");
  });
}

export default { openMenu };
