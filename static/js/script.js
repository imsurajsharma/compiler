var editor = ace.edit("editor");


function getvalue(){
var code = editor.getValue();
var input = document.getElementById('input').value;
console.log(input);
$.post( "", { compile:code,input:input,  csrfmiddlewaretoken: '{{ csrf_token }}' })
.done(function( data ) {
console.log(data);

for (var key in data) {
if (data.hasOwnProperty(key)) {
  var val = data[key];

document.getElementById("output").innerHTML =val.join("<br>")+'';

}

}

});

}



function setupEditor()
{
window.editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.getSession().setMode("ace/mode/python");
editor.setValue();
editor.focus();


editor.setOptions({
fontSize: "16pt",
showLineNumbers: false,
showGutter: false,
vScrollBarAlwaysVisible:true,
enableBasicAutocompletion: false, enableLiveAutocompletion: false
});

editor.setShowPrintMargin(false);
editor.setBehavioursEnabled(false);
}



setupEditor();
update();


$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });
});
