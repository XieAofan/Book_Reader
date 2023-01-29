data = '';
x = document.getElementById("f");
content = [];
nr = '';
front_url = '/api';
function get_content(url,index){
    r = nr;
    if(r==''){
        $.get(front_url+"/getBookContent",{'book_id':url,'index':index},function(redata,status){
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
    
    $.get(front_url+"/getBookContent",{'book_id':url,'index':index+1},function(redata,status){
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

function to_chapter(i){
    $("#nextl").show();
    index=i;
    get_content(url,index);
    $("#nextl").hide();
    $('#title').empty();
    $('#title').append('<h3>'+content[index]['title']+'</h3>');
    i=0;
    next_page(i);
    $('#myModal').modal('hide');
    save_progress()
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
    $.post(front_url+'/saveBookProgress',
        {
            'book_id':url,
            'index':index,
            'title':content[index]['title']
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
function fresh(isfresh=0){
    var s = $('#cd').scrollTop()
    //alert(s)
    $('#cf').show()
    $('#contents').empty()
    $.get(front_url+"/getChapterList",{'book_id':url,'isfresh':isfresh},function(redata,status){
            content = redata['data'];
            $('#title').empty();
            $('#title').append('<h3>'+content[index]['title']+'</h3>');
            for(var i=0,len=content.length; i<len; i++){
                var nr = `
                <li class="list-group-item contentli" onclick='to_chapter(${i});'>${content[i]['title']}</li>
                `;
                if(i==index-2){
                    var nr = `
                    <li class="list-group-item contentli" id='cll' onclick='to_chapter(${i});'>${content[i]['title']}</li>
                    `;
                }
                if(i==index){
                    var nr = `
                    <li class="list-group-item contentli onread" style="background-color: #e7e7e7;" id='clz' onclick='to_chapter(${i});'>${content[i]['title']} - 正在阅读</li>
                    `;
                }
                $('#contents').append(nr)
            }
            $('#cf').hide()
            if(s==null){
                scroll()
            }
            else{
                $('#cd').scrollTop(s)
            }
            
        });
    }
function scroll(){
    var element = document.querySelector("#cll")
    element.scrollIntoView();
};
fresh(0);