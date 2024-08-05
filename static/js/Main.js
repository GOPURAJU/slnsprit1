document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.Psection2 .nav-item');
    const sections = document.querySelectorAll('section');
    const offset = 50; 

    window.addEventListener('scroll', () => {
        let current = '';

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (window.scrollY >= sectionTop - offset) {
                current = section.getAttribute('id');
            }
        });

        navItems.forEach(navItem => {
            navItem.classList.remove('active');
            if (navItem.getAttribute('data-section') === current) {
                navItem.classList.add('active');
            }
        });
   

    


    navItems.forEach(navItem => {
        navItem.addEventListener('click', (event) => {
            event.preventDefault();
            const sectionId = navItem.getAttribute('data-section');
            document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
        });
    });


});


window.onscroll=()=>{
    if(window.scrollY >= 300){
        // console.log(window.scrollY)
        document.querySelector('.scroll-to-top').style.display="block";
    }
    else{
        document.querySelector('.scroll-to-top').style.display="none";

    }
   
    const nav2= document.querySelector('.Psection2').offsetTop;
    const offset=nav2-100;

    if(window.scrollY>=offset){

        document.querySelector('.navbar-section').style.display="none";

        
    }
    else{
        document.querySelector('.navbar-section').style.display="block";

    }
}
document.querySelector('.scroll-to-top').addEventListener('click',function(){

    window.scrollTo({top:0,behavior:"smooth"})
})


// const navLiItem = document.querySelectorAll('.navbar-section .navbar-nav .nav-item');

// navLiItem.forEach(item => {
//     item.addEventListener('click', function () {
      
//         navLiItem.forEach(nav => nav.classList.remove('active'));
       
//         this.classList.add('active');
//     });
// });




});