document.addEventListener("DOMContentLoaded", function() {
    // Evitar el envío al presionar Enter
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
            }
        });
    });

    // Desvanecer y remover la alerta
    setTimeout(function() {
        const alertElement = document.querySelector('.alert');
        if (alertElement) {
            alertElement.style.transition = "opacity 0.5s ease";
            alertElement.style.opacity = "0";
            setTimeout(() => alertElement.remove(), 500); // Remover del DOM
        }
    }, 6000); // 6000 ms = 6 segundos
});
