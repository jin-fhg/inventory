$(function(){
    console.log('Item Details')
    /*Highhlight the current page in NavBar*/
    $('.nav-link').each(function(index){

            if (index == 1) {
                $(this).addClass('active'); $(this).parents('li').addClass('active');
            }
    });


    $('.fieldContainer').hover(
        function(){
            $(this).closest('div').find('i').show()
        },

        function(){
            $(this).closest('div').find('i').hide()
        },

    )

    /*Adjust side of SideBar*/
    body = $('body').height()/1.4
    $('.bodyNav').css('height', body)
    /*End Adjust side of SideBar*/

    $('[data-toggle="tooltip"]').tooltip();

/*    Get Array from the text area tagify
    $('.submit').on('click', function(e){
        e.preventDefault()
        values = []
        $('.tagify__tag-text').each(function(index){
            console.log($(this).text() + " value ",index)
            values.push($(this).text())
        })
        console.log(values, "All Values")
        console.log($('.itemTags').val(), 'Logged')
    });*/


    $('.btnEdit').on('click', function(){
        $(this).closest('div').find('span, input').toggle();
        $(this).closest('div').find('input').focus();
    })

    $('input').on('blur', function(){
        $(this).closest('div').find('span, input').toggle();
        var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        var updateWhat = $(this).attr('name')
        var value = $(this).val()
        $(this).closest('div').find('.field').text(value);
        console.log("This " + csrfmiddlewaretoken +  ' ' + updateWhat)
        $.ajax({
            type: 'POST',
            url: 'edit/',
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken,
                updateWhat: updateWhat,
                value: value,
            }

        })
    })




});
