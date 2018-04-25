if(document.location.href.indexOf('login')>0){
  var app = new Vue({ 
    el: '#app',
    data : {
      status : "",
      username :"",
      password : ""
    },
    computed : {
      nullCheck : function(data){
        return  this.username=="" || this.password=="" ? "disabled" : null
   
      }
    
    }
  })
}
