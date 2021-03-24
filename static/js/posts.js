function new_post() {
    $(location).attr('href','/board/create');
}

function new_post1() {
    $(location).attr('href','/board/create2');
}

function new_post2() {
    $(location).attr('href','/board/create3');
}




function to_list() {
    $(location).attr('href','/board/list');
}


function to_list1() {
    $(location).attr('href','/board/list2');
}


function to_list2() {
    $(location).attr('href','/board/list3');
}





function delete_post(post_id) {
    let result = confirm('정말 삭제할까요?')
    if(result) {
        $(location).attr('href','/board/delete/' + post_id);
    }
}

function delete_post1(post_id) {
    let result = confirm('정말 삭제할까요?')
    if(result) {
        $(location).attr('href','/board/delete2/' + post_id);
    }
}

function delete_post2(post_id) {
    let result = confirm('정말 삭제할까요?')
    if(result) {
        $(location).attr('href','/board/delete3/' + post_id);
    }
}




function update_post(post_id) {
        $(location).attr('href','/board/update/' + post_id);
}


function update_post1(post_id) {
        $(location).attr('href','/board/update2/' + post_id);
}


function update_post2(post_id) {
        $(location).attr('href','/board/update3/' + post_id);
}