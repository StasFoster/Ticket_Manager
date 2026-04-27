const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');

loginBtn?.addEventListener('click', () => {
    window.location.href = "/login"; // твой url
});

registerBtn?.addEventListener('click', () => {
    window.location.href = "/auth"; // твой url
});