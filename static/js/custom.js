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


window.onscroll = function() {scrollFunction()};

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

$('#warning-sp2-tab').click(ajaxPage("/warning/questionnaire_list", '#warning-sp2'));


$(document).on('click', '.warning-sp2-page', function () {
    ajaxPage("/warning/questionnaire_list?page="+$(this).attr('aria-label'), '#warning-sp2');
});


// When the user clicks on the button, scroll to the top of the document
$('#backToTopBtn').click(function(){
    $('html,body').animate({scrollTop:0},'fast');return false;
});


$(document).ready(function () {
    resizeSidebar();
});