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
        $('.content').empty();
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
        $('.content').empty();
        for(var i=0,len=data.length; i<len; i++){
            data[i] = data[i].replace(/^\s+|\s+$/g,'');
            if(data[i]!=''){
                var n = '<p>'+data[i]+'</p>';
                $('#content').append(n);};
            }
    
};

function next(){
    $("#nextl").show();
    index++;
    get_content(url,index);
    $("#nextl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>')
    x.scrollTop=0;
};

function last(){
    $("#lastl").show();
    index--;
    get_content(url,index);
    $("#lastl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>')
    x.scrollTop=0;
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


$("#lastl").hide();
$("#nextl").hide();
get_content(url,index);
$(document).keydown(function(event){
    if(event.keyCode==39){next()}
    if(event.keyCode==37){last()}
    if(event.keyCode==38){
        x.scrollTop-=(x.clientHeight)
    }
    if(event.keyCode==40){
        x.scrollTop+=(x.clientHeight)
    }
});
window.onbeforeunload=save_progress;
$.get("https://read.xieaofan.top/reader3/getChapterList",{'url':url},function(redata,status){
        content = redata['data'];
        $('#title').empty();
        $('#title').append('<h3>'+content[index]['title']+'</h3>')
      });
