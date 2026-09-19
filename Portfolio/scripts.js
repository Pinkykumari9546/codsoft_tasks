

const navList =  document.getElementById("nav-link");
const menu = document.getElementById("menu-icon");
const mark = document.getElementById("mark");

menu.addEventListener("click", () =>{
    navList.style.right = "0";
    
})

mark.addEventListener("click", () => {
    navList.style.right = "-45%"
    
})

