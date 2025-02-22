// Close the navbar when a link is clicked
document.addEventListener('DOMContentLoaded', function () {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click(); // Simulate a click on the toggler to close the navbar
            }
        });
    });
});

function toggleDescription(descriptionId, buttonId) {
    const description = document.getElementById(descriptionId);
    const button = document.getElementById(buttonId);

    // Get the computed value of -webkit-line-clamp or line-clamp
    const lineClamp = window.getComputedStyle(description).webkitLineClamp || window.getComputedStyle(description).lineClamp;

    if (lineClamp === "2" || lineClamp === "3") { // Adjust based on your initial line-clamp value
        description.style.webkitLineClamp = "unset";
        description.style.lineClamp = "unset";
        button.textContent = "Read Less";
    } else {
        description.style.webkitLineClamp = "2"; // Adjust based on your initial line-clamp value
        description.style.lineClamp = "2"; // Adjust based on your initial line-clamp value
        button.textContent = "Read More";
    }
}