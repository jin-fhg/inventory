$(function (){
    console.log("Manage Users")
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

    var viewUsers = $('.user-table').DataTable({
       bFilter: true,
       bInfo: false,
       bLengthChange: true,
       bSort: true,
       pageLength: 10,
       language: { searchPlaceholder: "Search.."},
       });

    $('.addUser').on('click', function (){
        $('.frmAddUser').fadeToggle();
    });

    $('input[type=search]').add('select').on('focus', function (){

         $(this).css('border', '3px solid powderblue')
    });

    $('select').add('input[type=search]').on('blur focusOut', function (){
        $(this).css('border', '')
    });

    $('.btnEditName, .btnDelete, .btnReset').hover(
        function (){
        $(this).css('color', 'gray')
    },
    function (){
        $(this).css('color', 'black')
    }

    )

    $('#setPass').on('click', function (){
        if($(this).is(':checked')){
            $('input[type=password]').slideToggle()
            $('input[type=password]').attr('required', true);
        }else{
            $('input[type=password]').slideToggle()
            $('input[type=password]').attr('required', false);
        }
    })

    $(".alert-success, .alert-danger").fadeTo(2000, 500).slideUp(500, function(){
       $(".alert-success, .alert-danger").slideUp(500);
    });

    //Passing ID for Delete
    $('.btnDelete').on('click', function (){
        db_id =$(this).closest('tr').find('.handleId').val()
        $('.deleteOptionId').val(db_id)
    })

    //Passing ID for Edit
    $('.btnEditName').on('click', function (){
        db_id =$(this).closest('tr').find('.handleId').val()
        $('.idHandlerUpdate').val(db_id)
        $.ajax({
            type: 'GET',
            url: 'profile/',
            data: {
                id: db_id,
            },
            success: function (data){
                $('.userName').text(data['uname'])
                $('.profileName').val(data['name'])
                $('.profileAddress').val(data['address'])
                $('.profilePhone').val(data['phone'])
                $('.profileEmail').val(data['email'])
            }

        })
    });

    $('.btnReset').on('click', function(){
        $('.resetMessage').text("Loading...")
        $('.modal-footer').css('display', 'none')
        db_id =$(this).closest('tr').find('.handleId').val()
        $.ajax({
            type: 'GET',
            url: 'reset/',
            data: {
                id: db_id
            },
            success: function(data){
                console.log("Email Sent to " + data.email)
                $('.resetMessage').text("Password Reset Email was Successfully Sent to " + data.email)
                $('.modal-footer').css('display', 'block')
            },
        })
    });


    $('.disableUser').on('click', function(){
        db_id =$(this).closest('tr').find('.handleId').val()
        var csrfmiddlewaretoken = $(this).closest('tr').find('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: 'POST',
            url: 'disable/',
            data: {
                id: db_id,
                csrfmiddlewaretoken: csrfmiddlewaretoken,
            },
            success: function(data){
                console.log(data)
                location.reload();
            },
        })
    })

    //For Set Password

    $('.pword').keyup(function (){
        if($(this).val().length < 8 ){
            console.log("Password is too short")
            $('.errors').text("Password is too short. It should be atleast 8 characters")
            $('.btnreset').attr('disabled', true)
        }else{
            $('.errors').text("")
            $('.btnreset').attr('disabled', false)
        }

    })

    $('.pword2').keyup(function (){
        if($(this).val() !== $('.pword').val()){
            console.log("Password Does not Match")
            $('.errors').text("Password Does not Match")

        }else{
            $('.errors').text("")

        }

    })



})