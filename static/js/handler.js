$(document).ready(function() {

    $("#btn-output").click(function() {
        $.ajax( {
            url: "",
            type: "GET",
            contentType: "application/json",
            data: {
                message_body: $("#body").val(),
                encode_option: $("#encode-options option:selected").val()
            },
            success: function(response) {
                $("#message_output").text(response.output)
            }
        })
    })
})