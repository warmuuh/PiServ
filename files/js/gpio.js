define(["jquery"], function ($) {
     
  var pins = [];
  
  return {
  
    getPins: function(){
      return pins;
    },
    
    
    pollState: function(onSuccess, context) {       
       $.getJSON("/api/gpio",  function(data) { 
            pins = data;
            onSuccess.call(context);
         });
    },
    
    switchState: function(pinId, callback) {
      var pin = pins[pinId];
      pin.state = (pin.state-1) * -1;  //toggles 0 and 1
      /*$.post("/api/gpio/" + pinId,  JSON.stringify(pin), function(data, textStatus) {
          //data contains the JSON object
          //textStatus contains the status: success, error, etc
        }, "json");
        */

      $.ajax({
        url:"/api/gpio/" + pinId,
        type:"POST",
        data: JSON.stringify(pin),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(data){
            //data = JSON.parse(data);
            callback(pinId, data);
        }
      });
    }
    
    
  
  };
});