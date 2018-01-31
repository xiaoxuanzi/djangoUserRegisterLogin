

$(function () {


    $('#regist').click(function () {
        window.location.href = '/accounts/regist.html'
    });

    $('#quit_regist').click(function () {
        window.location.href = "/"
    });

    $('#check_regist').click(function () {
        var user = $('#ac_username').val();
        var chk_pass = $('#ac_chk_password').val();
        var pass = $('#ac_password').val();
        var email = $('#ac_email').val();

        if (user == '') {
            window.alert('请输入用户名!');
            return false;
        }else {
            $.ajax({
                url: '/accounts/ac_user?username=' + user,
                type: 'GET',
                async: true,
                success: function (data) {
                    if (data != 0){
                        var msg = user + '已存在,请更改其他为其他用户名!';
                        var res = confirm(msg);
                        if (res == true || res == false){
                            $('#ac_username').val('');
                            return false;
                        }
                        else{

                        }
                    }
                    else{

                    }
                },
                error: function () {
                    return false;
                }
            })
        }

        if (user.length < 3) {
            window.alert('用户名长度必须大于3!');
            return false;
        }

        if (pass == '') {
            alert('请输入密码!');
            return false;
        }

        if (pass.length < 6) {
            alert('密码长度必须大于6!');
            $('#ac_password').val('');
            return false;
        }

        if (pass != chk_pass) {
            alert('密码不一致!');
            $('#ac_chk_password').val('');
            return false;
        }
        if (email == '' || email.split('@')[1] != 'sohu-inc.com') {
            alert('请输入公司Email!');
            $('#ac_email').val('');
            return false;
        }

        $('form').submit();
    });




    $('#ack_new_pass').click(function () {
        var new_pass = $('#new_password').val();
        var ac_new_pass = $('#ac_new_password').val();

        if (new_pass == '') {
            alert('请输入密码!');
            return false;
        }

        if (new_pass.length < 6) {
            alert('密码长度必须大于6!');
            $('#new_password').val('');
            return false;
        }
        if (new_pass != ac_new_pass) {
            alert('密码不一致!');
            $('#ac_chk_password').val('');
            return false;
        }

        $('form').submit();

    });

    $('#quit_new_pass').click(function () {
        window.location.href = '/';
    })


    $('#reset_pass_sub').click(function () {
        var email = $('#reset_pass_email').val();
        console.log(email);
        debugger;
        if (email == '' || email.split('@')[1] != 'sohu-inc.com') {
            alert('请输入公司Email!');
            $('#ac_email').val('');
            return false;
        }
        else{
            $('form').submit();
        }
    })



});

