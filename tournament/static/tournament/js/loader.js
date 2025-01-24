document.addEventListener("DOMContentLoaded", function() {
  const preloader = document.getElementById('preloader');
  const body = document.body;
  const content = document.querySelector('.content');
  
  // Increase loading time by adding a delay
  setTimeout(() => {
    preloader.style.display = 'none'; // Hide the preloader
    body.style.display = 'block'; // Show the entire body content (page)
    
    // After hiding the preloader, show the content with animation
    content.classList.add('show-content'); // Trigger fade-in or slide-in animation
  }, 400); // Adjust this value for desired delay in milliseconds
});
