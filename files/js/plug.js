define(["jquery"], function ($) {
  
  return {
      switch: function(pid, callback){
          
          
          $.ajax({
            url:"/api/plug",
            type:"POST",
            data: JSON.stringify({id:pid}),
            processData: false,
            contentType:"application/json; charset=utf-8",
            dataType:"json",
            success: function(data){
                //data = JSON.parse(data);
                callback(pid, data);
            }
          });
      }
      
      
  };
  
});