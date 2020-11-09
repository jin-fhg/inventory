$(function (){
    console.log("Tag List")
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

    var viewTags = $('#tagList').DataTable({
       bFilter: true,
       bInfo: false,
       bLengthChange: true,
       bSort: true,
       pageLength: 10,
       language: { searchPlaceholder: "Search.."},
       });

    $('.addTag').on('click', function (){
        $('.frmAddTag').fadeToggle();
    });

    $('input[type=search]').add('select').on('focus', function (){

         $(this).css('border', '3px solid powderblue')
    });

    $('select').add('input[type=search]').on('blur focusOut', function (){
        $(this).css('border', '')
    });

    $('.btnEditName, .btnDelete').hover(
        function (){
        $(this).css('color', 'gray')
    },
    function (){
        $(this).css('color', 'black')
    }

    )

    $('.btnEditName').on('click', function (){
        txt = $(this).closest('tr').find('p').text()
        $(this).closest('tr').find('.txtEditTagName').val(txt)
        $(this).closest('tr').find('.txtEditTagName, p').toggle()
        $(this).closest('tr').find('.txtEditTagName, p').focus()
    })

    $('.txtEditTagName').on('blur focusOut', function (){
       if($(this).val() == '') {
           alert("Please Enter a Value")
           $(this).css('border-bottom', '2px solid red')
       }
       else{
               $(this).closest('tr').find('p,.txtEditTagName').toggle();
               $(this).closest('tr').find('p').text($(this).val());
               var db_id = $(this).attr('db_id')
               var txtVal = $(this).val()
               var csrfmiddlewaretoken = $(this).closest('tr').find('input[name=csrfmiddlewaretoken]').val();
               console.log(db_id, txtVal, csrfmiddlewaretoken)
               $.ajax({
                       type: 'POST',
                       url: 'update/',
                       data: {
                           update: 'tagNameUpdate',
                           id: db_id,
                           value: txtVal,
                           csrfmiddlewaretoken: csrfmiddlewaretoken,
                       }
                   })
       }
    });

    $('.btnDelete').on('click', function (){
        tag_id = $(this).closest('tr').find('.txtEditTagName').attr('db_id')
        $('.deleteOptionId').val(tag_id)
    })

    /*For Alert*/
    $(".alert-success, .alert-danger").fadeTo(2000, 500).slideUp(500, function(){
       $(".alert-success").slideUp(500);
    });

})