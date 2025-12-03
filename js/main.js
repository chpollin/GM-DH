// Nach-oben-Button Funktionalität
const backToTopButton = document.getElementById('back-to-top');

// Button anzeigen/verbergen basierend auf Scroll-Position
window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight) {
        backToTopButton.classList.add('show');
    } else {
        backToTopButton.classList.remove('show');
    }
});

// Smooth scroll nach oben
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Smooth scrolling für Jahr-Navigation
document.querySelectorAll('.year-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const offset = 80; // Offset für sticky navigation
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});
