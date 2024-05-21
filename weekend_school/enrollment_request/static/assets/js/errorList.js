document.addEventListener("DOMContentLoaded", () => {
  const errorlists = document.querySelectorAll("ul.errorlist");
  errorlists.forEach((errorlist) => {
    const liElements = errorlist.querySelectorAll("li");
    liElements.forEach((li) => {
      const iconElement = document.createElement("i");
      iconElement.classList.add("bi", "bi-exclamation-triangle-fill");
      li.insertBefore(iconElement, li.firstChild);
    });
  });
});
