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
    
    console.log({data:{title:title.value,html:content.trumbowyg('html')}})
  } 
  else{
    e.preventDefault()
  }
})

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
          c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
          return c.substring(name.length, c.length);
      }
  }
  return "";
}


fetch('/api',{
  method: "get",
  credentials: "same-origin",
  headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Accept": "application/json",
      "Content-Type": "application/json"
  }, 
}).then(x=>x.json()).then(function(data){
  console.log(data)
})