let burger_buttom = document.querySelector(".header_burger_menu");
let side_menu = document.querySelector(".side_menu");
let side_menu_X = document.querySelector(".side_menu_cross")

burger_buttom.onclick = () => (
    side_menu.classList.add('active_side_menu')
);

side_menu_X.onclick = () => (
    side_menu.classList.remove('active_side_menu')
)
