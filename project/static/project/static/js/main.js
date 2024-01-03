let navbutton=document.querySelector('#btn-nav');
let nav=document.querySelector('.head');


navbutton.addEventListener('click',()=>{
  if (nav.style.display === "none") {
    nav.style.display = "block";
  } else {
    nav.style.display = "none";
  }
  
})