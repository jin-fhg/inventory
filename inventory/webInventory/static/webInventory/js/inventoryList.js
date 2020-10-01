$(function (){
    console.log("Inventory")
    /*Highhlight the current page in NavBar*/
    $('.nav-link').each(function(){
            if ($(this).prop('href') == window.location.href) {
                $(this).addClass('active'); $(this).parents('li').addClass('active');
            }
    });

    /*Adjust side of SideBar*/
    body = $('body').height()/1.4
    $('.bodyNav').css('height', body)
    /*End Adjust side of SideBar*/

    $('.itemFolder').hover(function (){
        $(this).css('background-color', 'gray')
        $(this).find('a').css('color', 'white')

    });

    $('.showHide').on('click', function (){
        $('.addForm').fadeToggle('slow');
    });

    $('.btnEditName').on('click', function (){
        var txt = $(this).closest('.card-body').find('.folderName').html();
        $(this).closest('.card-body').find('.txtEditName').val(txt)
        $(this).closest('.card-body').find('.card-text,.txtEditName').toggle();
        $(this).closest('.card-body').find('.txtEditName').focus();
    });



    $('.txtEditName').on('blur focusOut', function (){
       if(!$.trim(this.value).length){
           $(this).addClass('warning');
           alert("The Field Cannot be Empty");
       }else{
           $(this).removeClass('warning');
           $(this).closest('.card-body').find('.folderName').html($(this).val());
           $(this).closest('.card-body').find('.card-text,.txtEditName').toggle();
           var db_id = $(this).attr('db_id')
           var txtVal = $(this).val()
           var csrfmiddlewaretoken = $(this).closest('.card-body').find('input[name=csrfmiddlewaretoken]').val();

           $.ajax({
               type: 'POST',
               url: 'update/',
               data: {
                   update: 'name',
                   id: db_id,
                   value: txtVal,
                   csrfmiddlewaretoken: csrfmiddlewaretoken,
               }
           })
       }

    });


    $('.itemFolder').mouseleave(function (){
        $(this).css('background-color', 'white')
        $(this).find('a').css('color', 'black')
    })


    $('.btnEditDesc').on('click', function (){
        var txt = $(this).closest('.card-body').find('.descContent').text()
        $(this).closest('.card-body').find('.txtEditDesc').val(txt);
        $(this).closest('.card-body').find('.descContent, .txtEditDesc').toggle();
        $(this).closest('.card-body').find('.txtEditDesc').focus();
    })

    $('.txtEditDesc').on('blur focusOut', function (){
       $(this).closest('.card-body').find('.descContent,.txtEditDesc').toggle();
       $(this).closest('.card-body').find('.descContent').text($(this).val());
       var db_id = $(this).attr('db_id')
       var txtVal = $(this).val()
       var csrfmiddlewaretoken = $(this).closest('.card-body').find('input[name=csrfmiddlewaretoken]').val();
       $.ajax({
               type: 'POST',
               url: 'update/',
               data: {
                   update: 'description',
                   id: db_id,
                   value: txtVal,
                   csrfmiddlewaretoken: csrfmiddlewaretoken,
               }
           })
    });

    $('.deleteOption').on('click', function (){
        var db_id = $(this).attr('db_id')
        $('.deleteOptionId').val(db_id)
    })

    /*For Alert*/
    $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){
       $(".alert-success").slideUp(500);
    });




});