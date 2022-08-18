// arrow up btn

const home = document.querySelector(".top-left");
const home_height = home.getBoundingClientRect().height;
const arrow_up = document.querySelector(".arrowbtn");
document.addEventListener("scroll", () => {
  if (window.scrollY > home_height / 2) {
    arrow_up.classList.add("visible");
  } else {
    arrow_up.classList.remove("visible");
  }
});

arrow_up.addEventListener("click", () => {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
});
