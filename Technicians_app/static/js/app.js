document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default AJAX behavior
        window.location.href = this.href; // Force a full page reload
      });
    });
  });