$(function(){
    console.log('Item Details')
    /*Highhlight the current page in NavBar*/
    $('.nav-link').each(function(index){

            if (index == 1) {
                $(this).addClass('active'); $(this).parents('li').addClass('active');
            }
    });

    /*Adjust side of SideBar*/
    body = $('body').height()/1.4
    $('.bodyNav').css('height', body)
    /*End Adjust side of SideBar*/


    Get Array from the text area tagify
    $('.submit').on('click', function(e){
        e.preventDefault()
        values = []
        $('.tagify__tag-text').each(function(index){
            console.log($(this).text() + " value ",index)
            values.push($(this).text())
        })
        console.log(values, "All Values")
        console.log($('.itemTags').val(), 'Logged')
    });



});
