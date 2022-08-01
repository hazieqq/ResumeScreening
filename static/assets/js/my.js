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