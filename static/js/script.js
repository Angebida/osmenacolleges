document.addEventListener('DOMContentLoaded', function() {
    // Get the logout modal
    var logoutModal = document.getElementById('logoutModal');
    if (logoutModal) {
        // When modal is hidden, reset focus
        logoutModal.addEventListener('hidden.bs.modal', function () {
            document.activeElement.blur();
        });
    }

    // Scroll Animation Handler
    const sections = document.querySelectorAll('.scroll-section');
    let ticking = false;

    function handleScroll() {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                sections.forEach((section) => {
                    const rect = section.getBoundingClientRect();
                    const isVisible = (
                        rect.top < window.innerHeight * 0.75 &&
                        rect.bottom >= 0
                    );
                    
                    if (isVisible) {
                        section.classList.add('active');
                        const scrollProgress = Math.max(0.4, 1 - (Math.abs(rect.top) / window.innerHeight));
                        if (section.querySelector('.content')) {
                            section.querySelector('.content').style.opacity = scrollProgress;
                        }
                    }
                });
                ticking = false;
            });
            ticking = true;
        }
    }

    // Initial check and scroll handler
    handleScroll();
    window.addEventListener('scroll', handleScroll, { passive: true });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
