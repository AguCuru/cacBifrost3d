let footer =
`
                <div class="col-md-4 d-flex align-items-center">
                <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                    <svg class="bi" width="30" height="24">
                        <use xlink:href="./index.html" />
                    </svg>
                </a>
                <span class="text-muted">&copy; 2024 Bifrost 3D</span>
            </div>

            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                <li class="iconos">
                    <a class="text-muted" href="https://x.com"><i class="fa-brands fa-x-twitter"></i></a>
                </li>
                <li class="iconos">
                    <a class="text-muted" href="https://www.instagram.com"><i class="fa-brands fa-instagram"></i></a>
                </li>
            </ul>
`
document.getElementById("id_footer").innerHTML = footer;
