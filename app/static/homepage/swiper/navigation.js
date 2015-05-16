window.onload = function () {
    var mySwiper = new Swiper('.swiper-container', {
        //Your options here:
        mode: 'horizontal',
        loop: false,
        initialSlide: 1,
        onTouchStart: function () {
            var contactContent = document.getElementById("contactContent");
            var mainContent = document.getElementById("mainContent");
            var aboutUsContent = document.getElementById("aboutUsContent");

            contactContent.style["border"] = "border: 1px solid #ffffff";
            mainContent.style["border"] = "border: 1px solid #ffffff";
            aboutUsContent.style["border"] = "border: 1px solid #ffffff";
            contactContent.style["-webkit-box-shadow"] = "inset 0 0 130px #ffffff";
            mainContent.style["-webkit-box-shadow"] = "inset 0 0 130px #ffffff";
            aboutUsContent.style["-webkit-box-shadow"] = "inset 0 0 130px #ffffff";
            contactContent.style["-moz-box-shadow"] = "inset 0 0 130px #ffffff";
            mainContent.style["-moz-box-shadow"] = "inset 0 0 130px #ffffff";
            aboutUsContent.style["-moz-box-shadow"] = "inset 0 0 130px #ffffff";
            contactContent.style["box-shadow"] = "inset 0 0 130px #ffffff";
            mainContent.style["box-shadow"] = "inset 0 0 130px #ffffff";
            aboutUsContent.style["box-shadow"] = "inset 0 0 130px #ffffff";
        },
        onTouchEnd: function () {
            var contactContent = document.getElementById("contactContent");
            var mainContent = document.getElementById("mainContent");
            var aboutUsContent = document.getElementById("aboutUsContent");

            contactContent.style["border"] = "border: 0";
            mainContent.style["border"] = "border: 0";
            aboutUsContent.style["border"] = "border: 0";
            contactContent.style["-webkit-box-shadow"] = "inset 0 0 0px #ffffff";
            mainContent.style["-webkit-box-shadow"] = "inset 0 0 0px #ffffff";
            aboutUsContent.style["-webkit-box-shadow"] = "inset 0 0 0px #ffffff";
            contactContent.style["-moz-box-shadow"] = "inset 0 0 0px #ffffff";
            mainContent.style["-moz-box-shadow"] = "inset 0 0 0px #ffffff";
            aboutUsContent.style["-moz-box-shadow"] = "inset 0 0 0px #ffffff";
            contactContent.style["box-shadow"] = "inset 0 0 0px #ffffff";
            mainContent.style["box-shadow"] = "inset 0 0 0px #ffffff";
            aboutUsContent.style["box-shadow"] = "inset 0 0 0px #ffffff";
        }
    });

    var contactButton = document.getElementById("contactButton");
    contactButton.addEventListener("click", function() {
        mySwiper.swipeTo(0, 1000, true);
    }, true);

    var aboutUsButton = document.getElementById("aboutUsButton");
    aboutUsButton.addEventListener("click", function() {
        mySwiper.swipeTo(2, 1000, true);
    }, true);

    var homeInContactButton = document.getElementById("homeInContactButton");
    homeInContactButton.addEventListener("click", function() {
        mySwiper.swipeTo(1, 1000, true);
    }, true);

    var homeInAboutUsButton = document.getElementById("homeInAboutUsButton");
    homeInAboutUsButton.addEventListener("click", function() {
        mySwiper.swipeTo(1, 1000, true);
    }, true);
};