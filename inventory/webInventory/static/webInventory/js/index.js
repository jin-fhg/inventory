$(function (){
    console.log("Index JQuery");

    /*Adjust side of SideBar*/
    body = $('body').height()
    $('.bodyNav').css('height', body)
    /*End Adjust side of SideBar*/

    $('.chartHeader').on('click', function (){
        $('.chartContent').fadeToggle();
    });

    /*Highhlight the current page in NavBar*/
    $('.nav-link').each(function(){
            if ($(this).prop('href') == window.location.href) {
                $(this).addClass('active'); $(this).parents('li').addClass('active');
            }
    });



});