

if(document.location.pathname =="/"){
  var vue = new Vue({
    el : '#posts',
    data: {
      posts :null,
      isAuthUser : false,
      trash : "trash icon"
    },
    created: function () {
      this.fetchData()

    },
    methods: {
      fetchData : function(){
        var self= this  
        fetch('/api',{
            method: "get",
            credentials: "same-origin",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"
            }, 
          })
          .then(x=>x.json()).then(function(data){
            if(typeof(data)==="object"){
              var arr=[]
              data.some(function(obj){
                arr.push(JSON.parse(obj))
              })
              self.posts = arr
            }else{
              if(data!=null){
                self.posts =  JSON.parse(data);
              }   
            }
          })
      },
      checkLimit : function(data){
        if (data.length>30){
          return data.substring(0,25)
        }else{
          return data
        }    
      },
      isAuthUser_ : function(data){
        return  data==document.querySelector("#user_id").value? true : false
     }
    }
  })
  
}
