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

    $('.btnEditName, .btnDelete').hover(
        function (){
        $(this).css('color', 'gray')
    },
    function (){
        $(this).css('color', 'black')
    }

    )

})