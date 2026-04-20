// Reveal elements on scroll
function reveal() {
    const reveals = document.querySelectorAll(".reveal");
    const windowHeight = window.innerHeight;
    const elementVisible = 150;

    reveals.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        if (elementTop < windowHeight - elementVisible) {
            element.classList.add("active");
        }
    });
}

// Event listener for scrolling
window.addEventListener("scroll", reveal);

// Initial call to reveal elements already in viewport
document.addEventListener("DOMContentLoaded", () => {
    reveal();
});
