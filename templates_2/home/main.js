const lightDark = document.querySelector(".lightDark");
const lightdarskBg = document.querySelector(".light-darskBg");
const logo = document.getElementById("logo");
const namee = document.querySelector(".namee");
const aboutMe = document.querySelector(".aboutMe");
const li = document.querySelectorAll("li");
const icons = document.querySelectorAll("i");
const iconId = document.getElementById("iconid");
const atags = iconId.querySelectorAll("a");

lightDark.addEventListener("click", () => {
  lightdarskBg.classList.toggle("dark");
  lightDark.style.background = "#2d2d2d";
  document.body.classList.toggle("bodyColor");
  logo.classList.toggle("colorWhite");
  namee.classList.toggle("colorWhite");
  aboutMe.classList.toggle("colorWhite");
  li.forEach((item) => {
    console.log(item);
    item.classList.toggle("colorWhite");
  });

  atags.forEach((item) => item.classList.toggle("iconvo"));
});


