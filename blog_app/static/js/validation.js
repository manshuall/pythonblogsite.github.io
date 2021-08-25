$(document).ready(function () {
    $('#error1').hide();
    $('#error2').hide();

    let user_error = true;
    let user_pass = true;

    $('#email').keyup(function () {
        validation_error();
    })



    function validation_error() {
        let check = $('#email').val()
        if (check.length == "") {
            $('#error1').show();
            $('#error1').html("Plese Enter User Name");
            user_error = false;
            return false;
        }
        else if (check.length < 3 || check.length > 50) {
            $('#error1').show();
            $('#error1').html("User must be grader than 2 and lesser than 50");
            user_error = false;
            return false;
        }
        else
            $('#error1').hide();

    }
    // VALIDATION FOR PASSWORD
    
    $('#password').keyup(function () {
        password_validation();
    })
    function password_validation() {
        let pass_check = $('#password').val();
        if (pass_check.length == "") {
            $('#error2').show();
            $('#error2').html("Plese Enter password")
            user_pass = false;
            return false;

        }
        else {
            if (pass_check.length < 6) {
                $('#error2').show();
                $('#error2').html("Password must me 6 digit or more");
                user_pass = false;
                return false;
            }
            else {
                $('#error2').hide();
            }
        }
    }

    $('#submit').click(function(){

        user_error = true;
        user_pass = true;
        validation_error();
        password_validation();
        if(user_error==true && user_pass==true)
        {
            return true;
        }
        else
        {
            return false;
        }
    })



        // validation of singup modal
        $('#error_con_pass').hide();
        let user_pass_sign_up=true;
        $('#user_con_pass').keyup(function(){
            user_pass_get_val();
        })
        function user_pass_get_val()
        {
            let pass_value=$('#user_pass').val();
            let con_pass_value=$('#user_con_pass').val();
            $('#error_con_pass').css("color","red");
            if(con_pass_value.length=="")
            {
                $('#error_con_pass').show();
                $('#error_con_pass').html("plese enter Password to confirm")
                user_pass_sign_up=false;
                return false;
            }
             else if(pass_value!=con_pass_value)
             {
                $('#error_con_pass').show();
                $('#error_con_pass').html("Password not Match");
                user_pass_sign_up=false;
                return false;
             }
             else if(pass_value==con_pass_value && con_pass_value==pass_value)
                    $('#error_con_pass').hide();    
        }

        $('#sign_up').click(function(){
            user_pass_sign_up=true;
            console.log(user_pass_get_val());
            if(user_pass_sign_up==true)
                {
                    return true;
                }
            else
                {
                    return false;
                }
        })





})