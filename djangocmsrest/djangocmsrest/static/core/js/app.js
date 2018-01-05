document.getElementById('title').innerHTML = localStorage['title'] || 'Just Write';
document.getElementById('content').innerHTML = localStorage['content'] || 'This text is auto saved';

setInterval(function(){
    localStorage['title'] = document.getElementById('title').innerHTML;
    localStorage['content'] = document.getElementById('content').innerHTML;
}, 1000);



$("#btn_text").click(function(){
    var token = $("#box_text").children()[1-1];
    var tokenname = token.name;
    var data = {
          csrfmiddlewaretoken: token.value,
          title: localStorage['title'],
          content: localStorage['content'],
    }
    
    $.ajax({
        url: "/postingcms",
        method: "POST",
        success: function(result){
            document.getElementById("logtext").innerHTML = result;
        },
        data: data,
        crossDomain: false, 
    });

});