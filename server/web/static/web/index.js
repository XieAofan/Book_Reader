function creat_book_div(name,url,img,isnew,id){
    if(img==undefined){
        img = no_cover_url
    };
    var nl = '';
    if(isnew){
        nl=`
        <img class = 'new' id="book${id}" src="static/web/icon/new.svg">
        `;
    };
    
    var node = `
    <div class="col-*-* book">
                <a href="${url}">
                    <img src="${img}" onerror="javascript:this.src='/static/web/failed.jpg';this.onerror=null;">
                    ${nl}
                    <span>
                        <h5 class='text-center'>${name}</h5>
                    </span>
                </a>
            </div>
    `;
    return node;
}

function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
      for (let j = 0; j < arr.length - i - 1; j++) {
        if (arr[j]['durChapterTime'] < arr[j + 1]['durChapterTime']) {
          ;[arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]
        }
      }
    }
    return arr
  }

function init(){
    var url;
    data = 'start'
    $.get("https://r.xieaofan.top/reader3/getBookshelf",function(re_data,status){
        data = re_data['data']
        $('#loading').hide()
        $('#loading-last').hide()
        data = bubbleSort(data)
        for (var i=0,len=3; i<len; i++)
        { 
            var isnew = true;
            var r = data[i];
            
            if(r['durChapterTime']>=r['latestChapterTime']){isnew=false};
            $("#booklast").append(creat_book_div(r['name'],r['bookUrl'],r['coverUrl'],isnew,i));
        }

        for (var i=0,len=data.length; i<len; i++)
        {
            var isnew = true;
            var r = data[i];
            if(r['durChapterTime']>=r['latestChapterTime']){isnew=false};
            $("#booksheft").append(creat_book_div(r['name'],r['bookUrl'],r['coverUrl'],isnew,i));
        }
      });
}

function onKeyDown(event){
    var e = event || window.event || arguments.callee.caller.arguments[0];
    if(e && e.keyCode==27){ // 按 Esc
        //要做的事情
    }
    if(e && e.keyCode==113){ // 按 F2
        //要做的事情
    }
    if(e && e.keyCode==13){ // enter 键
        alert("此处回车触发搜索事件");
    }
}


init()