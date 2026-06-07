document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contactForm');
    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            alert('Thanks! Your message was sent.');
            form.reset();
        });
    }

    const page = window.location.pathname.split('/').pop();
    document.querySelectorAll('.circuit-strip a').forEach(function (link) {
        if (link.getAttribute('href') === page) {
            link.classList.add('active');
        }
    });
});
