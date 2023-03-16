window.addEventListener('pywebviewready', function() {
    var disassemble_button = document.getElementById('disassemble_button');
    var python_form_textarea = document.getElementById('python_form_textarea');
    var bytecode_form_textarea = document.getElementById('bytecode_form_textarea');

    var copyright_text = document.getElementById("copyright_text");

    pywebview.api.get_display_name().then(function (display_name) {
        copyright_text.innerHTML = display_name + " - " + copyright_text.innerHTML;
    })

    disassemble_button.addEventListener("click", function () {
        pywebview.api.to_bytecode(python_form_textarea.value).then(function (bytecode_string) {
            bytecode_form_textarea.innerText = "";

            for (var i = 0; i < bytecode_string.length; i++) {
                var text = document.createTextNode(bytecode_string[i]);
                bytecode_form_textarea.appendChild(text);

                var br = document.createElement("br");
                bytecode_form_textarea.appendChild(br);
            }
        })
    })
    
})