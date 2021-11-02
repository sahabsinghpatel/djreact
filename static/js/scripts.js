window.addEventListener('DOMContentLoaded', event => {
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }
    };
    navbarShrink();
    document.addEventListener('scroll', navbarShrink);
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
});

function enableloginbtn(){
    var loginbtn = document.getElementById('submitlogin')
    if (document.getElementById('lusername').value != "" && document.getElementById('lpassword').value != ""){
        loginbtn.disabled = false;
    }
    else{
        loginbtn.disabled = true;
    }
};

function enablesignupbtn(){
    var signupbtn = document.getElementById('signupbtn')
    if (document.getElementById('username').value != "" && document.getElementById('email').value != "" && document.getElementById('password').value != ""){
        signupbtn.disabled = false;
    }
    else{
        signupbtn.disabled = true;
    }
};

function enablevarifybtn(){
    var vaifybtn = document.getElementById('vaifybtn')
    if (document.getElementById('otp').value.length === 6){
        vaifybtn.disabled = false;
    }
    else{
        vaifybtn.disabled = true;
    }
};

function searchbtn(){
    var searchbutton = document.getElementById('searchbutton')
    if (document.getElementById('searchinput').value != ""){
        searchbutton.disabled = false;
    }
    else{
        searchbutton.disabled = true;
    }
};

function enableresetpasspbtn(){
    var resetpassbtn=document.getElementById('resetpassbtn')
    if (document.getElementById('email').value.length > 4){
        resetpassbtn.disabled=false;
    }
    else{
        resetpassbtn.disabled=true;
    }
};
