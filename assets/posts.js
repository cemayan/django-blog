
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
      user : null,
      id:0,
      postStatus : true
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
     createPost: function(data){

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
     },

     editPost: function(pk){
      vue.postStatus = false
      $('.modal').modal('show');
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
            //document.querySelector("#title").value =   data_.data.title
            $('#editor').trumbowyg('html', data_.data.html);

          self.title = data_.data.title
          self.html = $('#editor').trumbowyg('html')
          self.created_date = data_.created_date
          self.user = data_.user
          self.id = data_.id


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
      
     },
     updatePost : function(obj){
      var self= this  
      fetch('http://127.0.0.1:8000/api/',{
        method: 'PUT',
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body : JSON.stringify({"id":self.id,"data":{"title": self.title,"html":self.html}})

      }).then(response => {if(response.ok){self.fetchData()}  })
     }
    }
  })
  
}



