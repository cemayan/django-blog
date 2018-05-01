
if(document.location.pathname =="/"){
  var vue = new Vue({
    el : '#posts',
    data: {
      posts :null
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
          }).then(x=>x.json()).then(function(data){
            if(typeof(data)==="string"){
              var arr=[]
              JSON.parse(data).some(function(obj){
                  arr.push(JSON.stringify(obj))
              })
              self.posts = arr
            }else{
              self.posts = data
            }
          })
      },
    }
  })
  
}
