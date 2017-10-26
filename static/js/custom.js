function ajaxData(url, element) {
    $.get(url, function (data) {
        $(element).html(data);
    })
}
// $(function () {
//     $('[data-toggle="popover"]').popover()
// });

$(".superPopover").popover({ trigger: "manual" , html: true, animation:false})
.on("mouseenter", function () {
    var _this = this;
    setTimeout(function () {
        if ($(".superPopover:hover").length) {
            $(_this).popover("show");
        }
    }, 300);
    $(".popover").on("mouseleave", function () {
        $(_this).popover('hide');
    });
}).on("mouseleave", function () {
    var _this = this;
    setTimeout(function () {
        if (!$(".popover:hover").length) {
            $(_this).popover("hide");
        }
    }, 200);
});

$(".warning_popAjax").click(
    function () {
        var pop = $(this);
        var type = pop.attr("q_type");
        var category = pop.attr("q_category");
        var keyword = pop.attr("data-title");
        var url = "/warning/detail/?type="+type+"&category="+category+"&keyword="+keyword;
        $.get(url, function (data) {
            pop.attr("data-content",(data));
            pop.popover('show')
        })
    }
);

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("backToTopBtn").style.display = "block";
    } else {
        document.getElementById("backToTopBtn").style.display = "none";
    }
}

function resizeSidebar() {
    var h = $(window).height();
    $("#sidebar,.list-group").css("height", h-140); //加了个逗号
}

$(window).resize(function(){
    resizeSidebar();
});

function ajaxPage(url, element) {
    $.get(url, function (data) {
        $(element).html(data);
    })
}

$(document).on('click', 'warning-tab2-page', function () {
    ajaxPage("/warning/questionnaire_list?page="+$(this).attr('aria-label'), '#warning-tab2');
});

$(document).on('click', 'a[class^=js_creative_page]', function (event) {
    var tab = $(event.target).parents("div[class^=tab-pane]");
    ajaxPage("/creative/"+tab.attr("data-url")+"?page="+$(this).attr('aria-label'), '#'+tab.attr("id"));
});

// When the user clicks on the button, scroll to the top of the document
$('#backToTopBtn').click(function(){
    $('html,body').animate({scrollTop:0},'fast');return false;
});

$(document).on('click', '.js_post_modal', function () {
    var pid = $(this).attr("data-pid");
    var name = $(this).attr("data-name");
    var type = $(this).attr("data-type");
    var fid = $(this).attr("data-fid");

    var url = "/creative/detail/?type="+type+"&&pid="+pid+"&&fid="+fid;
    $.get(url, function (data) {
        $(".modal-title").html(name);
        $(".modal-body").html(data);
        $('#PostModal').modal("show");
    });
});

window.onscroll = function() {scrollFunction()};
$('#PostModal').on('hidden.bs.modal', function () {
   $('#player')[0].pause();

});

$(document).ready(function () {
    resizeSidebar();
    var questionnaire_list = $('#warning-tab-2');
    if (questionnaire_list.length > 0) {
        ajaxPage("/warning/questionnaire_list", '#warning-tab-2');
    }
    var creative_list = $('#creative_tab_1');
    if (creative_list.length > 0) {
        ajaxPage("/creative/design/", '#creative_tab_1');
        ajaxPage("/creative/templates/", '#creative_tab_2');
        ajaxPage("/creative/method/", '#creative_tab_3');

    }
});

