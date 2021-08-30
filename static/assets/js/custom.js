(function($) {
    "use strict";

	// ______________Cover Image
	$(".cover-image").each(function() {
		var attr = $(this).attr('data-image-src');
		if (typeof attr !== typeof undefined && attr !== false) {
			$(this).css('background', 'url(' + attr + ') center center');
		}
	});

	$('.table-subheader').click(function(){
		$(this).nextUntil('tr.table-subheader').slideToggle(100);
	});

	// ______________ Horizonatl
	$(document).ready(function() {
      $("a[data-theme]").click(function() {
        $("head link#theme").attr("href", $(this).data("theme"));
        $(this).toggleClass('active').siblings().removeClass('active');
      });

      $("a[data-effect]").click(function() {
        $("head link#effect").attr("href", $(this).data("effect"));
        $(this).toggleClass('active').siblings().removeClass('active');
      });
    });

	// ______________Full screen
	$("#fullscreen-button").on("click", function toggleFullScreen() {
      if ((document.fullScreenElement !== undefined && document.fullScreenElement === null) || (document.msFullscreenElement !== undefined && document.msFullscreenElement === null) || (document.mozFullScreen !== undefined && !document.mozFullScreen) || (document.webkitIsFullScreen !== undefined && !document.webkitIsFullScreen)) {
        if (document.documentElement.requestFullScreen) {
          document.documentElement.requestFullScreen();
        } else if (document.documentElement.mozRequestFullScreen) {
          document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullScreen) {
          document.documentElement.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
        } else if (document.documentElement.msRequestFullscreen) {
          document.documentElement.msRequestFullscreen();
        }
      } else {
        if (document.cancelFullScreen) {
          document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
          document.webkitCancelFullScreen();
        } else if (document.msExitFullscreen) {
          document.msExitFullscreen();
        }
      }
    })

	// ______________Active Class
	$(document).ready(function() {
		$(".horizontalMenu-list li a").each(function() {
			var pageUrl = window.location.href.split(/[?#]/)[0];
			if (this.href == pageUrl) {
				$(this).addClass("active");
				$(this).parent().addClass("active"); // add active to li of the current link
				$(this).parent().parent().prev().addClass("active"); // add active class to an anchor
				$(this).parent().parent().prev().click(); // click the item to make it drop
			}
		});
		$(".horizontal-megamenu li a").each(function() {
			var pageUrl = window.location.href.split(/[?#]/)[0];
			if (this.href == pageUrl) {
				$(this).addClass("active");
				$(this).parent().addClass("active"); // add active to li of the current link
				$(this).parent().parent().parent().parent().parent().parent().parent().prev().addClass("active"); // add active class to an anchor
				$(this).parent().parent().prev().click(); // click the item to make it drop
			}
		});
		$(".horizontalMenu-list .sub-menu .sub-menu li a").each(function() {
			var pageUrl = window.location.href.split(/[?#]/)[0];
			if (this.href == pageUrl) {
				$(this).addClass("active");
				$(this).parent().addClass("active"); // add active to li of the current link
				$(this).parent().parent().parent().parent().prev().addClass("active"); // add active class to an anchor
				$(this).parent().parent().prev().click(); // click the item to make it drop
			}
		});
	});

	// ______________Quantity Cart Increase & Descrease
	$(function () {
		$('.add').on('click',function(){
			var $qty=$(this).closest('div').find('.qty');
			var currentVal = parseInt($qty.val());
			if (!isNaN(currentVal)) {
				$qty.val(currentVal + 1);
			} 
			
		});
		$('.minus').on('click',function(){
			var $qty=$(this).closest('div').find('.qty');
			var currentVal = parseInt($qty.val());
			if (!isNaN(currentVal) && currentVal > 0) {
				$qty.val(currentVal - 1);
			}
		});
	});

	// __________MODAL
	
	// showing modal with effect
	$('.modal-effect').on('click', function(e) {
		e.preventDefault();
		var effect = $(this).attr('data-bs-effect');
		$('#modaldemo8').addClass(effect);
	});
		
	// hide modal with effect
	$('#modaldemo8').on('hidden.bs.modal', function(e) {
		$(this).removeClass(function(index, className) {
			return (className.match(/(^|\s)effect-\S+/g) || []).join(' ');
		});
	});

	// ______________ Page Loading
	$(window).on("load", function(e) {
		$("#global-loader").fadeOut("slow");
	})

	// ______________Back to top Button
	$(window).on("scroll", function(e) {
    	if ($(this).scrollTop() > 0) {
            $('#back-to-top').fadeIn('slow');
        } else {
            $('#back-to-top').fadeOut('slow');
        }
    });
    $("#back-to-top").on("click", function(e){
        $("html, body").animate({
            scrollTop: 0
        }, 0);
        return false;
    });

	// ______________ StarRating
	var ratingOptions = {
		selectors: {
			starsSelector: '.rating-stars',
			starSelector: '.rating-star',
			starActiveClass: 'is--active',
			starHoverClass: 'is--hover',
			starNoHoverClass: 'is--no-hover',
			targetFormElementSelector: '.rating-value'
		}
	};
	$(".rating-stars").ratingStars(ratingOptions);

	// ______________ Chart-circle
	if ($('.chart-circle').length) {
		$('.chart-circle').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: '#e2e2e9',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Chart-circle
	if ($('.chart-circle-transparent').length) {
		$('.chart-circle-transparent').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: 'rgba(0, 0, 0, 0.1)',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Chart-circle
	if ($('.chart-circle-primary').length) {
		$('.chart-circle-primary').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: 'rgba(112, 94, 200, 0.4)',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Chart-circle
	if ($('.chart-circle-secondary').length) {
		$('.chart-circle-secondary').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: 'rgba(251, 28, 82, 0.4)',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Chart-circle
	if ($('.chart-circle-success').length) {
		$('.chart-circle-success').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: 'rgba(66, 196, 138, 0.5)',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Chart-circle
	if ($('.chart-circle-warning').length) {
		$('.chart-circle-warning').each(function() {
			let $this = $(this);

			$this.circleProgress({
			  fill: {
				color: $this.attr('data-color')
			  },
			  size: $this.height(),
			  startAngle: -Math.PI / 4 * 2,
			  emptyFill: 'rgba(255, 171, 0, 0.5)',
			  lineCap: 'round'
			});
		});
	}

	// ______________ Global Search
	$(document).on("click", "[data-bs-toggle='search']", function(e) {
		var body = $("body");

		if(body.hasClass('search-gone')) {
			body.addClass('search-gone');
			body.removeClass('search-show');
		}else{
			body.removeClass('search-gone');
			body.addClass('search-show');
		}
	});
	var toggleSidebar = function() {
		var w = $(window);
		if(w.outerWidth() <= 1024) {
			$("body").addClass("sidebar-gone");
			$(document).off("click", "body").on("click", "body", function(e) {
				if($(e.target).hasClass('sidebar-show') || $(e.target).hasClass('search-show')) {
					$("body").removeClass("sidebar-show");
					$("body").addClass("sidebar-gone");
					$("body").removeClass("search-show");
				}
			});
		}else{
			$("body").removeClass("sidebar-gone");
		}
	}
	toggleSidebar();
	$(window).resize(toggleSidebar);

	$(document).on("click", ".close-btn", function() {
		$("body").removeClass("search-show");
	});

	const DIV_CARD = 'div.card';

	// ______________ Attach Remove
	$(document).on('click', '[data-toggle="remove"]', function(e) {
		let $a = $(this).closest(".attach-supportfiles");
		$a.remove();
		e.preventDefault();
		return false;
	});

	
	// ______________ Tooltip
	var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
	var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
 	 return new bootstrap.Tooltip(tooltipTriggerEl)
	})


	// ______________ Popover
	var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
	var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	html:
	return new bootstrap.Popover(popoverTriggerEl)
	})
	
	// ______________ Card Remove
	$(document).on('click', '[data-bs-toggle="card-close"]', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.remove();
		e.preventDefault();
		return false;
	});


	// ______________ Card Remove
	$(document).on('click', '[data-bs-toggle="card-remove"]', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.remove();
		e.preventDefault();
		return false;
	});

	// ______________ Card Collapse
	$(document).on('click', '[data-bs-toggle="card-collapse"]', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-collapsed');
		e.preventDefault();
		return false;
	});

	// ______________ Card Fullscreen
	$(document).on('click', '[data-bs-toggle="card-fullscreen"]', function(e) {
		let $card = $(this).closest(DIV_CARD);
		$card.toggleClass('card-fullscreen').removeClass('card-collapsed');
		e.preventDefault();
		return false;
	});

	// sparkline1
	$(".sparkline_bar").sparkline([2, 4, 3, 4, 5, 4, 5, 4, 3, 4], {
		height: 20,
		type: 'bar',
		colorMap: {
			'7': '#a1a1a1'
		},
		barColor: '#ff5b51'
	});

	// sparkline2
	$(".sparkline_bar1").sparkline([3, 4, 3, 4, 5, 4, 5, 6, 4, 6,], {
		height: 20,
		type: 'bar',
		colorMap: {
			'7': '#c34444'
		},
		barColor: '#44c386'
	});

	// sparkline3
	$(".sparkline_bar2").sparkline([3, 4, 3, 4, 5, 4, 5, 6, 4, 6,], {
		height: 20,
		type: 'bar',
		colorMap: {
			'7': '#a1a1a1'
		},
		barColor: '#fa057a'
	});

	// ______________ SWITCHER-toggle ______________//
	
	$('.layout-setting').on("click", function(e) {
		if (document) {
			$('body').toggleClass('dark-mode');
		} else {
			$('body').removeClass('dark-mode');
			$('body').addClass('light-mode');
		}
	});

	$(document).on("click", "a[data-sidetheme]", function() {
		$("head link#sidemenu-theme").attr("href", $(this).data("sidetheme"));
	  });
	  
	  $('.default-menu').on('click', function() {
		$('body').addClass('menu1') 
		$('body').removeClass('menu2') 
		$('body').removeClass('menu3') 
		var ww = document.body.clientWidth;
		if (ww >= 767) {
			$('body').removeClass('sidenav-toggled');
		}
	});
	$('.sideicon-menu').on('click', function() {
		$('body').addClass('menu3') 
		$('body').removeClass('menu2') 
		$('body').removeClass('menu1') 
		jQuery(document).ready(function($) {
			var alterClass = function() {
			var ww = document.body.clientWidth;
			if (ww < 768) {
				$('body').removeClass('sidenav-toggled');
			} else if (ww >= 767) {
				$('body').addClass('sidenav-toggled');
			};
			};
			$(window).resize(function(){
			alterClass();
			});
			//Fire it when the page first loads:
			alterClass();
		});
	});
	$('.icontext-menu').on('click', function() {
		$('body').addClass('menu2') 
		$('body').removeClass('menu1') 
		$('body').removeClass('menu3') 
		jQuery(document).ready(function($) {
			var alterClass = function() {
			var ww = document.body.clientWidth;
			if (ww < 768) {
				$('body').removeClass('sidenav-toggled');
			} else if (ww >= 767) {
				$('body').addClass('sidenav-toggled');
			};
			};
			$(window).resize(function(){
			alterClass();
			});
			//Fire it when the page first loads:
			alterClass();
		});
	});

	/*Theme-layout*/
	$('#background-left1').on('click', function() {
		$('body').addClass('light-mode');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-mode');
		$('body').removeClass('color-header');
		$('body').removeClass('dark-header'); 
		$('body').removeClass('dark-menu');
		$('body').removeClass('gradient-menu');
		$('body').removeClass('gradient-header');
		$('body').removeClass('color-menu');
		return false;
	});

	$('#background-left2').on('click', function() {
		$('body').addClass('dark-mode');
		$('body').removeClass('light-mode');
		$('body').removeClass('light-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('dark-header');
		$('body').removeClass('color-header');
		$('body').removeClass('light-header');
		$('body').removeClass('dark-menu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('gradient-menu');
		return false;
	});

	$('#background1').on('click', function() {
		$('body').addClass('light-header');
		$('body').removeClass('color-header');
		$('body').removeClass('dark-header');
		$('body').removeClass('gradient-header');
		return false;
	  });

	$('#background2').on('click', function() {
		$('body').addClass('color-header');
		$('body').removeClass('light-header');
		$('body').removeClass('dark-header');
		 $('body').removeClass('gradient-header');
		return false;
	  });

	  $('#background3').on('click', function() {
		$('body').addClass('dark-header');
		$('body').removeClass('color-header');
		$('body').removeClass('light-header');
		 $('body').removeClass('gradient-header');
		return false;
	  });

	  $('#background11').on('click', function() {
		$('body').addClass('gradient-header');
		$('body').removeClass('dark-header');
		$('body').removeClass('color-header');
		$('body').removeClass('light-header');
		return false;
	  });

	  $('#background4').on('click', function() {
		$('body').addClass('light-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('gradient-menu');
		$('body').removeClass('light-hormenu');
		 $('body').removeClass('dark-hormenu');
		 $('body').removeClass('color-hormenu');
		return false;
	  });

	  $('#background5').on('click', function() {
		$('body').addClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('gradient-menu');
		$('body').removeClass('light-hormenu');
		 $('body').removeClass('dark-hormenu');
		 $('body').removeClass('color-hormenu');
		return false;
	  });

	  $('#background6').on('click', function() {
		$('body').addClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		$('body').removeClass('light-hormenu');
		 $('body').removeClass('dark-hormenu');
		 $('body').removeClass('dark-hormenu');
		return false;
	  });

	  $('#background10').on('click', function() {
		$('body').addClass('gradient-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('light-hormenu');
		 $('body').removeClass('dark-hormenu');
		 $('body').removeClass('dark-hormenu');
		return false;
	  });

	   /*Layout-width Styles*/
	   $('#background14').on('click', function() {
		$('body').addClass('layout-fullwidth');
		$('body').removeClass('layout-boxed');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	  $('#background15').on('click', function() {
		$('body').addClass('layout-boxed');
		$('body').removeClass('layout-fullwidth');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	   /*Header-Position Styles*/
	   $('#background16').on('click', function() {
		$('body').addClass('fixed-layout');
		$('body').removeClass('scrollable-layout');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	  $('#background17').on('click', function() {
		$('body').addClass('scrollable-layout');
		$('body').removeClass('fixed-layout');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	 

	/*Tag Input Style*/
	$('input, select').on('change', function(event) {
		var $element = $(event.target),
		  $container = $element.closest('.example');
	
		if (!$element.data('tagsinput'))
		  return;
	
		var val = $element.val();
		if (val === null)
		  val = "null";
		$('code', $('pre.val', $container)).html( ($.isArray(val) ? JSON.stringify(val) : "\"" + val.replace('"', '\\"') + "\"") );
		$('code', $('pre.items', $container)).html(JSON.stringify($element.tagsinput('items')));
	  }).trigger('change');
	
	 /*Horizontal Style*/
	 $('#background7').on('click', function() {
		$('body').addClass('light-hormenu');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	  $('#background8').on('click', function() {
		$('body').addClass('color-hormenu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	  $('#background9').on('click', function() {
		$('body').addClass('dark-hormenu');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('gradient-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });

	  $('#background13').on('click', function() {
		$('body').addClass('gradient-hormenu');
		$('body').removeClass('dark-hormenu');
		$('body').removeClass('color-hormenu');
		$('body').removeClass('light-hormenu');
		$('body').removeClass('dark-menu');
		$('body').removeClass('color-menu');
		$('body').removeClass('light-menu');
		$('body').removeClass('gradient-menu');
		return false;
	  });
	  
	  /*Left-menu Styles*/
	  $('#background18').on('click', function() {
		$('body').addClass('default-menu');
		$('body').removeClass('icontext-menu');
		$('body').removeClass('sideicon-menu');
		return false;
	  });
	  $('#background19').on('click', function() {
		$('body').addClass('icontext-menu');
		$('body').removeClass('default-menu');
		$('body').removeClass('sideicon-menu');
		return false;
	  });
	  $('#background20').on('click', function() {
		  $('body').addClass('sideicon-menu');
		$('body').removeClass('default-menu');
		$('body').removeClass('icontext-menu');
		return false;
	  });

})(jQuery);

