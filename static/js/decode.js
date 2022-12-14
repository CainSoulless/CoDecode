/* 
Manipulate if the decode options are properly selected.
*/

var optionSelection = document.getElementById('encode-options')

optionSelection.addEventListener("click", function() {

    // Option
    var encodeOption = document.getElementById("encode-options");
    var value = encodeOption.options[encodeOption.selectedIndex].text;

    if (value == "AES_EAX") {
        document.getElementById("key").removeAttribute("disabled");
        document.getElementById("key-line-1").removeAttribute("disabled");
        document.getElementById("key-line-2").removeAttribute("disabled");
    }
    else {
        // Ensure these attributes are not setted.
        btn_decode.removeAttribute("data-bs-toggle");
        btn_decode.removeAttribute("data-bs-target");

        // Set disabled attribute in case the option selected is not "AES-EAX"
        document.getElementById("key").setAttribute("disabled", "");
        document.getElementById("key-line-1").setAttribute("disabled", "");
        document.getElementById("key-line-2").setAttribute("disabled", "");

        // Restoring defailt values.
        document.getElementById("key").value =  "";
        document.getElementById("key-line-1").value = "";
        document.getElementById("key-line-2").value = "";
    }
})

var btn_decode = document.getElementById('btn-decode')

btn_decode.addEventListener("click", function() {
    // Option
    var encodeOption = document.getElementById("encode-options");
    var value = encodeOption.options[encodeOption.selectedIndex].text;

    if (value == "AES_EAX") {
        let line1 = document.getElementById("key-line-1").value;
        let line2 = document.getElementById("key-line-2").value;
        let key = document.getElementById("key").value;

        // Modal
        if (line1 == "" || line2 == "" || key == "") {
            btn_decode.setAttribute("data-bs-toggle", "modal");
            btn_decode.setAttribute("data-bs-target", "#exampleModal");
            document.getElementById("modal-body").innerHTML = 
                "Please fill all the needed options.";
        }
    }

    btn_decode.click();
})