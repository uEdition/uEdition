(function () {
    async function setup() {
        try {
            let buttonContainer = document.querySelector('.article-header-buttons');
            if (!buttonContainer) {
                buttonContainer = document.querySelector('.navbar-header-items__end .navbar-item.navbar-persistent--container');
            }
            if (!buttonContainer) {
                return;
            }
            // Create the dropdown container
            const container = document.createElement('div');
            container.classList.add('dropdown');
            // Create the button and its icon
            const button = document.createElement('button');
            button.classList.add('btn');
            button.classList.add('dropdown-toggle');
            button.classList.add('ue-language-switcher');
            button.setAttribute('aria-label', 'Switch to another language');
            button.setAttribute('aria-expanded', 'false');
            button.setAttribute('data-bs-toggle', 'dropdown');
            button.setAttribute('type', 'button');
            const iconWrapper = document.createElement('span');
            iconWrapper.classList.add('btn__icon-container');
            const icon = document.createElement('i');
            icon.classList.add('fas');
            icon.classList.add('fa-language');
            icon.setAttribute('aria-hidden', 'true');
            // Create the dropdown list and its items
            const menu = document.createElement('ul');
            menu.classList.add('dropdown-menu');
            for (let langConfig of DOCUMENTATION_OPTIONS.UEDITION.languages) {
                const item = document.createElement('li');
                const link = document.createElement('a');
                link.classList.add('btn');
                link.classList.add('btn-sm');
                link.classList.add('dropdown-item');
                if (langConfig.code === DOCUMENTATION_OPTIONS.LANGUAGE) {
                    link.classList.add('fw-bold');
                }
                link.innerHTML = langConfig.label;
                link.setAttribute('href', document.querySelector("html").getAttribute("data-content_root") + '../' + langConfig.path + '/' + DOCUMENTATION_OPTIONS.pagename + DOCUMENTATION_OPTIONS.LINK_SUFFIX);

                item.append(link);
                menu.append(item);
            }

            iconWrapper.append(icon);
            button.append(iconWrapper);
            container.append(button);
            container.append(menu);
            buttonContainer.prepend(container);
        } catch (e) {
            console.error(e);
        }
    }

    window.addEventListener('DOMContentLoaded', setup);
})();
