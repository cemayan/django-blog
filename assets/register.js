if(document.location.href.indexOf('register')>0){
var app = new Vue({ 
  el: '#app',
  data : {
    status : "",
    firstname: "",
    lastname: "",
    username :"",
    password : "",
    password1:"",
    email:""
  },
  computed : {
    nullandPasswordCheck : function(data){
      if(this.username!="" && this.password!="" && this.firstname!="" && this.lastname!="" && this.password1!="" && this.email!= "") {
        if(this.password == this.password1){
          return null
        }
        else{
          return "disabled"
        }
      }
      else{
        return "disabled"
      }
    }
  },
})
}