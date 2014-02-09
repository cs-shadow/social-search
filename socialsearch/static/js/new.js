function addPostModal() {
        var form = 
                '<div class="row text-center demo-row">' +
                '<form method="POST" action="post_add" class="question" id="new-post">' +
                '<select class="form-control" name="topic">' +
                '<option value="1">Topic1</option>' +
                '<option value="two">Two</option>' +
                '<option value="three">Three</option>' +
                '<option value="four">Four</option>' +
                '<option value="five">Five</option>' +
                '</select>' +
                '<input type="text" class="form-control" placeholder="Paste title" name="paste_title">' +
                '<input type="text" class="form-control" placeholder="Link" name="URL">' +
                '<input type="text" class="form-control" placeholder="Link title" name="title">' +
                '<span class="add-row">' +
                '<a href="javascript:addLinkRow()" class="btn btn-block btn-primary" style="clear: both; width: 10%; margin-left: 5%; float: left;"><span class="glyphicon fui-plus"></span></a>' +
                '<input type="submit" name="submit" value="Add Paste" class="form-control btn btn-primary btn-lg btn-block">' +
                '</span>' +
                '</form>' +
                '</div>' +
                '</div>';

                BootstrapDialog.show({message: form});
}

function addLinkRow() {
        var temp = '<span class="add-row">' + $('.add-row').html() + '</span>';
        $('.add-row').remove();
        var inp = '<input type="text" class="form-control" placeholder="Link" name="URL"> <input type="text" class="form-control" placeholder="Link title" name="title">';
        $('#new-post').append(inp + temp);
}

function addPostRows() {
        var html = 
                '<div class="row text-center demo-row">' +
                '  <div class="col-xs-3">' +
                '    <img src="http://placehold.it/150x150" style="width:75px;">' +
                '  </div>' +
                '  <div class="col-xs-9" style="postion:absolute;height:75px;">    ' +
                '    <p id="topic-content" style="text-align:left">' +
                '    lorem ipsem;<br />' +
                '    </p>' +
                '    <div style="text-align:left">' +
                '      <a href="#">Check it out</a>   ' +
                '    </div>' +
                '    <div style="text-align:left" class="vote-post">' +
                '      <a href="post_like/1"><i class="icon-large icon-thumbs-up"></i>Upvote</a> ' +
                '      <a href="post_dislike/1"><i class="icon-large icon-thumbs-down"></i>Downvote</a>   ' +
                '    </div>' +
                '  </div>' +
                '</div>' +
                '<hr />';

        $('#post-body').append(html);
}
