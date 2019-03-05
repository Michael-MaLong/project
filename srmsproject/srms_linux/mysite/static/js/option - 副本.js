var option = {
	title:{
		text:""
	},
	tooltip:{
		show:true,
		showContent:true,
		//triggerOn:"click",
		alwaysShowContent:false,
		enterable:false,
		confine:false,
		position:"right",
		formatter:function(a,b,c){
			if(a.dataType == "node"){
				return a.data.value;
			}
		}
	},/*
	legend:[{
		show:false,
		data:[
			{
				name:"文件夹"
			},
			{
				name:"文件"
			}
		]
	}],*/
	animationDuration:1200,
	animationEasingUpdate:"quinticInOut",
	backgroundColor:"#fff",
	series:[{
		draggable:true,
		symbol:"circle",
		legendHoverLink:true,
		hoverAnimation:true,
		focusNodeAdjacency:false,
		name:"服务器资源监控系统",
		type:"graph",
		roam:true,
		layout:"force",
		force:{
			repulsion:800,
			gravity:0.1,
			layoutAnimation:true
		},/*
		categories:[
			{
				name:"文件夹"
			},
			{
				name:"文件"
			}
		],*/
		label:{
			normal:{
				show:true,
				position:"bottom",
				//formatter:"{b}"
				textStyle:{
					color:"#333"
				}
			},
			emphasis:{
				textStyle:{
					color:"#333"
				}
			}
		},
		itemStyle:{
			normal:{
				color:"#2f4554"
			}
		},
		lineStyle:{
			normal:{
				width:1,
				curveness:0,
				color:"#ccc",
				opacity:1
			},
			emphasis:{
				width:2
			}
		},
		data:[
			{
				name:"aaa",
				path:"root",
				symbol:"circle",
				symbolSize:60,
				value:"sss",
				itemStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				name:"bbb",
				path:"aaa/bbb",
				symbolSize:42,
				value:"bbb",
				itemStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				name:"ccc",
				value:0,
				symbolSize:42
			},
			{
				name:"ddd",
				value:"呵呵呵呵呵",
				symbolSize:42
			},
			{
				name:"eee",
				value:"嗯嗯嗯嗯嗯",
				symbolSize:42,
				itemStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				name:"fff",
				value:"嘿嘿嘿嘿嘿",
				symbolSize:42
			},
			{
				name:"ggg",
				value:0,
				symbolSize:26
			},
			{
				name:"hhh",
				value:0,
				symbolSize:26

			},
			{
				name:"iii",
				value:0,
				symbolSize:26
			},
			{
				name:"jjj",
				value:0,
				symbolSize:26
			},
			{
				name:"kkk.exe",
				value:0,
				symbolSize:26,
				itemStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},


			{
				name:"lll",
				value:0,
				symbolSize:26
			},

			{
				name:"mmm",
				value:0,
				symbolSize:26
			},

			{
				name:"nnn",
				value:0,
				symbolSize:26
			},
			{
				name:"ooo",
				value:0,
				symbolSize:26
			},
			{
				name:"ppp",
				value:0,
				symbolSize:26
			},
			{
				name:"qqq",
				value:0,
				symbolSize:26
			}

		],
		links:[
			{
				source: "bbb",
				target: "aaa",
				lineStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				source: "aaa",
				target: "ccc"
			},
			{
				source: "aaa",
				target: "ddd"
			},
			{
				source: "aaa",
				target: "eee",
				lineStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			{
				source: "aaa",
				target: "fff"
			},
			{
				source: "bbb",
				target: "ggg"
			},
			{
				source: "bbb",
				target: "hhh"
			},
			{
				source: "bbb",
				target: "iii"
			},
			{
				source: "eee",
				target: "jjj"
			},
			{
				source: "eee",
				target: "kkk.exe",
				lineStyle:{
					normal:{
						color:"#c23531"
					}
				}
			},
			///////////////



			{
				source: "eee",
				target: "lll"
			},
			{
				source: "eee",
				target: "mmm"
			},
			{
				source: "eee",
				target: "nnn"
			},
			{
				source: "eee",
				target: "ooo"
			},
			//////////////
			{
				source: "eee",
				target: "ppp"
			},
			{
				source: "eee",
				target: "qqq"
			}
		]
	}]
}
