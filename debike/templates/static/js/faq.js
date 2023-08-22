document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq-item");
  
    faqItems.forEach(function(item) {
      item.addEventListener("click", function() {
        const itemId = item.getAttribute("id");
        const content = document.querySelector(`.faq-content[id="${itemId}"]`);
  
        if (content) {
          content.classList.toggle("active");
        }
      });
    });
  });
  