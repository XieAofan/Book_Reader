data = '';
x = document.getElementById("f");
content = [];
nr = '';
function get_content(url,index){
    r = nr;
    if(r==''){
        $.get("https://read.xieaofan.top/reader3/getBookContent",{'url':url,'index':index},function(redata,status){
        data = redata['data'];
        data = data.split('\n');
        $('#content').empty();
        for(var i=0,len=data.length; i<len; i++){
            data[i] = data[i].replace(/^\s+|\s+$/g,'');
            if(data[i]!=''){
                var n = '<p>'+data[i]+'</p>';
                $('#content').append(n);};
            }
      });
    }
    
    $.get("https://read.xieaofan.top/reader3/getBookContent",{'url':url,'index':index+1},function(redata,status){
        data = redata['data'];
        nr = data;
      });
      window.history.pushState({}, 0, window.location.href.split('&myid=')[0] + '&myid=' + index);
      data = r.split('\n');
        $('#content').empty();
        for(var i=0,len=data.length; i<len; i++){
            data[i] = data[i].replace(/^\s+|\s+$/g,'');
            if(data[i]!=''){
                var n = '<p>'+data[i]+'</p>';
                $('#content').append(n);};
            }
    
};

function next_chapter(){
    $("#nextl").show();
    index++;
    get_content(url,index);
    $("#nextl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>');
    i=0;
    next_page(i);
};

function last_chapter(){
    $("#lastl").show();
    index--;
    get_content(url,index);
    $("#lastl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>')
    x.scrollTop=0;
    i=0;
    next_page(i);
};

function save_progress(){
    $.post('https://read.xieaofan.top/reader3/saveBookProgress',
        {
            'name':bookname,
            'index':index,
        },
        function(data, s){
            console.log(data)
        }
    )
}

function next_page(mi){
    let width = x.clientWidth
    imax = Math.ceil(article.scrollWidth/(article.clientWidth+60))
    if(mi > imax-1){
        i = 0;
        next_chapter();
        mi = i;
    }
    if(mi < 0){
        i=0;
        last_chapter();
        mi = i;
    }
    article.style.transform = `translateX(-${(width+60) * mi}px)`
}

$("#lastl").hide();
$("#nextl").hide();
get_content(url,index);
let i = 0;

article = document.querySelector('article');
$(document).keydown(function(event){
    if(event.keyCode==39){
        i++;
        next_page(i)
    }
    if(event.keyCode==37){
        i--;
        next_page(i);
    }
    if(event.keyCode==38){
        next_chapter()
    }
    if(event.keyCode==40){
        last_chapter()
    }
});
window.onbeforeunload=save_progress;
$.get("https://read.xieaofan.top/reader3/getChapterList",{'url':url},function(redata,status){
        content = redata['data'];
        $('#title').empty();
        $('#title').append('<h3>'+content[index]['title']+'</h3>')
      });
