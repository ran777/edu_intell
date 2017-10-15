$(function () {
    $('[data-toggle="popover"]').popover()
})

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


function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("backToTopBtn").style.display = "block";
    } else {
        document.getElementById("backToTopBtn").style.display = "none";
    }
};

$(document).ready(function(){
resizeSidebar();
});
window.onscroll = function() {scrollFunction()};

function resizeSidebar() {
    var h = $(window).height();
    $("#sidebar .list-group").css("height", h-140);
};

$(window).resize(function(){
    resizeSidebar();
});


// When the user clicks on the button, scroll to the top of the document
$('#backToTopBtn').click(function(){
    $('html,body').animate({scrollTop:0},'fast');return false;
});
