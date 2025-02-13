// Form Validation
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Initialize Google Maps
    initMap();
});

// Google Maps Integration
function initMap() {
    const companyLocation = { lat: YOUR_LATITUDE, lng: YOUR_LONGITUDE };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: companyLocation,
    });
    
    const marker = new google.maps.Marker({
        position: companyLocation,
        map: map,
        title: 'Our Location'
    });
}

// Portfolio Gallery
document.querySelectorAll('.portfolio-item').forEach(item => {
    item.addEventListener('click', function() {
        const imageSrc = this.querySelector('img').src;
        const title = this.querySelector('.portfolio-title').textContent;
        
        const modal = new bootstrap.Modal(document.getElementById('portfolioModal'));
        document.getElementById('modalImage').src = imageSrc;
        document.getElementById('modalTitle').textContent = title;
        modal.show();
    });
});
