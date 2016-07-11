$(document).ready(function () {
  $('[data-toggle="offcanvas"]').click(function () {
    $('.row-offcanvas').toggleClass('active')
  });
});
var lasturlpar='';
//获取url中的参数
function geturlpar(){
  if(window.location.hash){
    var reg = new RegExp("[A-z]+[A-z]");
    var r = window.location.hash.substr(1).match(reg);
    return unescape(r[0]);
  }
  else
    return null;
}

function loading(){
  jump(geturlpar());
  lasturlpar=geturlpar();
}

function jump(target){
  //ajax
  $.post('./query/',{'page':target,'type':'hist'},function(data)
  {
    $('.jumbotron').html(data);

    //set title
    if(target!=null)
    {
      document.title="mmPyData-"+target;
      window.location.hash='#'+target;
    }
    else
    {
      document.title='mmPyData';
      window.location.hash='#home';
    }
  });
}

window.onhashchange=function(){
  if(geturlpar()!=lasturlpar){
    jump(geturlpar());
    lasturlpar=geturlpar();
  }
};
//----------
$("ul li").click(function(){
  $("ul li.active").removeClass("active");
  $(this).addClass("active");
});