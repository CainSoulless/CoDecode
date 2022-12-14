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

    // function emailConfirmated() {
    //     $.ajax( {
    //         url: "/email-confirmated",
    //         type: "POST",
    //         contentType: "application/json",
    //         data: JSON.stringify({
    //             email_receiver: $("#email_receiver").val(),
    //             subject: $("#subject").val(),
    //             encode_option: $("#encode-options option:selected").val(),
    //             key: $("#key").val(),
    //             message: $("#body").val()
    //         }),
    //     });
    // };

    function decode() {
        $.ajax( {
            url: "/decode",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                message: $("#body").val(),
                encode_option: $("#encode-options option:selected").val(),
                key: $("#key").val(),
                line1: $("#key-line-1").val(),
                line2: $("#key-line-2").val()
            }),
            success: function(response) {
                $("#message_output").text(response.output)
            },
        });
    };

    function sendEmail() {
        $.ajax( {
            url: "/send-email",
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
    }

    $("#btn-send").click(function() {
        sendEmail();
    })

    // $("#btn-email-confirmed").click(function() {
    //     emailConfirmated();
    // })

    $("#btn-decode").click(function() {
        decode();
    })

    $("#btn-output").click(function() {
        outputVisualization();
    })

    $("#btn-generator").click(function() {
        keyGenerator();
    })
})
