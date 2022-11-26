$(document).ready(function() {

    $("#btn-output").click(function() {
        $.ajax( {
            url: "",
            type: "get",
            contentType: "application/json",
            data: {
                message_body: $("#body").val()
            },
            success: function(response) {
                $("#message_output").text(response.body)
            }
        })
    })
})