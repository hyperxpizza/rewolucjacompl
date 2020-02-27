$(function(){
    var ul = $("#menu");

    $(document).click(function(){
        ul.slideUp(400);
  });

  $("#logo_btn").on("click", function(e) {
    e.stopPropagation();
    ul.slideToggle(400);
  });

});