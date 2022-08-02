function login() {
    var username = $("#username").val();
    var password = $("#password").val();
    console.log(username.length)

    //validate
    if((username.length == 0 && password.length == 0) || (username.length == 0 && password.length != 0)){
        Swal.fire({
            icon: 'error',
            title: 'Input Field Required',
            text: 'Please Enter Your Username'
          })
    }else if(username.length != 0 && password.length == 0){
        Swal.fire({
            icon: 'error',
            title: 'Input Field Required',
            text: 'Please Enter Your Password'
          })
    }else{
        $.ajax({
            url: "/login",
            type: "POST",
            data: {
                'username': username,
                'password': password
            },
            success: function (response, errorThrown) {
                if(response == 'success'){
                    // Swal.fire(
                    //     'Login!',
                    //     'Login Successfully',
                    //     'success'
                    // )
                    window.location.href = '/index'
                }else{
                    console.log(errorThrown);
                    //to do error 404 zieq ajaq nanti
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Incorrect Username or Password',
                      })
                }
            },
            error: function (data, message, errorThrown) {
                console.log(errorThrown);
                console.log("failed");
                location.reload();
            },
        });
    }
}

function register() {

    //validate for Fullname 
    var fullname = $("#fullname").val();
    var error_message_fullname = document.getElementById("error_message_fullname");

    if (fullname.length == 0){
        error_message_fullname.style.display = "block";
    }

    //validate for username
    var username = $("#username").val();
    var error_message_username_1 = document.getElementById("error_message_username_1");
    var error_message_username_2 = document.getElementById("error_message_username_2");
    var error_message_username_3 = document.getElementById("error_message_username_3");

    if (username.length == 0){
        error_message_username_1.style.display = "block";
    }else{
        if(username.length <=4 ){
            error_message_username_1.style.display = "none";
            error_message_username_2.style.display = "block";
        }else{
            error_message_username_1.style.display = "none";
            error_message_username_2.style.display = "none";
        }
    }

    //validate for password
    var password = $("#password").val();
//     ^ represents the starting of the string.
//     (?=.*[a-z]) represent at least one lowercase character.
//     (?=.*[A-Z]) represents at least one uppercase character.
//     (?=.*\\d) represents at least one numeric value.
//     (?=.*[-+_!@#$%^&*., ?]) represents at least one special character.
//      . represents any character except line break.
//      + represents one or more times.
    var pattern = new RegExp(
        
        "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$"
      );
      var error_message_password_1 = document.getElementById("error_message_password_1");
      var error_message_password_2 = document.getElementById("error_message_password_2");
    
    if (password.length == 0) {
        error_message_password_1.style.display = "block";
    } else {
        if (pattern.test(password)) {
            error_message_password_1.style.display = "none";
            error_message_password_2.style.display = "none";
        } else {
            error_message_password_1.style.display = "none";
            error_message_password_2.style.display = "block";
        }
    }

    //validate for email
    var email = $("#email").val();
    var emailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var error_message_email_1 = document.getElementById("error_message_email_1");
    var error_message_email_2 = document.getElementById("error_message_email_2");
    
    if (email.length == 0){
        error_message_email_1.style.display = "block";
    }else{
        if (email.match(emailformat)){
            error_message_email_1.style.display = "none";
            error_message_email_2.style.display = "none";
        }else{
            error_message_email_1.style.display = "none";
            error_message_email_2.style.display = "block";
        }
    }

    //validate for phone number
    var phone_number = $("#phonenumber").val();
    var phone_number_format_1 = /^\d{10}$/;
    var phone_number_format_2 = /^\d{11}$/;
    var error_message_phone_number_1 = document.getElementById("error_message_phone_number_1");
    var error_message_phone_number_2 = document.getElementById("error_message_phone_number_2");

    if (phone_number.length == 0){
        error_message_phone_number_1.style.display = "block";
    }else{
        if(phone_number.match(phone_number_format_1) || phone_number.match(phone_number_format_2)){
            error_message_phone_number_1.style.display = "none";
            error_message_phone_number_2.style.display = "none";
        }else{
            error_message_phone_number_1.style.display = "none";
            error_message_phone_number_2.style.display = "block";
        }
    }
}
