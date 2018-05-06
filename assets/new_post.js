
var write_btn = document.querySelector("#submit-post")
var title = document.querySelector("#title")
var content = $("#editor");

$(document).ready(function() {
  $('.my-editor').trumbowyg();
});

$('.editor').click(function(){
  document.querySelector("#title").value = ""
  $("#editor").trumbowyg('empty');

  $('.modal').modal('show');
  vue.postStatus = true
})


//Write Button Click



write_btn.addEventListener('click',function(e){


  fetch('http://127.0.0.1:8000/api/',{
    method: 'POST',
    credentials: "same-origin",
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body : JSON.stringify({"data":{"title": document.querySelector("#title").value,"html":$("#editor").trumbowyg('html')}})
    
  }).then(response => {if(response.ok){vue.fetchData()}  })
  

})











