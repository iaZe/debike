const rotatingImages = document.querySelectorAll('.rotating-image');

window.addEventListener('scroll', () => {
  rotatingImages.forEach(image => {
    const rotationTrigger = image.offsetTop - window.innerHeight * 0.7;
    const rotationAngle = (window.scrollY - rotationTrigger) * 0.1;

    if (rotationAngle >= 0) {
      image.style.transform = `rotate(${rotationAngle}deg)`;
    }
  });
});