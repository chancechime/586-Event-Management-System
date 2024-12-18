function showSpinner() {
    document.getElementById('spinner').classList.remove('d-none');
}

function hideSpinner() {
    document.getElementById('spinner').classList.add('d-none');
}

function decrement() {
    var value = parseInt(document.getElementById('quantity').value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 0) {
        value--;
    }
    document.getElementById('quantity').value = value;
}

function increment() {
    var value = parseInt(document.getElementById('quantity').value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 8) {
        value++;
    }
    document.getElementById('quantity').value = value;
}

// Example usage: Show spinner for 1.0 seconds on page load
document.addEventListener('DOMContentLoaded', () => {
    showSpinner();
    setTimeout(hideSpinner, 1000);
});
