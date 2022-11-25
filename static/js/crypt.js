
function messageEncode() {
    // Left side of home.html
    var emailDestination = document.getElementById("destination").innerHTML;
    var encodeOption = document.getElementById("encode-options").value;
    var subject = document.getElementById("subject").innerHTML;
    var body = document.getElementById("body").value;
    let output;

    console.log(encodeOption);
    // Getting selected option
    if (encodeOption == "base64") {
        output = btoa(body);
        console.log(atob(output));
    }
    else if (encodeOption == "SHA-256") {
        output = window.crypto.getRandomValues(new Uint8Array(10));
        console.log(secure);
    }
    else {
        output = body;
    }

    // Right side of home.html
    document.getElementById("message_output").value = output;
}
