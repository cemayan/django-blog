document.addEventListener('DOMContentLoaded', function() {
  var reply_button = document.querySelector("#reply_button")
  reply_button.addEventListener('click',function(e){


  
    fetch('http://127.0.0.1:8000/api/comment/',{
      method: 'POST',
      credentials: "same-origin",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Accept": "application/json",
          "Content-Type": "application/json"
      },
      body : JSON.stringify({"post":document.location.pathname.split("/")[2],"data":{"comment":document.querySelector("#comment").value}})
      
    }).then(response => {if(response.ok){}  })
    
  
  })
})












