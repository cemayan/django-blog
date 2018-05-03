if(document.location.pathname.indexOf("posts")>=0){
var vue_detail = new Vue({
  el : '#post_detail',
  data: {
    title :null,
    html : null,
    created_date :null,
    user :null
  },
  mounted: function () {
    this.fetchData()
  },
  methods: {
    fetchData : function(){
      var self= this  
      fetch('/api/'+document.location.pathname.split("/")[2],{
          method: "get",
          credentials: "same-origin",
          headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              "Content-Type": "application/json"
          }, 
        }).then(x=>x.json()).then(function(data_){
            self.title = data_.data.title
            self.html = data_.data.html
            self.created_date = data_.created_date
            self.user = data_.user
        })
    },
  }
})
}