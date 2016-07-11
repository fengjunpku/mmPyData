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
  //获取url中的参数
  /* window.location.href;
  function getUrlParam(name) {
      var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
      var r = window.location.search.substr(1).match(reg);  //匹配目标参数
      if (r != null) return unescape(r[2]); return null; //返回参数值
  }
  var UrlPar=getUrlParam('page');
  */
}

function jump(target){
  //ajax
  $.post('./query/',{'page':target},function(data)
  {
    $('.jumbotron').html(data);
    //自动生成目录
    tags = $(".jumbotron h1,.jumbotron h2");
    n = 0;
    c = "";
    tags.each(function() {
      $(this).before("<a class='target-offset' name='"+target+"+miao" + n + "'></a>");
      if ($(this).prop('tagName') == "H1") //不可用"h1"
      {
        c=c+"<a href='#"+target+"+miao"+n+"' class='list-group-item active'><p1>"+$(this).text()+"</p1></a>";
      }
      else 
      {
        c=c+"<a href='#"+target+"+miao"+n+"' class='list-group-item'><p2>"+$(this).text()+"</p2></a>";
      }
      n = n + 1;
    });
    //set title
    if(target!=null)
    {
      document.title=target;
      c=c+"<a href='#home' class='list-group-item'><b>Back to Main</b></a>";
      window.location.hash='#'+target;
    }
    else
    {
      document.title='MakrDown Notes';
      window.location.hash='#home';
    }
    $('.list-group').html(c);
  });
}

function showdiv() { 
  document.getElementById("bg").style.display ="block";
  document.getElementById("show").style.display ="block";
}
function hidediv() {
  document.getElementById("bg").style.display ='none';
  document.getElementById("show").style.display ='none';
}

window.onhashchange=function(){
  if(geturlpar()!=lasturlpar){
    jump(geturlpar());
    lasturlpar=geturlpar();
  }
};