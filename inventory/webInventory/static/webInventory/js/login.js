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

});