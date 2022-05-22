
function Setupforcards(){
    $(document).ready(function(){
       $(".wrapper__loginform-eye").click(function(){
            $(this).toggleClass("reveal"); //$(this): lệnh này trỏ đến thẻ đang được gọi cho sự kiện click, cụ thể là thẻ div có class là .wrapper__loginform-eye.
            $(this).children("i").toggleClass("fal fa-eye far fa-eye-slash");
            if($(this).hasClass("reveal"))
                $(".wrapper__loginform-input-password").attr("type", "text");
            else
                $(".wrapper__loginform-input-password").attr("type", "password");
       });
    });
}

