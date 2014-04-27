/**
 * Created by leppin on 22.04.14.
 * License: GPL 3  2014
 */
// Treeview Function
$(function () {
    $('.tree li:has(ul)').addClass('parent_li').find(' > span').attr('title', 'Collapse this branch');
    $('.tree li.parent_li > span').on('click', function (e) {
        var children = $(this).parent('li.parent_li').find(' > ul > li');
        if (children.is(":visible")) {
            children.hide('fast');
            $(this).attr('title', 'Expand this branch').find('span').addClass('glyphicon-plus-sign').removeClass('glyphicon-minus-sign');
        } else {
            children.show('fast');
            $(this).attr('title', 'Collapse this branch').find('span').addClass('glyphicon-minus-sign').removeClass('glyphicon-plus-sign');
        }
        e.stopPropagation();
    });
});

// load Content from contenturl to place as html inline a divtag
function loadcontent(contenturl, divtag) {
    $.get( contenturl, function( data ) {
        $( divtag ).html(data);
    })
    .fail(function (){
            alert("Error: JS: immotask.js - Function: loadcontent")
        })
    };

// toggle hide / show vor div
function togglehidden(divtag) {
    if ( $(divtag).is(':visible')){
       $(divtag).hide()
    } else {
       $(divtag).show()
    };
}

