

$(document).ready(function (){
    var verify = $("#chk_td").length;
        if (verify == 0) {
            $("#no-data").text("Не найдено по параметрам");
        }

});


setInterval(function () {
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ":" +
        (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" +
        (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);


function validateEmail(email){
    const regex =
  /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    return regex.test(email);
}

function validateAll(){
    var name = $('#name').val();
    var phone = $('#phone').val();
    var email = $('#email').val();
    var age = $('#age').val();
    var gender = $('#gender').val();

    if(name == ''){
        swal('Упс!','Поле "ФИО" не может быть пустым.', 'error')
        return false;
    }
    else if (name.split(' ').length < 2){
        swal('Упс!','Укажите фамилию!', 'info')
        return false;
    }
    else if(phone == ''){
        swal('Упс!','Поле "Телефон" не может быть пустым.', 'error')
        return false;
    }
    else if(email == ''){
        swal('Упс!','Поле "Email" не может быть пустым.', 'error')
        return false;
    }
    else if(validateEmail(email) == false){
        console.log(validateEmail(email))
        swal('Упс!','Проверьте поле "Email".', 'error');
        return false;
    }
    else if(age == ''){
        swal('Упс!','Поле "Возраст" не может быть пустым.', 'error')
        return false;
    }
    else if(gender == ''){
        swal('Упс!','Поле "Пол" не может быть пустым.', 'error')
        return false;
    }
}

$("#btn-add").bind("click", validateAll);

$(document).ready(function (){
    jQuery('input[name="name"]').keyup(function (){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Zа-яА-Я _]/g, '');
        jQuery(this).val(allow);
    });
    $("input").on("keypress", function (e) {
        if (e.which == 32 && !this.value.length)
            e.preventDefault();
    });
});

$(document).ready(function (){
   $("#phone").inputmask("999-999-9999", {"onincomplete": function (){
       swal('Упс!','Ошибка в поле "Телефон"!', 'error');
       return false;
        }
   });


    $("#age").keyup(function () {
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^0-9_]/g, '');
        jQuery(this).val(allow);
    });
});