

if(document.location.pathname =="/"){
  var vue = new Vue({
    el : '#posts',
    data: {
      posts :null,
      isAuthUser : false,
      trash : "trash icon grey",
      edit : "edit icon blue",
      title : "",
      html : "",
      created_date :null,
      user : null
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
     },
     editPost: function(pk){
      $('.modal-edit').modal('show');
      var self= this  
      fetch('/api/'+pk,{
          method: "get",
          credentials: "same-origin",
          headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              "Content-Type": "application/json"
          }, 
        }).then(x=>x.json()).then(function(data_){
            document.querySelector("#title_edit").value =   data_.data.title
            $('#editor_edit').trumbowyg('html', data_.data.html);

          self.html =
          self.created_date = data_.created_date
          self.user = data_.user



        })


     },
     deletePost : function(pk){
      var self= this  
      fetch('/api/'+pk,{
        method: "delete",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
      }).then(function(data){
       var y =  self.posts.filter(x=>{
          return x.id != pk 
        })
          Vue.set(self, "posts" ,y)
      })
      
     }
    }
  })
  
}



