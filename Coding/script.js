// Toggle Navbar on Hamburger Click
document.getElementById('menu-toggle').addEventListener('click', function() {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active');
});

// Toggle Color Mode
document.getElementById('color-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
});
