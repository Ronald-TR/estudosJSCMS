/*try {
    document.getElementById('title').innerHTML = localStorage['title'] || 'Just Write';
    document.getElementById('content').innerHTML = localStorage['content'] || 'This text is auto saved';
} catch (error) {

}

setInterval(function(){
    localStorage['title'] = document.getElementById('title').innerHTML;
    localStorage['content'] = document.getElementById('content').innerHTML;
}, 1000);
*/
$("#btn_text").click(function(){
    
    var token = $("#boxcontent").children()[0];
    var tokenname = token.name;
    
    var data = {
          csrfmiddlewaretoken: token.value,
          text: CKEDITOR.instances.box_text.getData(),
    }
    $.ajax({
        url: "/postsave",
        method: "POST",
        success: function(result){
             alert(result);
        },
        data: data,
        crossDomain: false, 
    });
});

function ChangeActionOnSubmit(AformId, Aaction){
    form = $(AformId)[1-1];
    form.action = Aaction;
    form.submit();
}
