
$('.menu-btn').on('click', function(){
    $(this).toggleClass('menu-btn_active');
    $('.hiden-menu').toggleClass('hiden-menu_active');
    $('.opened-menu').toggleClass('opened-menu_active');
    $('.content-slide').toggleClass('content-slide_active');
    
})


$(window).scroll(function(){
    if ($(this).scrollTop() > 140 ) {
        $('#masthead').css({
            "background-color": "rgba(0,0,0,0.6)",
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "z-index": "99"
        })
        $('.menu-btn').css({
            "background-color": "rgba(0,0,0,0)",
        });
    }
    else if (($(this).scrollTop() < 140)  ) {
        $('#masthead').css({
            "background-color": "",
            "position": "",
            "width": "100%"
        });
    }
})

