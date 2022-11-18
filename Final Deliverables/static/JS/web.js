function preview() {
    frame.src=URL.createObjectURL(event.target.files[0]);
    document.getElementById("frame").style.display = "block";
}
$(document).ready(function() {
    $('#clear').on('click', function() {
        $('#image').val('');
        $('#frame').attr('src',"");
        });
});
function clear(){
    document.getElementById("d62").style.display="none";
 }