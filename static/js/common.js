
window.addEventListener('DOMContentLoaded',()=>{


    const pathname=window.location.pathname;
   const res=pathname.split('/').pop();
   const listitems=document.querySelectorAll('.nav-item.dropdown .dropdown-menu .dropdown-item')


if(res==="{% url 'about' %}"){
    document.querySelector('.Aboutus').classList.add('myactive');
}
else if(res==="{% url 'creditpage' %}"){
    document.querySelector('.credit-cards').classList.add('myactive');

}
else if(res==="{% url 'allinsurance' %}" || res==="{% url 'lifeinsurance' %}" || res==="{% url 'generalinsurance' %}" || res==="{% url 'helathinsurance' %}"){

    document.querySelector('.insurance').classList.add('myactive');
    listitems.forEach(items=>{
        console.log(items.getAttribute('href'));
        if(items.getAttribute('href')===res){
            items.classList.add('custom-background');

        }
    })

   



}
else if(res==="{% url 'contact' %}"){
    document.querySelector('.contactus').classList.add('myactive');
}
else if(res==="{% url 'dsa' %}" || res==="{% url 'franchise' %}"){
    document.querySelector('.partner').classList.add('myactive');
    listitems.forEach(items=>{
        console.log(items.getAttribute('href'));
        if(items.getAttribute('href')===res){
            items.classList.add('custom-background');

        }
    })
}

else if(res==="{% url 'personalloans' %}" || res==="{% url 'educationalloan' %}" || res==="{% url 'homeloan' %}" || res==="{% url 'bussinessloan' %}" || res==="{% url 'lap' %}" || res==="{% url 'carloan' %}" || res==="{% url 'usedcar' %}.html" || res==="{% url 'newcar' %}"){

    document.querySelector('.loans').classList.add('myactive');
    console.log(res);

    
    console.log(listitems);

    listitems.forEach(items=>{
        console.log(items.getAttribute('href'));
        if(items.getAttribute('href')===res){
            items.classList.add('custom-background');

        }
    })

}

});