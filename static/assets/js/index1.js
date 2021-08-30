$(function(e){
    'use strict'

	/* Apexcharts (#bar) */
	var options = {
		series: [{
		name: 'Net Profit',
		data: [44, 42, 57, 86, 58, 55, 70, 52, 29,56, 75, 61],
		color:['#664dc9']
	  }, {
		name: 'Revenue',
		data: [26, 35, 41, 78, 46, 37, 65, 49, 23, 38, 65, 27]
	  }],
		chart: {
		type: 'bar',
		height: 375
	  },
	  grid: {
		borderColor: '#eff2f6',
	  },
	  colors: ["#664dc9", '#e3dff5'],
	  plotOptions: {
		bar: {
		  horizontal: false,
		  columnWidth: '25%',
		  endingShape: 'rounded'
		},
	  },
	  
	  dataLabels: {
		enabled: false
	  },
	  stroke: {
		show: true,
		width: 3,
		colors: ['transparent']
	  },
	  states: {
		hover: {
		 filter: {
			type: 'none'
		  }
		}
	  },
	  xaxis: {
		categories: ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov','Dec'],
		axisBorder: {
			show: true,
			color: '#e6ebf1',
			offsetX: 0,
			offsetY: 0,
		},
		axisTicks: {
			show: true,
			borderType: 'solid',
			color: '#e6ebf1',
			width: 6,
			offsetX: 0,
			offsetY: 0
		},
	  },
	  fill: {
		opacity: 1
	  },
	  legend: {
		position: "bottom"	
		},
	  };

	  var chart = new ApexCharts(document.querySelector("#statistics"), options);
	  chart.render();
	
	  
	  /* Apexcharts (#bar) closed */
	
	  

    var spark1 = {
		chart: {
		  type: 'area',
		  height: 60,
		  width:120,
		  sparkline: {
			enabled: true
		  },
		  dropShadow: {
			  enabled: false,
			  blur: 3,
			  opacity: 0.2,
			  show:false,
		  }
		  },
		  stroke: {
			  show: true,
			  curve: 'smooth',
			  lineCap: 'butt',
			  colors: undefined,
			  width: 2,
			  dashArray: 0,
		  },
		fill: {
		  gradient: {
			enabled: false
		  }
		},
		series: [{
		  name: 'Total Sales',
		  data: [0, 45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46]
		}],
		yaxis: {
		  min: 0
		},
		colors: ['#664dc9'],
  
	  }
	  var spark1 = new ApexCharts(document.querySelector("#spark1"), spark1);
	  spark1.render();
 
	  var spark2 = {
		chart: {
		  type: 'area',
		  height: 60,
		  width: 120,
		  sparkline: {
			enabled: true
		  },
		  dropShadow: {
			  enabled: false,
			  blur: 3,
			  opacity: 0.2,
		  }
		  },
		  stroke: {
			  show: true,
			  curve: 'smooth',
			  lineCap: 'butt',
			  colors: undefined,
			  width: 2,
			  dashArray: 0,
		  },
		  fill: {
		  gradient: {
			enabled: false
		  }
		},
		series: [{
		  name: 'Total stats',
		  data: [0, 45, 93, 53, 61, 27, 54, 43, 19, 46, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51, 35, 41, 35, 27, ]
		}],
		yaxis: {
		  min: 0
		},
		colors: ['#38cb89'],
  
	  }
	  var spark2 = new ApexCharts(document.querySelector("#spark2"), spark2);
	  spark2.render();

	  var spark3 = {
		chart: {
		  type: 'area',
		  height: 60,
		  width: 120,
		  sparkline: {
			enabled: true
		  },
		  dropShadow: {
			  enabled: false,
			  blur: 3,
			  opacity: 0.2,
		  }
		  },
		  stroke: {
			  show: true,
			  curve: 'smooth',
			  lineCap: 'butt',
			  colors: undefined,
			  width: 2,
			  dashArray: 0,
		  },
		  fill: {
		  gradient: {
			enabled: false
		  }
		},
		series: [{
		  name: 'Total Income',
		  data: [0, 35, 41, 35, 27, 93, 53, 61, 27, 54, 43, 19, 46,45, 54, 38, 56, 24, 65, 31, 37, 39, 62, 51]
		}],
		yaxis: {
		  min: 0
		},
		colors: ['#ffab00'],
  
	  }
	  var spark3 = new ApexCharts(document.querySelector("#spark3"), spark3);
	  spark3.render();
  

	  var spark4 = {
		  chart: {
			type: 'area',
			height: 60,
			width: 120,
			sparkline: {
			  enabled: true
			},
			dropShadow: {
				enabled: false,
				blur: 3,
				opacity: 0.2,	
			}
			},
			stroke: {
				show: true,
				curve: 'smooth',
				lineCap: 'butt',
				colors: undefined,
				width: 2,
				dashArray: 0,
			},
		  fill: {
			gradient: {
			  enabled: false
			}
		  },
		  series: [{
			name: 'Total Tax',
			data: [0, 45, 54, 38, 56, 24, 55, 31, 37, 39, 62, 51, 35, 41, 48, 27, 93, 53, 52, 27, 54, 43, 19, 46]
		  }],
		  yaxis: {
			min: 0
		  },
		  colors: ['#ef4b4b'],
	
		}
		var spark4 = new ApexCharts(document.querySelector("#spark4"), spark4);
		spark4.render();

	

	$('#datatable').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
			lengthMenu: '_MENU_',
		}
	});

	
	const ps4 = new PerfectScrollbar('.recent-activity', {
		useBothWheelAxes:true,
		suppressScrollX:true,
	  });
	
 });