$(document).ready(function() {

    function outputVisualization() {
        $.ajax( {
            url: "/output-visualization",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                message: $("#body").val(),
                encode_option: $("#encode-options option:selected").val(),
                key: $("#key").val()
            }),
            success: function(response) {
                $("#message_output").text(response.output)
            }
        })
    };

    function keyGenerator() {
        $.ajax( {
            url: "/key-generator",
            type: "GET",
            contentType: "application/json",

            success: function(response) {
                $("#key").val(response.key_generator)
            }
        })
    };

    function emailConfirmated() {
        $.ajax( {
            url: "/email-confirmated",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                email_receiver: $("#email_receiver").val(),
                subject: $("#subject").val(),
                encode_option: $("#encode-options option:selected").val(),
                key: $("#key").val(),
                message: $("#body").val()
            }),
        });
    };

    function decode() {
        $.ajax( {
            url: "/decoded",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                message: $("#body").val(),
                encode_option: $("#encode-options option:selected").val(),
                key: $("#key").val()
            }),
            success: function(response) {
                $("#message_output").text(response.output)
            },
        });
    };

    function upload() {
        $.ajax( {
            url: "/upload",
            type: "POST",
            cache: false,
            contentType: false,
            processData: false,
            data: form_data,
            dataType: "json",
            success: function(response) {
                console.log("success");
            }
        });
    };


    $("#btn-email-confirmed").click(function() {
        emailConfirmated();
    })

    $("#btn-decode").click(function() {
        // var form_data = new FormData();
        // alert(JSON.stringify(form_data))
        upload();
        decode();
    })

    $("#btn-output").click(function() {
        outputVisualization();
    })

    $("#btn-generator").click(function() {
        keyGenerator();
    })
})
