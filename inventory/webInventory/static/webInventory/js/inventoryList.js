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

    $('[data-toggle="tooltip"]').tooltip();

    var folderList = $('.folderList').DataTable({
       bFilter: true,
       bInfo: false,
       bLengthChange: true,
       bSort: true,
       pageLength: 10,
       language: { searchPlaceholder: "Names.."},
       });




    $('.showHide').on('click', function (){
        $('.addForm').fadeToggle('slow');
    });

    $('.folderList').on('click','.btnEditName',function (){
        var txt = $(this).closest('p').find('.folderName').html();
        $(this).closest('p').find('.txtEditName').val(txt)
        $(this).closest('p').find('.folderName,.txtEditName').toggle();
        $(this).closest('p').find('.txtEditName').focus();
    });



    $('.folderList').on('blur focusOut','.txtEditName',function (){
       if(!$.trim(this.value).length){
           alert("The Field Cannot be Empty");
           $(this).addClass('warning');
       }else{
           $(this).removeClass('warning');
           $(this).closest('p').find('.folderName').html($(this).val());
           $(this).closest('p').find('.folderName, .txtEditName').toggle();
           var db_id = $(this).attr('db_id')
           var txtVal = $(this).val()
           var csrfmiddlewaretoken = $(this).closest('p').find('input[name=csrfmiddlewaretoken]').val();

           $.ajax({
               type: 'POST',
               url: 'update/',
               data: {
                   id: db_id,
                   value: txtVal,
                   csrfmiddlewaretoken: csrfmiddlewaretoken,
               }
           })
       }

    });


    /*$('.itemFolder').mouseleave(function (){
        $(this).css('background-color', 'white')
        $(this).find('a').css('color', 'black')
    })*/

    $('.folderList').on('click', '.deleteOption' ,function (){
        var db_id = $(this).attr('db_id')
        $('.deleteOptionId').val(db_id)
    })

    /*For Alert*/
    $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){
       $(".alert-success").slideUp(500);
    });


    $('input[type=search]').add('select').on('focus', function (){

         $(this).css('border', '3px solid powderblue')
    });

    $('select').add('input[type=search]').on('blur focusOut', function (){
        $(this).css('border', '')
    });

    $('.td-container').hover(
        function(){
            $('.btnEditName').css('display', 'inline')
        },

        function(){
            $('.btnEditName').css('display', 'none')
        }
    )

});