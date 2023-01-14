data = '';
content = [];
function get_content(url,index){
    $.get("https://read.xieaofan.top/reader3/getBookContent",{'url':url,'index':index},function(redata,status){
        data = redata['data'];
        data = data.split('\n');
        $('.content').empty();
        for(var i=0,len=data.length; i<len; i++){var n = '<p>'+data[i]+'</p>';$('#content').append(n);};
      });
      window.history.pushState({}, 0, window.location.href.split('&id=')[0] + '&id=' + index);
    
};

function next(){
    $("#nextl").show();
    index++;
    get_content(url,index);
    $("#nextl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>')
};

function last(){
    $("#lastl").show();
    index--;
    get_content(url,index);
    $("#lastl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>')
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
});
window.onbeforeunload=save_progress;
$.get("https://read.xieaofan.top/reader3/getChapterList",{'url':url},function(redata,status){
        content = redata['data'];
        $('#title').empty();
        $('#title').append('<h3>'+content[index]['title']+'</h3>')
      });
