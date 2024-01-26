(function () {
    function setup() {
        try {
            const dropdownMenu = document.querySelector(".article-header-buttons .dropdown-download-buttons .dropdown-menu");
            if (dropdownMenu) {
                const item = document.createElement("li");
                const link = document.createElement("a");
                link.classList.add("btn");
                link.classList.add("btn-sm");
                link.classList.add("dropdown-item");
                if (location.href.endsWith("/")) {
                    link.setAttribute("href", location.href + "index.tei");
                } else {
                    link.setAttribute("href", location.href.substring(0, location.href.lastIndexOf(".")) + ".tei");
                }
                const icon = document.createElement("span");
                icon.classList.add("btn__icon-container");
                icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="svg-inline--fa fa-code" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="code" data-fa-i2svg=""><!--!Font Awesome Free 6.5.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.--><path d="M64 0C28.7 0 0 28.7 0 64V448c0 35.3 28.7 64 64 64H320c35.3 0 64-28.7 64-64V160H256c-17.7 0-32-14.3-32-32V0H64zM256 0V128H384L256 0zM153 289l-31 31 31 31c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0L71 337c-9.4-9.4-9.4-24.6 0-33.9l48-48c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9zM265 255l48 48c9.4 9.4 9.4 24.6 0 33.9l-48 48c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l31-31-31-31c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0z"/></svg>';
                const text = document.createElement("text");
                text.classList.add("btn__text-container");
                text.innerHTML = ".tei";

                link.appendChild(icon);
                link.appendChild(text);
                item.appendChild(link);
                dropdownMenu.appendChild(item);
            }
        } catch (e) {
            console.error(e);
        }
    }

    window.addEventListener('DOMContentLoaded', setup);
})();
