$(document).ready(function() {
  $('.my-editor').trumbowyg();
});

$('.editor').click(function(){
  $('.ui.modal').modal('show');
})


//Write Button Click

var write_btn = document.querySelector("#write")
var title = document.querySelector("#title")
var content = $(".my-editor");

write_btn.addEventListener('click',function(e){

  if(title.value!="" && content.textContent!=""){

    fetch('http://127.0.0.1:8000/api/',{
      method: 'POST',
      credentials: "same-origin",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Accept": "application/json",
          "Content-Type": "application/json"
      },
      body : JSON.stringify({"data":{"title":title.value,"html":content.trumbowyg('html')}})
      
    }).then(response => {if(response.ok){vue.fetchData()}})
    
  } 
  else{
    e.preventDefault()
  }
})





