$(function(){
    var al = $("#storeMenu");

    $(document).click(function(){
        al.slideUp(400);
  });

  $("#sklep").on("click", function(e) {
    e.stopPropagation();
    al.slideToggle(400);
  });

});