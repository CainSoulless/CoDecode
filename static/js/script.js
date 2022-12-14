/* 
Manipulate all the modals displays and check if the options are properly
selected.
*/

var optionSelection = document.getElementById('encode-options')

optionSelection.addEventListener("click", function() {
    // Option
    var encodeOption = document.getElementById("encode-options");
    var value = encodeOption.options[encodeOption.selectedIndex].text;
    console.log(value);

    if (value == "AES_EAX") {
        // Key generator
        document.getElementById("btn-generator").removeAttribute("disabled");

        // Modal
        document.getElementById("btn-download").style.display = "flex";
        document.getElementById("btn-email-confirmed").style.display = "flex";
        document.getElementById("modal-body").innerHTML = 
            "Remeber: The AES_EAX decryption needs 2 things, your key and the file " + 
            "with download option below. The person who want to decrypt the email " + 
            "needs these two stuff. And remember, take care your key.";
    }
    else {
        document.getElementById("key").setAttribute("disabled", "");
        document.getElementById("key").value =  "";
        document.getElementById("btn-generator").setAttribute("disabled", "");

        // Modal
        document.getElementById("modal-body").innerHTML = 
            "Please confirm to send the email."
        document.getElementById("btn-download").style.display = "none";
        document.getElementById("btn-email-confirmed").style.display = "flex";
    }
})

let body = document.getElementById('body')
let email = document.getElementById('email_receiver')

if ((optionSelection.selectedIndex == "-1" || 
     body == "" || email == "")) {
    document.getElementById("modal-body").innerHTML = 
        "Please fill all the needed options." 
    document.getElementById("btn-download").style.display = "none";
    document.getElementById("btn-email-confirmed").style.display = "none";
} 