    document.addEventListener('DOMContentLoaded', function() {
        const removeButtons = document.querySelectorAll('.cart-container .remove-btn');

        removeButtons.forEach(function(button) {
            button.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent the form from submitting
                const confirmed = confirm('Are you sure you want to remove this item from your cart?');
                if (confirmed) {
                    this.closest('form').submit(); // Submit the form if confirmed
                }
            });
        });
    });