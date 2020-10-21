$(function (){
   console.log("Java Script Works")

   /*Check if the login page is blank*/
   $('.logCred').on('blur', function (){
      if(!$.trim(this.value).length){
         $(this).addClass('warning')
      }else {
         $(this).removeClass('warning')
      }
   })

   /*For Alert*/
    $(".alert-danger").fadeTo(2000, 500).slideUp(500, function(){
        $(".alert-danger").slideUp(500);

    });

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
            $('.btnreset').attr('disabled', true)
        }else{
            $('.errors').text("")
            $('.btnreset').attr('disabled', false)
        }

    })

});