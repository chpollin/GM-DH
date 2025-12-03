// Nach-oben-Button Funktionalität
const backToTopButton = document.getElementById('back-to-top');

// Button anzeigen/verbergen basierend auf Scroll-Position
window.addEventListener('scroll', () => {
    if (window.scrollY > window.innerHeight) {
        backToTopButton.classList.add('show');
    } else {
        backToTopButton.classList.remove('show');
    }

    // Scroll Spy für Navigation
    updateActiveNavLink();
});

// Smooth scrolling für Jahr-Navigation
document.querySelectorAll('.year-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const offset = 100; // Offset für sticky navigation
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Smooth scroll nach oben
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Scroll Spy: Aktiven Link basierend auf Scroll-Position markieren
function updateActiveNavLink() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.year-link');

    if (sections.length === 0) {
        console.log('No sections found!');
        return;
    }

    let currentSection = '';
    const scrollPosition = window.scrollY + 120; // Offset für sticky navigation

    // Von unten nach oben durchgehen, um die aktuellste Section zu finden
    const sectionsArray = Array.from(sections);
    for (let i = sectionsArray.length - 1; i >= 0; i--) {
        const section = sectionsArray[i];
        const sectionTop = section.offsetTop;

        if (scrollPosition >= sectionTop - 50) {
            currentSection = section.getAttribute('id');
            break;
        }
    }

    // Wenn keine Section gefunden wurde, erste Section aktivieren
    if (!currentSection && sections.length > 0) {
        currentSection = sections[0].getAttribute('id');
    }

    navLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href');
        if (href === `#${currentSection}`) {
            link.classList.add('active');
            console.log('Active section:', currentSection);
        }
    });
}

// Initiale Aktivierung beim Laden
document.addEventListener('DOMContentLoaded', () => {
    updateActiveNavLink();
    const sections = document.querySelectorAll('section[id]');
    console.log('Scroll Spy initialized. Found sections:', sections.length);
    sections.forEach(s => console.log('Section ID:', s.id));
});
