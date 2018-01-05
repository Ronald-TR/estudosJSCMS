document.getElementById('heading').innerHTML = localStorage['title'] || 'Just Write';
document.getElementById('content').innerHTML = localStorage['content'] || 'This text is auto saved';

setInterval(function(){
    localStorage['title'] = document.getElementById('heading').innerHTML;
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
    var logtext = $("#logtext");
    logtext.text = data.toString();
    console.log(data);
    $.ajax({
        url: "/postingcms",
        method: "POST",
        success: function(result){
            alert(result);
        },
        data: data,
        crossDomain: false, 
    });

});