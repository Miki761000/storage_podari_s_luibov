// $(function () {
//     select_view();
//
//     $('#list-view').on('click', function () {
//         list_view();
//     });
//
//     $('#grid-view').on('click', function () {
//         grid_view();
//     });
//
//     $('#compact-view').on('click', function () {
//         compact_view();
//     });
//
//     max_height_div('.home_banner');
//     max_height_div('.category_list p');
//
//     $(document).on('keydown', '#collapse-checkout-option input[name=\'email\'], #collapse-checkout-option input[name=\'password\']', function (e) {
//         if (e.keyCode == 13) {
//             $('#collapse-checkout-option #button-login').trigger('click');
//         }
//     });
//
//     $(window).scroll(function () {
//         if ($(this).scrollTop() > 190) {
//             $('.scroll_up').addClass('show');
//         } else {
//             $('.scroll_up').removeClass('show');
//         }
//     });
//
//     $('header .dropdown-menu').mouseover(function () {
//         $(this).attr('style', 'display:block');
//     }).mouseout(function () {
//         $(this).removeAttr('style');
//     });
//
//     if ($(window).width() < 767) {
//         $('#menu li').removeClass('open');
//         $('#grid-view').trigger('click');
//         m_filter();
//     }
//
//     $(window).resize(function () {
//         m_filter();
//     });
//
//     $('#menu span.visible-xs').on('click', function () {
//         $(this).parent().toggleClass('open');
//         $(this).next().toggleClass('open');
//     });
//
//     if ($(window).width() > 768) {
//         $('[data-toggle=\'tooltip\']').tooltip({container: 'body', trigger: 'hover'});
//         $(document).ajaxStop(function () {
//             $('[data-toggle=\'tooltip\']').tooltip({container: 'body', trigger: 'hover'});
//         });
//     }
//
//     $('.add_to_cart.disabled').each(function () {
//         $(this).attr('disabled', true);
//     });
//
//     $(document).ajaxStop(function () {
//         if ($('#column-left #filterpro_box').length || $('#column-left .mfilter-box').length) {
//             select_view();
//             add_additional_img();
//         }
//     });
//
//     $('.text-danger').each(function () {
//         var element = $(this).parent().parent();
//
//         if (element.hasClass('form-group')) {
//             element.addClass('has-error');
//         }
//     });
//
//     $('#language li a').on('click', function (e) {
//         e.preventDefault();
//         $('#language input[name=\'code\']').attr('value', $(this).attr('data-code'));
//         $('#language').submit();
//     });
//
//     $('#currency li a').on('click', function (e) {
//         e.preventDefault();
//         $('#currency input[name=\'code\']').attr('value', $(this).attr('data-code'));
//         $('#currency').submit();
//     });
//
//     $('body').on('click', '#search ul li', function () {
//         $('#search .cat_id button span').text($(this).text());
//         $('#search input[name=\'filter_category_id\']').val($(this).attr('data-id'));
//     });
//
//     $('body').on('click', '.search', function () {
//         url = $('base').attr('href') + 'index.php?route=product/search';
//         var value = $(this).parent().parent().find('input[name=\'search\']').val();
//         if (value) {
//             url += '&search=' + encodeURIComponent(value);
//         }
//         var filter_category_id = $(this).parent().parent().find('input[name=\'filter_category_id\']').val();
//         if (filter_category_id > 0) {
//             url += '&category_id=' + encodeURIComponent(filter_category_id);
//         }
//         location = url;
//     });
//
//     $('body').on('keydown', '#search input[name=\'search\']', function (e) {
//         if (e.keyCode == 13) {
//             $(this).parent().find('button.search').trigger('click');
//         }
//     });
//
//     $('body').on('input', 'div input[name=\'search\']', function (e) {
//         if ($('div input[name=\'search\']').not($(this))) {
//             $('div input[name=\'search\']').val($(this).val());
//         }
//     });
//
//     $('#search_phrase a').on('click', function () {
//         $(this).parent().prev().find('.form-control.input-lg').val($(this).text());
//         $(this).parent().prev().find('.search').trigger('click');
//     });
//
//     $('.nav-tabs li a').on('shown.bs.tab', function (e) {
//         block_arr();
//     });
//
//     $(window).resize(function () {
//         setTimeout(function () {
//             block_arr();
//         }, 200);
//     });
//
//     top_menu();
//     add_additional_img();
//     fly_menu_enabled = 0;
// });
//
// function list_view() {
//     $('#content .product-grid > .clearfix').remove();
//     $('#content .product-grid, #content .product-price').attr('class', 'product-layout product-list col-xs-12');
//     localStorage.setItem('display', 'list');
// }
//
// function grid_view() {
//     cols = $('#column-right, #column-left').length;
//     menu = $('.breadcrumb.col-md-offset-4.col-lg-offset-3').length;
//
//     if (cols == 2) {
//         $('.product-grid, .product-list, .product-price').attr('class', 'product-layout product-grid col-lg-6 col-md-6 col-sm-12 col-xs-12');
//     } else if (cols == 1 || menu == 1) {
//         $('.product-grid, .product-list, .product-price').attr('class', 'product-layout product-grid col-lg-4 col-md-6 col-sm-6 col-xs-12');
//     } else {
//         $('.product-grid, .product-list, .product-price').attr('class', 'product-layout product-grid col-lg-3 col-md-4 col-sm-4 col-xs-12');
//     }
//
//     $product = $('.product-grid .product-thumb');
//
//     max_height_div($product.find('.caption > a'));
//     max_height_div($product.find('.attribute, .description'));
//     max_height_div($product.find('.option'));
//
//     localStorage.setItem('display', 'grid');
// }
//
// function compact_view() {
//     $('#content .row > .product-list, #content .row > .product-grid').attr('class', 'product-layout product-price col-xs-12');
//     if (!$('.product-price .product-thumb div .caption').length) {
//         $('.product-price .caption').wrap('<div></div>');
//     }
//     localStorage.setItem('display', 'compact');
// }
//
// function select_view() {
//     if (localStorage.getItem('display') == 'list') {
//         list_view();
//     } else if (localStorage.getItem('display') == 'compact') {
//         compact_view();
//     } else {
//         grid_view();
//     }
// }
//
// var new_id = [];
//
// function module_type_view(type, id, items) {
//     var items = typeof (items) != 'undefined' ? items : [[0, 1], [580, 2], [720, 3], [1050, 4]],
//         columns = ($('#column-left ' + id).length || $('#column-right ' + id).length);
//
//     if (new_id.join().search(id) == -1) {
//         new_id.push({'name': id, 'type': type});
//     }
//
//     block_resize = function (id, type) {
//
//         var div_arr = [id + ' .caption > a', id + ' .name', id + ' .attribute, ' + id + ' .description', id + ' .option'];
//
//         if ($(id).parent().parent().parent().hasClass('tab-content')) {
//             var width = $(id).parent().parent().parent().width() + 20;
//         } else {
//             var width = $(id).width();
//         }
//
//         width = Math.floor(parseFloat(width))
//
//         if (type == 'grid' && !columns) {
//             for (i = 0; i < items.length; i += 1) {
//                 if (items[i][0] <= width) {
//                     itemsNEW = parseFloat(items[i][1]);
//                 }
//             }
//             $(id).find('.product-layout-1').attr('style', 'float:left;width:' + (Math.floor(width / itemsNEW) - 0.2) + 'px;padding:0 10px');
//         } else {
//             $(id).owlCarousel({
//                 responsiveBaseWidth: id,
//                 itemsCustom: items,
//                 autoPlay: false,
//                 mouseDrag: false,
//                 navigation: true,
//                 navigationText: ['<i class="fa fa-chevron-left"></i>', '<i class="fa fa-chevron-right"></i>'],
//                 pagination: false,
//                 afterUpdate: function () {
//
//                 }
//             });
//         }
//
//         for (i in div_arr) {
//             var maxheight = 0;
//
//             $(div_arr[i]).height('auto');
//
//             $.each($(div_arr[i]), function () {
//                 if ($(this).height() > maxheight) {
//                     maxheight = $(this).height();
//                 }
//             });
//
//             $(div_arr[i]).height(maxheight);
//         }
//     }
//
//     block_resize(id, type);
// }
//
// function block_arr() {
//     for (i in new_id) {
//         block_resize(new_id[i]['name'], new_id[i]['type']);
//     }
// }
//
// function max_height_div(div) {
//     block_height = function () {
//         var maxheight = 0;
//
//         if ($(div).length) {
//             $(div).each(function () {
//                 if ($(this).height() > maxheight) {
//                     maxheight = $(this).height();
//                 }
//             });
//             $(div).height(maxheight);
//         }
//     }
//
//     block_height();
//     $(window).resize(function () {
//         setTimeout(function () {
//             block_height();
//         }, 200);
//     });
// }
//
// function top_menu() {
//     menu = function () {
//         if (!$('#top-links2 ul').length && $(window).width() < 992) {
//             $('#top-links ul').clone().appendTo('#top-links2');
//             $('#top-links2 ul').addClass('dropdown-menu dropdown-menu-left');
//         }
//     }
//
//     menu();
//     $(window).resize(menu);
// }
//
// function fly_menu(fly_menu_product) {
//
//     fly_menu_enabled = 1;
//
//     menu = function () {
//         product = '';
//         price = '';
//         button = '';
//         menu = '';
//         search = '';
//
//         if (!$('#menu_wrap').length && $(window).width() > 992) {
//             if (fly_menu_product && $('#product').length) {
//                 var button = '<button type="button" class="' + $('#product #button-cart').attr('class') + '">' + $('#product #button-cart').html() + '</button>';
//                 var product = '<div class="product_wrap col-md-8 col-lg-8"><div><div class="product_name">' + $('#product h1').html() + '</div>' + $('#product .price li:first').html() + '' + button + '</div></div>';
//             } else {
//                 var menu = '<div class="menu_wrap col-md-4 col-lg-3"><div id="menu">' + $('header #menu').html() + '</div></div>';
//                 var search = '<div id="search_w" class="search_wrap col-md-4 col-lg-5"><div id="search" class="search_form input-group">' + $('#div_search #search').html() + '</div></div>';
//             }
//
//             var phone = '<div class="phone_wrap col-md-2 col-lg-2"><div id="phone">' + $('header #phone').html() + '</div></div>';
//             var account = '<div class="account_wrap col-md-1 col-lg-1"><div id="account">' + $('#top #account').html() + '</div></div>';
//             var cart = '<div class="cart_wrap col-md-1 col-lg-1"><div id="cart">' + $('header #cart').html() + '</div></div>';
//
//             $('#menu').after('<div id="menu_wrap"><div class="container"><div class="row">' + menu + ' ' + search + ' ' + product + ' ' + phone + ' ' + account + ' ' + cart + '</div></div></div>');
//
//             $('.product_wrap button').click(function () {
//                 $('#button-cart').click();
//             });
//
//             if (product) {
//                 scroll_text('#menu_wrap .product_wrap .product_name', '#menu_wrap .product_wrap .product_name span');
//             }
//
//             $(window).scroll(function () {
//                 if ($(this).scrollTop() > 190) {
//                     $('#menu, #menu_wrap').addClass('show');
//                     $('#div_search #search').attr('id', 'search_');
//                 } else {
//                     $('#menu, #menu_wrap').removeClass('show');
//                     $('#div_search #search_').attr('id', 'search');
//                 }
//             });
//         }
//     }
//
//     menu();
//     $(window).resize(menu);
// }
//
// function fly_cart() {
//     if (!fly_menu_enabled) {
//         $(window).scroll(function () {
//             if ($(window).width() > 992) {
//                 if ($(this).scrollTop() > 100) {
//                     $('#cart').addClass('fly');
//                 } else {
//                     $('#cart').removeClass('fly');
//                 }
//                 if ($(this).scrollTop() > 190) {
//                     $('#cart').addClass('fly2');
//                 } else {
//                     $('#cart').removeClass('fly2');
//                 }
//             }
//         });
//     }
// }
//
// function fly_callback(text) {
//     $('body').append('<div class="fly_callback" onclick="callback()"><i class="fa fa-phone" aria-hidden="true"></i></div>');
//
//     $fly_callback = $('.fly_callback');
//
//     if (text) {
//         $fly_callback.attr('title', text).attr('data-toggle', 'tooltips');
//         $('[data-toggle=\'tooltips\']').tooltip({container: 'body', trigger: 'hover'});
//     }
//     $(window).scroll(function () {
//         if ($(this).scrollTop() > 190) {
//             $fly_callback.addClass('show');
//         } else {
//             $fly_callback.removeClass('show');
//         }
//     });
// }
//
// function add_additional_img() {
//     $('.image a > img, .thumbnails a > img').each(function () {
//         if ($(this).attr('data-status')) {
//             $(this).addClass('greyimage').after('<div class="product_status status_' + $(this).attr('data-status-id') + '">' + $(this).attr('data-status') + '</div>');
//         }
//         if ($(this).attr('data-additional')) {
//             $(this).addClass('main').after('<img src="' + $(this).attr('data-additional') + '" class="additional img-responsive" title="' + $(this).attr('alt') + '" />');
//         }
//     });
// }
//
// function change_opt_img() {
//     $('.product-thumb .option span.img').bind('click', function () {
//         $(this).parent().parent().parent().parent().prev().find('a img:first').attr('src', $(this).attr('data-thumb'));
//         $(this).parent().parent().parent().parent().parent().prev().find('a img:first').attr('src', $(this).attr('data-thumb'));
//     });
// }
//
// function m_filter() {
//     if ($(window).width() < 767) {
//         if ($('#column-left #filterpro_box').size()) {
//             $('#column-left #filterpro_box').css('height', $(window).height());
//             $('#column-left').after('<div id="filterpro_box_open">' + $('#filterpro_box .heading span').text() + '</div');
//             if (!$('.app_filter').size()) {
//                 $('#filterpro_box').append('<div style="margin:15px 0; text-align:center"><button class="app_filter btn btn-primary">Применить</button></div>');
//             }
//             $('#filterpro_box_open').on('click', function () {
//                 $('#column-left, #filterpro_box_open').addClass('show');
//             });
//
//             $('.app_filter, .clear_filter').on('click', function () {
//                 $('#column-left, #filterpro_box_open').removeClass('show');
//                 scroll_to('h1.heading');
//             });
//         }
//
//         if ($('#column-left #megafilter-box').size()) {
//             $('#column-left #megafilter-box').css('height', $(window).height());
//             $('#column-left').after('<div id="megafilter_box_open">Фильтр</div');
//             if (!$('.app_filter').size()) {
//                 $('.mfilter-box').append('<div style="margin:15px 0; text-align:center"><button class="app_filter btn btn-primary">Применить</button></div>');
//             }
//             $('#megafilter_box_open').on('click', function () {
//                 $('#column-left, #megafilter_box_open').addClass('show');
//             });
//
//             $('.app_filter, .clear_filter').on('click', function () {
//                 $('#column-left, #megafilter_box_open').removeClass('show');
//                 scroll_to('h1.heading');
//             });
//         }
//     } else {
//         $('.app_filter, #filterpro_box_open, #megafilter_box_open').remove();
//         $('#column-left #filterpro_box, #column-left #megafilter_box').removeAttr('style');
//     }
// }
//
// function quantity(data, minimum, flag) {
//     var input = $(data).parent().parent().find('input[name="quantity"]');
//     var minimum = parseFloat(minimum);
//
//     if (flag == '+') {
//         input.val(parseFloat(input.val()) + 1);
//     }
//
//     if (flag == '-') {
//         if (input.val() > minimum) {
//             input.val(parseFloat(input.val()) - 1);
//         }
//     }
// }
//
// function banner_link(url) {
//     $('#modal-banner').remove();
//
//     $.ajax({
//         url: url,
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             var data = $(data);
//
//             title = data.find('h1.heading').text();
//             data.find('h1.heading').remove();
//             text = data.find('#content').html();
//
//             html = '<div id="modal-banner" class="modal fade">';
//             html += '<div class="modal-dialog">';
//             html += '<div class="modal-content">';
//             html += '<div class="modal-header">';
//             html += '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>';
//             html += '<h4 class="modal-title">' + title + '</h4>';
//             html += '</div>';
//             html += '<div class="modal-body">' + text + '</div>';
//             html += '</div>';
//             html += '</div>';
//             html += '</div>';
//
//             $('html body').append(html);
//             $('#modal-banner').modal('show');
//         }
//     });
// }
//
// function quick_order(id) {
//     $('#modal-quick-order').remove();
//
//     $.ajax({
//         url: 'index.php?route=unishop/quick_order&id=' + id,
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             $('html body').append(data);
//             $('#modal-quick-order').modal('show');
//         }
//     });
// }
//
// function add_quick_order() {
//     $.ajax({
//         url: 'index.php?route=unishop/quick_order/add',
//         type: 'post',
//         data: $('#quick_order input, #quick_order select, #quick_order textarea').serialize(),
//         dataType: 'json',
//         beforeSend: function () {
//             $('.add_quick_order').button('loading');
//         },
//         complete: function () {
//             $('.add_quick_order').button('reset');
//         },
//         success: function (json) {
//
//             $('.text-danger').remove();
//
//             $('.form-group').removeClass('has-error');
//
//             if (json['error']) {
//                 if (json['error']['option']) {
//                     for (i in json['error']['option']) {
//
//                         var element = $('#quick_order #input-option' + i.replace('_', '-'));
//
//                         if (element.parent().hasClass('input-group')) {
//                             element.parent().after('<div class="text-danger">' + json['error']['option'][i] + '</div>');
//                         } else {
//                             element.after('<div class="text-danger">' + json['error']['option'][i] + '</div>');
//                         }
//                     }
//                 }
//             }
//
//             if (json['error_c']) {
//                 for (i in json['error_c']) {
//                     $('.add_quick_order').before('<div class="text-danger" style="margin:0 auto 10px;">' + json['error_c'][i] + '</div>');
//                 }
//             }
//
//             if (json['success']) {
//                 $('#quick_order #product').html('<div class="row"><div class="col-xs-12">' + json['success_text'] + '</div></div>')
//             }
//         }
//     });
// }
//
// function callback(reason, id) {
//     if (typeof (reason) == 'undefined') {
//         reason = '';
//     }
//     if (typeof (id) == 'undefined') {
//         id = '';
//     }
//
//     $('#modal-request-form').remove();
//
//     $.ajax({
//         url: 'index.php?route=unishop/request&reason=' + reason + '&id=' + id,
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             $('html body').append(data);
//             $('#modal-request-form').modal('show');
//         }
//     });
// }
//
// function send_callback() {
//     $.ajax({
//         url: 'index.php?route=unishop/request/mail',
//         type: 'post',
//         data: $('.callback input, .callback textarea').serialize(),
//         dataType: 'json',
//         beforeSend: function () {
//             $('.callback_button').button('loading');
//         },
//         complete: function () {
//             $('.callback_button').button('reset');
//         },
//         success: function (json) {
//             if (json['success']) {
//                 $('#callback > div').html($('<div class="callback_success">' + json['success'] + '</div>').fadeIn());
//             }
//
//             $('#callback .text-danger, #callback hr').remove();
//
//             if (json['error']) {
//                 for (i in json['error']) {
//                     $('.callback_button').before('<div class="text-danger" style="margin:-5px auto 10px;">' + json['error'][i] + '</div>');
//                 }
//             }
//         }
//     });
// }
//
// function login() {
//     $('#modal-login-form').remove();
//
//     $.ajax({
//         url: 'index.php?route=unishop/login_register',
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             $('html body').append(data);
//             $('#modal-login-form').modal('show');
//         }
//     });
// }
//
// function send_login() {
//     $.ajax({
//         url: 'index.php?route=unishop/login_register/login',
//         type: 'post',
//         data: $('#modal-login-form input, #modal-login-form textarea').serialize(),
//         dataType: 'json',
//         beforeSend: function () {
//             $('.login_button').button('loading');
//         },
//         complete: function () {
//             $('.login_button').button('reset');
//         },
//         success: function (json) {
//             if (json['redirect']) {
//                 if (window.location.pathname == '/logout/') {
//                     location = json['redirect'];
//                 } else {
//                     window.location.reload();
//                 }
//             }
//
//             $('#modal-login-form .text-danger').remove();
//
//             if (json['error']) {
//                 $('.login_button').before($('<div class="text-danger" style="margin:0 auto 10px;">' + json['error'] + '</div>'));
//             }
//         }
//     });
// }
//
// function register() {
//     $('#modal-register-form').remove();
//
//     $.ajax({
//         url: 'index.php?route=unishop/login_register',
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             $('html body').append(data);
//             $('#modal-register-form').modal('show');
//         }
//     });
// }

function send_register() {
    $.ajax({
        url: 'index.php?route=unishop/login_register/register',
        type: 'post',
        data: $('#modal-register-form input, #modal-register-form textarea').serialize(),
        dataType: 'json',
        beforeSend: function () {
            $('.register_button').button('loading');
        },
        complete: function () {
            $('.register_button').button('reset');
        },
        success: function (json) {
            if (json['redirect']) {
                location = json['redirect'];
            }
            if (json['appruv']) {
                $('.popup_register').html($('<div class="register_success">' + json['appruv'] + '</div>').fadeIn());
            }

            $('#popup_register .text-danger').remove();

            if (json['error']) {
                for (i in json['error']) {
                    $('.register_button').before('<div class="text-danger" style="margin:0 auto 10px;">' + json['error'][i] + '</div>');
                }
            }
        }
    });
}
//
// function scroll_to(hash) {
//     var destination = $(hash).offset().top - 100;
//     $('html, body').animate({scrollTop: destination}, 400);
// }
//
// function scroll_text(target_div, target_text) {
//     $(target_div).mouseover(function () {
//         $(this).stop();
//         var boxWidth = $(this).width();
//         var textWidth = $($(target_text), $(this)).width();
//
//         if (textWidth > boxWidth) {
//             $(target_text).animate({left: -((textWidth + 20) - boxWidth)}, 800);
//         }
//     }).mouseout(function () {
//         $(target_text).stop().animate({left: 0}, 800);
//     });
// }
//
// function uni_live_search(show_image, show_description, show_rating, show_price, show_limit, all_results, empty_results) {
//     data_id = 'div_search';
//     $('body').on('click', function () {
//         $('.live-search').hide();
//     });
//     $('header .form-control.input-lg').attr('autocomplete', 'off')
//
//     $('body').on('input click', 'header .form-control.input-lg', function () {
//         data_id = $(this).parent().parent().attr('id');
//         if (!$('.' + data_id).size()) {
//             $(this).parent().after('<div id="live-search" class="live-search ' + data_id + '"><ul></ul></div>');
//         }
//
//         if ($(this).val().length >= 3) {
//             $.ajax({
//                 url: 'index.php?route=unishop/search&filter_name=' + $('#' + data_id + ' input[name=\'search\']').val() + '&category_id=' + $('#' + data_id + ' input[name=\'filter_category_id\']').val(),
//                 dataType: 'json',
//                 beforeSend: function () {
//                     $('.' + data_id + ' ul').html('<li style="text-align:center;"><i class="fa fa-spinner" aria-hidden="true"></i></li>');
//                 },
//                 complete: function () {
//                     $('.' + data_id + ' ul').html();
//                 },
//                 success: function (result) {
//                     var products = result.products;
//                     $('.' + data_id + ' ul li').remove();
//                     if (!$.isEmptyObject(products)) {
//                         $(products).each(function (index, product) {
//                             html = '';
//                             html += '<li onclick="location=\'' + product.url + '\'">';
//                             if (product.image && show_image) {
//                                 html += '<div class="product-image"><img alt="' + product.name + '" src="' + product.image + '"></div>';
//                             }
//                             html += '<div class="product-name">' + product.name;
//                             if (show_description || show_rating) {
//                                 html += '<p>';
//                                 if (show_description) {
//                                     html += '<span>' + product.description + '</span>';
//                                 }
//                                 if (show_rating) {
//                                     html += '<span class="rating">';
//                                     for (var i = 1; i <= 5; i++) {
//                                         if (product.rating < i) {
//                                             html += '<i class="fa fa-star-o"></i>';
//                                         } else {
//                                             html += '<i class="fa fa-star"></i>';
//                                         }
//                                     }
//                                     html += '</span>';
//                                 }
//                                 html += '</p>';
//                             }
//                             html += '</div>';
//                             if (show_price) {
//                                 if (product.special) {
//                                     html += '<div class="product-price"><span class="special">' + product.price + '</span><span class="price">' + product.special + '</span></div>';
//                                 } else {
//                                     html += '<div class="product-price"><span class="price">' + product.price + '</span></div>';
//                                 }
//                             }
//                             html += '</li>';
//                             $('.' + data_id + ' ul').append(html);
//                         });
//                         if (parseFloat(show_limit) < parseFloat(result.products_total)) {
//                             var description = '';
//                             if (show_description) {
//                                 var description = '&description=true';
//                             }
//                             $('.' + data_id + ' ul').append('<li style="text-align:center;"><a href="index.php?route=product/search&search=' + $('#' + data_id + ' input[name=\'search\']').val() + '' + description + '">' + all_results + ' (' + result.products_total + ')</a></li>');
//                         }
//                     } else {
//                         $('.' + data_id + ' ul').html('<li style="text-align:center;padding:5px 0;">' + empty_results + '</li>');
//                     }
//                     $('.' + data_id).css('display', 'block');
//                 }
//             });
//         }
//     });
// }
//
// // Cart add remove functions
// var cart = {
//     'add': function (product_id, quantity, quick_order) {
//
//         if ($('#option_' + product_id).children().size() > 0) {
//             var options = $('#option_' + product_id + ' input[type=\'radio\']:checked, #option_' + product_id + ' input[type=\'checkbox\']:checked, #option_' + product_id + ' select');
//             var data = options.serialize() + '&product_id=' + product_id + '&quantity=' + (typeof (quantity) != 'undefined' ? quantity : 1);
//         } else {
//             var data = 'product_id=' + product_id + '&quantity=' + (typeof (quantity) != 'undefined' ? quantity : 1);
//         }
//
//         $.ajax({
//             url: 'index.php?route=checkout/cart/add',
//             type: 'post',
//             data: data,
//             dataType: 'json',
//             success: function (json) {
//                 $('.text-danger').remove();
//
//                 if (json['redirect'] && !quick_order && !options) {
//                     location = json['redirect'];
//                 }
//
//                 $('.form-group').removeClass('has-error');
//
//                 if (json['error']) {
//                     if (json['error']['option']) {
//                         for (i in json['error']['option']) {
//                             if (!quick_order) {
//                                 var element = $('#input-option' + i.replace('_', '-'));
//                             } else {
//                                 var element = $('#quick_order #input-option' + i.replace('_', '-'));
//                             }
//
//                             if (element.parent().hasClass('input-group')) {
//                                 element.parent().after('<div class="text-danger">' + json['error']['option'][i] + '</div>');
//                             } else {
//                                 element.after('<div class="text-danger">' + json['error']['option'][i] + '</div>');
//                             }
//                         }
//                     }
//                 }
//
//                 if (json['success']) {
//                     $('.tooltip').remove();
//
//                     $('#modal-cart').remove();
//
//                     html = '';
//                     html += '<div id="modal-cart" class="modal fade">';
//                     html += '<div class="modal-dialog">';
//                     html += '<div class="modal-content">';
//                     html += '<div class="modal-header">';
//                     html += '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>';
//                     html += '</div>';
//                     html += '<div class="modal-body">';
//                     html += json['success_new'];
//                     html += '</div>';
//                     html += '</div>';
//                     html += '</div>';
//                     html += '</div>';
//
//                     if (!$('#unicheckout').length) {
//                         $('html body').append(html);
//                         $('#modal-cart').modal('show');
//                     }
//
//                     $('#cart > button').html('<i class="fa fa-shopping-basket"></i><span id="cart-total">' + json['total_items'] + '</span>');
//                     $('#cart > ul').load('index.php?route=common/cart/info ul li');
//
//                     $('#cart').addClass('show');
//                     replace_button(product_id);
//                 }
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     },
//     'update': function (key, quantity) {
//         $('#cart, #cart .dropdown-menu').addClass('open2');
//         $.ajax({
//             url: 'index.php?route=checkout/cart/edit',
//             type: 'post',
//             data: 'quantity[' + key + ']=' + quantity,
//             dataType: 'html',
//             success: function (data) {
//                 $('#cart, .cart_wrap #cart').load('index.php?route=common/cart/info #cart > *');
//
//                 if (getURLVar('route') == 'checkout/cart' || getURLVar('route') == 'checkout/checkout') {
//                     $('#content').load('index.php?route=checkout/cart #content > *');
//                 }
//
//                 p_array();
//
//                 $('#cart, .cart_wrap #cart').addClass('open').removeClass('open2');
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     },
//     'remove': function (key, product_id) {
//         $.ajax({
//             url: 'index.php?route=checkout/cart/remove',
//             type: 'post',
//             data: 'key=' + key,
//             dataType: 'json',
//             success: function (json) {
//                 // Need to set timeout otherwise it wont update the total
//                 //setTimeout(function () {
//                 $('#cart > button').html('<i class="fa fa-shopping-basket"></i><span id="cart-total">' + json['total_items'] + '</span>');
//                 //}, 100);
//
//                 if (getURLVar('route') == 'checkout/cart' || getURLVar('route') == 'checkout/checkout') {
//                     location = 'index.php?route=checkout/cart';
//                 } else if (getURLVar('route') == 'checkout/unicheckout') {
//                     cart_update();
//                     $('#cart > ul').load('index.php?route=common/cart/info ul li');
//                 } else {
//                     $('#cart > ul').load('index.php?route=common/cart/info ul li');
//                 }
//
//                 return_button(product_id);
//                 $('#cart, .cart_wrap #cart').removeClass('show');
//                 //$('#cart').addClass('open').removeClass('open2');
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     }
// }
//
// var voucher = {
//     'add': function () {
//
//     },
//     'remove': function (key) {
//         $.ajax({
//             url: 'index.php?route=checkout/cart/remove',
//             type: 'post',
//             data: 'key=' + key,
//             dataType: 'json',
//             beforeSend: function () {
//                 $('#cart > button').button('loading');
//             },
//             complete: function () {
//                 $('#cart > button').button('reset');
//             },
//             success: function (json) {
//                 // Need to set timeout otherwise it wont update the total
//                 //setTimeout(function () {
//                 $('#cart > button').html('<span id="cart-total"><i class="fa fa-shopping-cart"></i> ' + json['total'] + '</span>');
//                 //}, 100);
//
//                 if (getURLVar('route') == 'checkout/cart' || getURLVar('route') == 'checkout/checkout') {
//                     location = 'index.php?route=checkout/cart';
//                 } else {
//                     $('#cart > ul').load('index.php?route=common/cart/info ul li');
//                 }
//
//                 if (getURLVar('route') == 'checkout/unicheckout') {
//                     update_checkout();
//                 }
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     }
// }
//
// var wishlist = {
//     'add': function (product_id) {
//         $.ajax({
//             url: 'index.php?route=account/wishlist/add',
//             type: 'post',
//             data: 'product_id=' + product_id,
//             dataType: 'json',
//             success: function (json) {
//                 $('.alert').remove();
//
//                 if (json['redirect']) {
//                     location = json['redirect'];
//                 }
//
//                 if (json['success']) {
//                     $('#content').parent().before('<div class="alert alert-success"><i class="fa fa-check-circle"></i> ' + json['success'] + ' <button type="button" class="close" data-dismiss="alert">&times;</button></div>');
//                 }
//
//                 $('#wishlist-total span').html(json['total']);
//                 $('#wishlist-total').attr('title', json['total']);
//
//                 //$('html, body').animate({ scrollTop: 0 }, 'slow');
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     },
//     'remove': function () {
//
//     }
// }
//
// var compare = {
//     'add': function (product_id) {
//         $.ajax({
//             url: 'index.php?route=product/compare/add',
//             type: 'post',
//             data: 'product_id=' + product_id,
//             dataType: 'json',
//             success: function (json) {
//                 $('.alert').remove();
//
//                 if (json['success']) {
//                     $('#content').parent().before('<div class="alert alert-success"><i class="fa fa-check-circle"></i> ' + json['success'] + ' <button type="button" class="close" data-dismiss="alert">&times;</button></div>');
//
//                     $('#compare-total').html(json['total']);
//
//                     //$('html, body').animate({ scrollTop: 0 }, 'slow');
//                 }
//             },
//             error: function (xhr, ajaxOptions, thrownError) {
//                 alert(thrownError + "\r\n" + xhr.statusText + "\r\n" + xhr.responseText);
//             }
//         });
//     },
//     'remove': function () {
//
//     }
// }
//
// $(document).delegate('.agree', 'click', function (e) {
//     e.preventDefault();
//
//     $('#modal-agree').remove();
//
//     var element = this;
//
//     $.ajax({
//         url: $(element).attr('href'),
//         type: 'get',
//         dataType: 'html',
//         success: function (data) {
//             var text = $(data).find('.article_description').length ? $(data).find('.article_description').html() : data;
//
//             html = '<div id="modal-agree" class="modal">';
//             html += '	<div class="modal-dialog">';
//             html += '    <div class="modal-content">';
//             html += '      <div class="modal-header">';
//             html += '        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>';
//             html += '        <h4 class="modal-title">' + $(element).text() + '</h4>';
//             html += '      </div>';
//             html += '      <div class="modal-body">' + text + '</div>';
//             html += '    </div';
//             html += '  </div>';
//             html += '</div>';
//
//             $('body').append(html);
//
//             $('#modal-agree').modal('show');
//         }
//     });
// });
//
// function getURLVar(key) {
//     var value = [];
//
//     var query = String(document.location).split('?');
//
//     if (query[1]) {
//         var part = query[1].split('&');
//
//         for (i = 0; i < part.length; i++) {
//             var data = part[i].split('=');
//
//             if (data[0] && data[1]) {
//                 value[data[0]] = data[1];
//             }
//         }
//
//         if (value[key]) {
//             return value[key];
//         } else {
//             return '';
//         }
//     }
// }
//
// (function ($) {
//     $.fn.autocomplete = function (option) {
//         return this.each(function () {
//             this.timer = null;
//             this.items = new Array();
//
//             $.extend(this, option);
//
//             $(this).attr('autocomplete', 'off');
//
//             // Focus
//             $(this).on('focus', function () {
//                 this.request();
//             });
//
//             // Blur
//             $(this).on('blur', function () {
//                 setTimeout(function (object) {
//                     object.hide();
//                 }, 200, this);
//             });
//
//             // Keydown
//             $(this).on('keydown', function (event) {
//                 switch (event.keyCode) {
//                     case 27: // escape
//                         this.hide();
//                         break;
//                     default:
//                         this.request();
//                         break;
//                 }
//             });
//
//             // Click
//             this.click = function (event) {
//                 event.preventDefault();
//
//                 value = $(event.target).parent().attr('data-value');
//
//                 if (value && this.items[value]) {
//                     this.select(this.items[value]);
//                 }
//             }
//
//             // Show
//             this.show = function () {
//                 var pos = $(this).position();
//
//                 $(this).siblings('ul.dropdown-menu').css({
//                     top: pos.top + $(this).outerHeight(),
//                     left: pos.left
//                 });
//
//                 $(this).siblings('ul.dropdown-menu').show();
//             }
//
//             // Hide
//             this.hide = function () {
//                 $(this).siblings('ul.dropdown-menu').hide();
//             }
//
//             // Request
//             this.request = function () {
//                 clearTimeout(this.timer);
//
//                 this.timer = setTimeout(function (object) {
//                     object.source($(object).val(), $.proxy(object.response, object));
//                 }, 200, this);
//             }
//
//             // Response
//             this.response = function (json) {
//                 html = '';
//
//                 if (json.length) {
//                     for (i = 0; i < json.length; i++) {
//                         this.items[json[i]['value']] = json[i];
//                     }
//
//                     for (i = 0; i < json.length; i++) {
//                         if (!json[i]['category']) {
//                             html += '<li data-value="' + json[i]['value'] + '"><a href="#">' + json[i]['label'] + '</a></li>';
//                         }
//                     }
//
//                     // Get all the ones with a categories
//                     var category = new Array();
//
//                     for (i = 0; i < json.length; i++) {
//                         if (json[i]['category']) {
//                             if (!category[json[i]['category']]) {
//                                 category[json[i]['category']] = new Array();
//                                 category[json[i]['category']]['name'] = json[i]['category'];
//                                 category[json[i]['category']]['item'] = new Array();
//                             }
//
//                             category[json[i]['category']]['item'].push(json[i]);
//                         }
//                     }
//
//                     for (i in category) {
//                         html += '<li class="dropdown-header">' + category[i]['name'] + '</li>';
//
//                         for (j = 0; j < category[i]['item'].length; j++) {
//                             html += '<li data-value="' + category[i]['item'][j]['value'] + '"><a href="#">&nbsp;&nbsp;&nbsp;' + category[i]['item'][j]['label'] + '</a></li>';
//                         }
//                     }
//                 }
//
//                 if (html) {
//                     this.show();
//                 } else {
//                     this.hide();
//                 }
//
//                 $(this).siblings('ul.dropdown-menu').html(html);
//             }
//
//             $(this).after('<ul class="dropdown-menu"></ul>');
//             $(this).siblings('ul.dropdown-menu').delegate('a', 'click', $.proxy(this.click, this));
//
//         });
//     }
// })(window.jQuery);