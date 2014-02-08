function addPostModal() {
        var form = 
                '<div class="row text-center demo-row">' +
                '<form method="POST" action="" class="question" id="new-post">' +
                '<select class="form-control" name="topic">' +
                '<option value="one">One</option>' +
                '<option value="two">Two</option>' +
                '<option value="three">Three</option>' +
                '<option value="four">Four</option>' +
                '<option value="five">Five</option>' +
                '</select>' +
                '<input type="text" class="form-control" placeholder="Paste title" name="paste_title">' +
                '<input type="text" class="form-control" placeholder="Link" name="link">' +
                '<input type="text" class="form-control" placeholder="Link title" name="link_title">' +
                '<span class="add-row">' +
                '<a href="javascript:addLinkRow()" class="btn btn-block btn-primary" style="clear: both; width: 10%; margin-left: 5%; float: left;"><span class="glyphicon fui-plus"></span></a>' +
                '<input type="submit" action="post_add" name="submit" value="Add Paste" class="form-control btn btn-primary btn-lg btn-block">' +
                '</span>' +
                '</form>' +
                '</div>' +
                '</div>';

                BootstrapDialog.show({message: form});
}

function addLinkRow() {
        var temp = '<span class="add-row">' + $('.add-row').html() + '</span>';
        $('.add-row').remove();
        var inp = '<input type="text" class="form-control" placeholder="Link" name="link"> <input type="text" class="form-control" placeholder="Link title" name="link_title">';
        $('#new-post').append(inp + temp);
}
