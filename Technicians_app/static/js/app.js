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
    $('.fullwidth-video').html(videoElement);
});