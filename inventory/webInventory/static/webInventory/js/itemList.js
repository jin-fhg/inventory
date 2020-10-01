$(function (){
    console.log("Item List")
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

    var viewItems = $('.itemList').DataTable({
       bFilter: true,
       bInfo: false,
       bLengthChange: true,
       bSort: true,
       pageLength: 10,
       language: { searchPlaceholder: "Names.."},
       });

    $('input[type=search]').add('select').on('focus', function (){

         $(this).css('border', '3px solid powderblue')
    });

    $('select').add('input[type=search]').on('blur focusOut', function (){
        $(this).css('border', '')
    });


    /*For Alert*/
    $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){
       $(".alert-success").slideUp(500);
    });



});