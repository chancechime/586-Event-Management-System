function showSpinner() {
    document.getElementById('spinner').classList.remove('d-none');
}

function hideSpinner() {
    document.getElementById('spinner').classList.add('d-none');
}

// Example usage: Show spinner for 3 seconds on page load
document.addEventListener('DOMContentLoaded', () => {
    showSpinner();
    setTimeout(hideSpinner, 3000);
});
