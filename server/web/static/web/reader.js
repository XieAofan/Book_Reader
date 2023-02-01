data = '';
x = document.getElementById("f");
content = [];
contents = {};
nr = '';
front_url = '/api';
li = 0;
r = '';
function fresh_content(vi) {
    mydata = contents[String(vi)]
    if (typeof mydata != 'undefined') {
        mydata = re(mydata)
        mydata = mydata.split('\n');
        $('#content').empty();
        for (var i = 0, len = mydata.length; i < len; i++) {
            data[i] = data[i].replace(/^\s+|\s+$/g, '');
            if (mydata[i] != '') {
                var n = '<p>' + mydata[i] + '</p>';
                $('#content').append(n);
            };
        }
        $('#title').empty();
        $('#title').append('<h3>' + content[vi]['title'] + '</h3>');
        i = 0;
        next_page(i);
        window.history.pushState({}, 0, window.location.href.split('&myid=')[0] + '&myid=' + index);
    }
    else {
        $.get(front_url + "/getBookContent", { 'book_id': url, 'index': vi }, function (redata, status) {
            data = redata['data'];
            vi = redata['i'];
            contents[String(vi)] = data;
            fresh_content(vi)
        });
        $.get(front_url + "/getBookContent", { 'book_id': url, 'index': vi + 1 }, function (redata, status) {
            data = redata['data'];
            vi = redata['i'];
            contents[String(vi)] = data;
            fresh_content(vi)
        });
        $('#content').empty();
        $('#content').append('<div class="spinner-border text-muted" style="position:absolute;left:50%;top:45%;"></div>')
        alert('Please Wait!')
    }
}
function get_content(url, index) {
    r = nr;
    if (r == '') {
        $.get(front_url + "/getBookContent", { 'book_id': url, 'index': index }, function (redata, status) {
            data = redata['data'];
            i = redata['i'];
            contents[String(i)] = data;
            data = re(data);
            mydata = data.split('\n');
            $('#content').empty();
            for (var i = 0, len = mydata.length; i < len; i++) {
                data[i] = data[i].replace(/^\s+|\s+$/g, '');
                if (mydata[i] != '') {
                    var n = '<p>' + mydata[i] + '</p>';
                    $('#content').append(n);
                };
            }

        });
    }
    else {
        $('#title').empty();
        $('#title').append('<h3>' + content[index]['title'] + '</h3>');
        fresh_content(index);
    }
    $.get(front_url + "/getBookContent", { 'book_id': url, 'index': index + 1 }, function (redata, status) {
        data = redata['data'];
        nr = data;
        i = redata['i'];
        contents[String(i)] = data;
    });
};

function next_chapter() {
    $("#nextl").show();
    index++;
    get_content(url, index);
    $("#nextl").hide();
    i = 0;
    next_page(i);
};

function to_chapter(i) {
    $('#content').empty();
    $('#content').append('<div class="spinner-border text-muted" style="position:absolute;left:50%;top:45%;"></div>')
    //$("#nextl").show();
    index = i;
    $.get(front_url + "/getBookContent", { 'book_id': url, 'index': index }, function (redata, status) {
        data = redata['data'];
        data = data.split('\n');
        $('#content').empty();
        for (var i = 0, len = data.length; i < len; i++) {
            data[i] = data[i].replace(/^\s+|\s+$/g, '');
            if (data[i] != '') {
                var n = '<p>' + data[i] + '</p>';
                $('#content').append(n);
            };
        }
    });
    r = '';
    //$("#nextl").hide();
    window.history.pushState({}, 0, window.location.href.split('&myid=')[0] + '&myid=' + index);
    $('#title').empty();
    $('#title').append('<h3>' + content[index]['title'] + '</h3>');
    i = 0;
    next_page(i);
    $('#myModal').modal('hide');
    save_progress()
};

function last_chapter() {
    $("#lastl").show();
    index--;
    get_content(url, index);
    $("#lastl").hide();
    //$('#title').empty();
    //$('#title').append('<h3>' + content[index]['title'] + '</h3>')
    x.scrollTop = 0;
    i = 0;
    next_page(i);
};

function save_progress() {
    $.post(front_url + '/saveBookProgress',
        {
            'book_id': url,
            'index': index,
            'title': content[index]['title']
        },
        function (data, s) {
            console.log(data)
        }
    )
}

function next_page(mi) {
    let width = x.clientWidth
    imax = Math.ceil(article.scrollWidth / (article.clientWidth + 60))
    if (mi > imax - 1) {
        pi = 0;
        console.log(mi)
        next_chapter();
        mi = pi;
    }
    if (mi < 0) {
        pi = 0;
        last_chapter();
        mi = pi;
    }
    console.log(mi-li)
    if (Math.abs(mi - li) > 1) {
        article.style.transition = '0s';
        //console.log(mi-li);
    }
    article.style.transform = `translateX(-${(width + 60) * mi}px)`
    setTimeout(function () {
        article.style.transition = '.4s';
    }, 400)
    li = mi
}
$("#lastl").hide();
$("#nextl").hide();
get_content(url, index);
pi = 0;

article = document.querySelector('article');
$(document).keydown(function (event) {
    if (event.keyCode == 39) {
        pi++;
        next_page(pi)
    }
    if (event.keyCode == 37) {
        pi--;
        next_page(pi);
    }
    if (event.keyCode == 38) {
        last_chapter();
    }
    if (event.keyCode == 40) {
        next_chapter();
    }
});
window.onbeforeunload = save_progress;
function fresh(isfresh = 0) {
    var s = $('#cd').scrollTop()
    //alert(s)
    $('#cf').show()

    $.get(front_url + "/getChapterList", { 'book_id': url, 'isfresh': isfresh }, function (redata, status) {
        content = redata['data'];
        $('#title').empty();
        $('#title').append('<h3>' + content[index]['title'] + '</h3>');
        $('#contents').empty()
        for (var i = 0, len = content.length; i < len; i++) {
            var nr = `
                <li class="list-group-item contentli" onclick='to_chapter(${i});'>${content[i]['title']}</li>
                `;
            if (i == index - 2) {
                var nr = `
                    <li class="list-group-item contentli" id='cll' onclick='to_chapter(${i});'>${content[i]['title']}</li>
                    `;
            }
            if (i == index) {
                var nr = `
                    <li class="list-group-item contentli onread" style="background-color: #e7e7e7;" id='clz' onclick='to_chapter(${i});'>${content[i]['title']} - 正在阅读</li>
                    `;
            }
            $('#contents').append(nr)
        }
        $('#cf').hide()
        if (s == null) {
            //scroll();
            s = 0;
        }
        else {
            console.log(s)
            $('#cd').scrollTop(s);
        }

    });
}
function scroll() {
    var element = document.querySelector("#cll")
    element.scrollIntoView();
};
fresh(0);