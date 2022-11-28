document.getElementById('encode-options').addEventListener("click", function() {
    // Option
    var encodeOption = document.getElementById("encode-options");
    var value = encodeOption.options[encodeOption.selectedIndex].text;


    if (value == "AES_EAX") {
        // Key generator
        document.getElementById("key").removeAttribute("disabled");
        document.getElementById("btn-generator").removeAttribute("disabled");
    } else {
        document.getElementById("key").setAttribute("disabled", "");
        document.getElementById("key").value =  "";
        document.getElementById("btn-generator").setAttribute("disabled", "");
    }

})