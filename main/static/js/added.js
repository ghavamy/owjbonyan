$(document).ready(function () {
    // Highlight active nav link
    $(".nav-link").each(function () {
        if (this.href === window.location.href) {
            $(this).addClass("active").attr("aria-current", "page");
        }
    });

    // Dropdown hover behavior
    var $dropdown = $(".nav-item.dropdown");
    if ($dropdown.length) {
        $dropdown.hover(
            function () {
                $(this).addClass("show");
                $(this).find(".dropdown-menu").addClass("show");
            },
            function () {
                $(this).removeClass("show");
                $(this).find(".dropdown-menu").removeClass("show");
            }
        );
    }

    // Side nav toggling
    var $sideNav = $("#mobileNav");
    var $toggler = $(".navbar-toggler");

    $toggler.on("click", function () {
        $sideNav.toggleClass("open");
    });

    $("#closeNav").on("click", function () {
        $sideNav.removeClass("open");
    });

    $(document).on("click", function (e) {
        if (
            $sideNav.hasClass("open") &&
            !$sideNav.is(e.target) &&
            $sideNav.has(e.target).length === 0 &&
            !$toggler.is(e.target) &&
            $toggler.has(e.target).length === 0
        ) {
            $sideNav.removeClass("open");
        }
    });
});