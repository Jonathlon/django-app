console.log("Welcome to the recipe app");

const counterContainer = document.querySelector(".website-counter");
const resetButton = document.querySelector("#reset");
let visitCount = localStorage.getItem("page_view");

if (visitCount) {
  visitCount = Number(visitCount) + 1;
  localStorage.setItem("page_view", visitCount);
} else {
  visitCount = 1;
  localStorage.setItem("page_view", 1);
}
counterContainer.innerHTML = visitCount;

resetButton.addEventListener("click", () => {
  visitCount = 1;
  localStorage.setItem("page_view", 1);
  counterContainer.innerHTML = visitCount;
});
