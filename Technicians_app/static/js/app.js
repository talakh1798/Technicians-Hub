document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default AJAX behavior
        window.location.href = this.href; // Force a full page reload
      });
    });
  });

$(document).ready(function() {
    // List of video URLs
    var videoURLs = [
        "https://cdn-static.findly.com/wp-content/uploads/sites/3285/2024/04/23090604/path-to-pro_intro-video.mp4",
        "https://cdn-static.findly.com/wp-content/uploads/sites/3285/2024/04/23090628/path-to-pro_intro-video-2.mp4",
        "https://cdn-static.findly.com/wp-content/uploads/sites/3285/2024/04/23090702/path-to-pro_intro-video-3.mp4"
    ];

    // Choose a random video URL
    var randomVideoURL = videoURLs[Math.floor(Math.random() * videoURLs.length)];

    // Generate video element and append it to .fullwidth-video div
    var videoElement = '<video preload="auto" autoplay playsinline loop muted><source src="' + randomVideoURL + '" type="video/mp4"></video>';
    $('.video-background').html(videoElement);
});

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    function showError(input, message) {
        const parent = input.parentElement;
        let error = parent.querySelector('.error-message');
        if (!error) {
            error = document.createElement('p');
            error.className = 'error-message';
            error.style.color = 'red';
            parent.appendChild(error);
        }
        error.textContent = message;
    }

    function clearError(input) {
        const parent = input.parentElement;
        const error = parent.querySelector('.error-message');
        if (error) {
            parent.removeChild(error);
        }
    }

    form.addEventListener('input', function (event) {
        const input = event.target;

        clearError(input);

        switch (input.id) {
            case 'first_name':
            case 'last_name':
                if (input.value.length < 2) {
                    showError(input, `${input.previousElementSibling.textContent} must be at least 2 characters`);
                }
                break;

            case 'email':
                const emailRegex = /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/;
                if (!emailRegex.test(input.value)) {
                    showError(input, 'Invalid email address!');
                }
                break;

            case 'phone_number':
                if (input.value.length < 10) {
                    showError(input, 'Phone number should be at least 10 digits long.');
                }
                break;

            case 'date_of_birth':
                const today = new Date();
                const dob = new Date(input.value);
                const age = today.getFullYear() - dob.getFullYear();
                if (isNaN(dob) || age < 18) {
                    showError(input, 'Age must be at least 18 years old');
                }
                break;

            case 'password':
                if (input.value.length < 6) {
                    showError(input, 'Password must be at least 6 characters');
                }
                break;
        }
    });
});


$(document).ready(function () {
    console.log("Script is running"); // Add this to confirm the script is working
    var passwordField = $('#password');
    var confirmPasswordField = $('#confirm_password');
    var message = $('#passwordMatchMessage');

    // Check if passwords match while typing
    function checkPasswords() {
        console.log("Checking passwords"); // Add this to confirm the function is running
        var password = passwordField.val();
        var confirmPassword = confirmPasswordField.val();

        if (password === confirmPassword) {
            message.text("Passwords match");
            message.removeClass('text-danger');
            message.addClass('text-success');
        } else {
            message.text("Passwords do not match!");
            message.removeClass('text-success');
            message.addClass('text-danger');
        }
    }

    passwordField.on('input', checkPasswords);
    confirmPasswordField.on('input', checkPasswords);
});



