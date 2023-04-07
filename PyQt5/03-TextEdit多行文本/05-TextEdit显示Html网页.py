import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("显示Html")
        self.resize(900, 1000)
        self.text_edit()
        self.show()

    def text_edit(self):
        text_edit = QTextEdit(self)
        text_edit.resize(900, 1000)
        # text_edit.setStyleSheet("background_color:cyan;color:black;")
        text_edit.setHtml("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>【渭源天气预报】渭源天气预报一周,渭源天气预报15天,30天,今天,明天,7天,10天,未来渭源一周天气预报查询—天气网</title>
<meta name="keywords" content="渭源天气,渭源天气预报,渭源天气预报查询,定西渭源县天气预报,定西渭源县天气预报查询,渭源今日天气,渭源周末天气,渭源一周天气预报,渭源天气预报一周,天气预报查询一周,渭源天气预报10天,渭源天气预报查询15天, 渭源未来一周的天气预报,渭源天气情况,渭源40日天气预报,天气预报40天,渭源30日天气预报,天气预报30天">
<meta  name="description" content="天气网提供渭源天气预报15天,30天,今日天气,明天天气,渭源未来一周的天气预报,定西渭源县天气,渭源实时天气查询,渭源天气预报一周,7天,10天,40天的天气情况。旅游出行,从天气网开始！">
<meta http-equiv='mobile-agent' content='format=xhtml;url=https://m.tianqi.com/weiyuan/'>
<meta name="mobile-agent" content="format=html5;url=https://m.tianqi.com/weiyuan/"/>
<meta name="mobile-agent" content="format=xhtml;url=https://m.tianqi.com/weiyuan/"/>
 <!--<meta name="referrer" content="origin">-->
<link rel='canonical' href='https://www.tianqi.com/weiyuan/' >
<script>
	(function(){var d=navigator.userAgent.toLowerCase();var h=d.match(/ipad/i)=="ipad";var i=d.match(/iphone os/i)=="iphone os";var g=d.match(/midp/i)=="midp";var e=d.match(/rv:1.2.3.4/i)=="rv:1.2.3.4";var f=d.match(/ucweb/i)=="ucweb";var a=d.match(/android/i)=="android";var b=d.match(/windows ce/i)=="windows ce";var j=d.match(/windows mobile/i)=="windows mobile";var c=window.location.href;c=c.replace("www.tianqi.com","m.tianqi.com");c=c.replace("wannianli.tianqi.com","m.tianqi.com");if(h||i||g||e||f||a||b||j){c=c.replace("http://","https://");window.location.href=c}})();
</script>
	<!-- <script src="//static.tianqistatic.com/static/tianqi2018/js/_banner_news.js" type="text/javascript"></script> -->
<script type="text/javascript" src="//static.tianqistatic.com/static/tianqi2018/js/jQuery.1.8.2.min.js"></script>
<script type="text/javascript" src="//static.tianqistatic.com/static/tianqi2018/js/common.js"></script>
<script language="javascript" src="//static.tianqistatic.com/static/js/new_rili.js"></script>
<script type="text/javascript" src="//ip.tianqi.com/ipdb/"></script>
<script type="text/javascript" src="//static.tianqistatic.com/static/tianqi2018/js/tianqi.js?v=20220721"></script>
<link href="//static.tianqistatic.com/static/tianqi2018/css/news.css" rel="stylesheet" type="text/css">

<link href="//static.tianqistatic.com/static/tianqi2018/css/index.css" rel="stylesheet" type="text/css"/>

<script type="text/javascript">
var pagetype = 'cityindex';
var cityname = '渭源';
</script>
<script type="text/javascript" src="//static.tianqistatic.com/static/tianqi2018/js/jQselect.js"></script>
<!-- <script src="//static.tianqistatic.com/static/lvyou2018/js/ad_lvyou.js" type="text/javascript" charset="utf-8"></script> -->
</head>
<body>
	<style type="text/css">
	.hhx_midBox>a{
		display: block;
	}
	.roof{
		display: flex;
		align-items: center;
	}
	.roof>img{
		width: 15px;
		height: 15px;
	}
	.roof>p{
		margin-left: 8px;
		color: #666666;
	}
	.roof>p>span{
		margin-left: 3px;
		color: #999999;
	}

	/* 天气页面头部改版 */

.new_wea_icon{display: flex!important;align-items: center;width: 300px;margin-left: 40px; margin-top: 12px;}
.new_wea_icon a, .wx_gzh{
   display: flex;
   flex-direction: column;
   align-items: center;
   font-size: 14px;
   color: #666666;
   margin-right: 40px;
   position: relative;
   height: 64px;
   justify-content: flex-end;
}
.wx_gzh{
	margin-right: 0;
}
.new_wea_icon a p , .wx_gzh >p{
    margin-top: 14px;
	line-height: normal;
}

.wx_gzh .erweima_box{
    position: absolute;
    width: 140px;
    height: 140px;
    background: #FFFFFF;
    box-shadow: 0px 1px 9px 1px rgba(111, 112, 113, 0.2);
    border-radius: 4px;
    display: none;
    align-items: center;
    justify-content: center;
    top: 115%;
	z-index: 999;   
	flex-direction: column;
}
.wx_gzh .erweima_box img{
    width: 108px;
    height: 108px;
}
.wx_gzh .erweima_box  p{
    font-size: 12px;
    color: #999999;
    text-align: center;
	line-height: normal;
}
.wx_gzh .erweima_box::before{
    content: '';
    display: block;
    border-bottom:9px solid #ffffff;
    border-top:9px solid transparent;
    border-left:9px solid transparent;
    border-right:9px solid transparent;
    box-sizing: content-box;
    width: 0px;
    height: 0px;
    position: absolute;
    top: -16px;;
    right:60px;
}
.wx_gzh .erweima_box::after{
    content: '';
    display: block;
    border-bottom:9px solid #ffffff;
    border-top:9px solid transparent;
    border-left:9px solid transparent;
    border-right:9px solid transparent;
    box-sizing: content-box;
    width: 0px;
    height: 0px;
    position: absolute;
    top: -16px;;
    right:60px; 
}

</style>
<!-- 新增顶部 2018/6/1 -->
<div class="hhx_newheader">
    <div class="hhx_midBox">
		<!--<a href="/chinacity.html">-->
		<!--<div class="fl roof">-->
			<!--<img src="//static.tianqistatic.com/static/images/bianmin/dingwei.png">-->
			<!--<p>重庆<span>[切换城市]</span></p>-->
		<!--</div>-->
		<!--</a>-->
        <marquee direction="left" class="tit1 fl" style="width: 300px;">天气网提供全国国内城市天气预报，旅游景点天气预报，国际城市天气预报以及历史天气预报查询</marquee>
	    <div class="tit2 right" style="width: auto;">
            <ul>
                <li class="t1 hhx_aHoverBlue">
						<span class="hhx_appLoadSpan">
                            <a href="https://www.tianqi.com/jingdian.html" target="_blank">旅游景点</a> <i>|</i>
                            <a href="https://www.tianqi.com/meishi.html" target="_blank">美食</a><i>|</i>
                            <a href="https://www.tianqi.com/techan.html" target="_blank">特产</a><i>|</i>
                            <a href="https://www.tianqi.com/tag/" target="_blank">TAG标签</a><i>|</i>
							<a href="https://www.tianqi.com/bianmin/" target="_blank">便民信息</a> <i>|</i>
							<!-- <a href="" target="_blank">交通查询</a>-->
						</span>
                </li>
            </ul>
	    </div>
    	<div style="clear: both;"></div>
    </div>
</div>

<div class="tiaqni_header_box">
		<div class="tianqi_log_box">
			<a id="tq_logo" href="https://www.tianqi.com" target="_blank"> <img src="//static.tianqistatic.com/static/img/logo_210.png" alt="天气网"></a>
		</div>
		
		<div class="tianqi_top_search_box">		
			<select name="" value="">
				<option value="" selected = "selected" >天气</option>
			</select>
			<form id="index_serch" method="get" action="" name="index_serch" class="clearfix" onkeydown="if(event.keyCode==13)return false;">
                <input type="text" value="" id="serch_text" autocomplete="off" placeholder="输入中文/拼音、城市/景点名称"
                        name="keyword" style="color: rgb(153, 153, 153);"/>
                <button class="tianqi_search_btn" type="button"></button>
            </form>

			<div class="tianqi_weather_box new_wea_icon">
                 <a href="https://www.tianqi.com/alarmnews/" title="天气预警">
					 <img style="width: 28px;height: 27px;" src="//static.tianqistatic.com/static/tianqi2021/img/yujing.png" alt="">
					 <p>天气预警</p>
				 </a>
				 <a href="https://www.tianqi.com/plugin/" title="天气插件">
					<img style="width: 37px;height: 31px;" src="//static.tianqistatic.com/static/tianqi2021/img/wea.png" alt="">
					<p>天气插件</p>
				 </a>
				 <div class="wx_gzh">
					<img style="width: 25px;height: 24px;" src="//static.tianqistatic.com/static/tianqi2021/img/erweima.png" alt="">
					<p>微信公众号</p>

					<div class="erweima_box">
                         <img  src="//www.tianqi.com/static/wap2018/ico1/wxerweima.jpg" alt="">
						 <p>扫码随时看天气</p>
					</div>
				 </div>
			</div>
		</div>
</div>
<script>
    function getCookie(a){var b=a+"=";var c="";if(document.cookie.length>0){offset=document.cookie.lastIndexOf(b);if(offset!=-1){offset+=b.length;end=document.cookie.indexOf(";",offset);if(end==-1){end=document.cookie.length}c=unescape(document.cookie.substring(offset,end))}}return c};
    $(".tianqi_search_btn").on('click', function() {
        var city = $("#serch_text").val();
        if(!city || city=='输入中文/拼音、城市/景点名称'){
           alert('请输入搜索的城市');
        }else {
            $("#index_serch").submit();
        }

    });
    
	$('.wx_gzh').mouseover(function(){
		$('.erweima_box').css('display','flex')
	}).mouseout(function(){
		$('.erweima_box').css('display','none')
	})
</script>



<div style="clear: both;"></div>
<div class="tianqi_pub_nav_box">
	    <ul class="tianqi_nav_content_box">
		<li  ><a href="//www.tianqi.com" target="_blank" title="天气网">首页</a></li>
        <li class="target_ li_tianqi">
        	<a href="https://www.tianqi.com/chinacity.html" target="_blank" title="天气" class="tianqi_nav_tianqiblank" style="background-image: url(//static.tianqistatic.com/static/wap2018/ico1/arrow_down.png);">天气</a>      	    
        </li>
        <li  ><a href="https://www.tianqi.com/air/" title="空气质量" target="_blank">空气质量</a></li>
        <li class="target_ li_news" ><a href="https://www.tianqi.com/news/" title="天气新闻" target="_blank" style="background: url(//static.tianqistatic.com/static/wap2018/ico1/arrow_down.png) no-repeat 86% 50%">天气新闻</a></li>
        
        <li class="target_ li_life">
        	<a href="https://www.tianqi.com/toutiao/" title="天气生活" class="tianqi_nav_tianqiblank_life" target="_blank" style="background-image: url(//static.tianqistatic.com/static/wap2018/ico1/arrow_down.png);">天气生活</a>
        </li>
		<li class="target_ li_shipin">
			<a href="https://www.tianqi.com/video/" title="视频" target="_blank" style="background-image: url(//static.tianqistatic.com/static/wap2018/ico1/arrow_down.png);" class="tianqi_nav_tianqiblank">视频</a></li>
		<!-- <li class="target_ nav_jingdian">
			<a href="https://www.tianqi.com/jingdian.html" title="旅游景点" target="_blank" style="background-image: url(//static.tianqistatic.com/static/wap2018/ico1/arrow_down.png);" class="tianqi_nav_tianqiblank_jingdian">旅游景点</a>
		</li>
        <li ><a href="https://www.tianqi.com/meishi.html" title="美食" target="_blank">美食</a></li>
        <li ><a href="https://www.tianqi.com/techan.html" title="特产" target="_blank">特产</a></li> -->
        <li><a href="https://wannianli.tianqi.com/" title="万年历" target="_blank">万年历</a></li>   
    </ul>
    <!-- 二级导航 -->
    <!-- 天气 -->
	<div class="tianqi_nav_next_box tianqi_nav_next_box_tianqi" style="display: none;">
		<div class="tianqi_nav_hover_box clearfix">
			<a href="https://www.tianqi.com/chinacity.html" title="全国天气" target="_blank">全国天气</a>
			<a href="https://www.tianqi.com/worldcity.html" title="国际天气" target="_blank">国际天气</a>
			<a href="https://lishi.tianqi.com/" title="历史天气" target="_blank">历史天气</a>
			<a href="https://www.tianqi.com/qiwen/" title="气温查询" target="_blank">气温查询</a>
			<a href="https://www.tianqi.com/changshi/" title="天气常识" target="_blank">天气常识</a>
			<a href="https://tf.tianqi.com/" title="台风路径图" target="_blank">台风路径图</a>
		</div>
	</div>
	<!-- 新闻 -->
	<div class="tianqi_nav_next_box tianqi_nav_next_box_news" style="display: none;">
		<div class="tianqi_nav_hover_box clearfix">
			<a href="https://www.tianqi.com/tianqi/chinanews.html" title="天气资讯" target="_blank">天气资讯</a>
		</div>
	</div>
	<!-- 生活 -->
	<div class="tianqi_nav_next_box tianqi_nav_next_box_life" style="display: none;">
		<div class="tianqi_nav_hover_box clearfix" style="width: auto;padding-left: 420px;">
			<a href="https://www.tianqi.com/toutiao/" title="推荐" target="_blank">推荐</a>			
			<a href="https://www.tianqi.com/toutiao/hots/" title="热点" target="_blank">热点</a>
			<a href="https://www.tianqi.com/toutiao/shenghuo/" title="生活" target="_blank">生活</a>
			<a href="https://www.tianqi.com/toutiao/lvyou/" title="旅游" target="_blank">旅游</a>
			<a href="https://www.tianqi.com/toutiao/yangsheng/" title="养生" target="_blank">养生</a>
			<a href="https://www.tianqi.com/toutiao/haowu/" title="好物" target="_blank">好物</a>
			<a href="https://www.tianqi.com/toutiao/jiankang/" title="健康" target="_blank">健康</a>
			<a href="https://www.tianqi.com/toutiao/jujia/" title="居家" target="_blank">居家</a>
			<a href="https://www.tianqi.com/toutiao/wenhua/" title="城市文化" target="_blank">城市文化</a>
			<a href="https://www.tianqi.com/toutiao/keji/" title="科技" target="_blank">科技</a>
			<a href="https://www.tianqi.com/toutiao/meishi/" title="美食" target="_blank">美食</a>
			<a href="https://www.tianqi.com/toutiao/jiaoyu/" title="教育" target="_blank">教育</a>
			<a href="https://www.tianqi.com/toutiao/yingshi/" title="影视" target="_blank">影视</a>
			<a href="https://www.tianqi.com/toutiao/zhiwu/" title="植物" target="_blank">植物</a>
			<a href="https://www.tianqi.com/toutiao/ask/" title="问答" target="_blank">问答</a>
		</div>
	</div>

	<!-- 旅游景点 -->
	<!-- <div class="tianqi_nav_next_box tianqi_nav_box_jingdian"   style="display: none;">
		<div class="tianqi_nav_hover_box clearfix">
			<a href="https://www.tianqi.com/jingdian.html" title="景点天气" target="_blank">景点天气</a>
			<a href="https://www.tianqi.com/worldcity/jingdian.html" title="国际景点天气" target="_blank">国际景点天气</a>
			<a href="https://www.tianqi.com/huaxue.html" title="滑雪天气" target="_blank">滑雪天气</a>
			<a href="https://www.tianqi.com/jingdian/5a.html" title="5A级景点" target="_blank">5A级景点</a>
			<a href="https://www.tianqi.com/jingdian/4a.html" title="4A级景点" target="_blank">4A级景点</a>
			<a href="https://www.tianqi.com/jingdian/3a.html" title="3A级景点" target="_blank">3A级景点</a>
			<a href="https://www.tianqi.com/jingdian/2a.html" title="2A级景点" target="_blank">2A级景点</a>
			<a href="https://www.tianqi.com/jingdian/1a.html" title="1A级景点" target="_blank">1A级景点</a>
		</div>
	</div> -->

	<!--视频-->
	<div class="tianqi_nav_next_box tianqi_nav_box_shipin tianqi_nav_next_box_shipin"   style="display: none;">
		<div class="tianqi_nav_hover_box clearfix">
			<a href="https://www.tianqi.com/video/" title="推荐" target="_blank">推荐</a>			
			<a href="https://www.tianqi.com/video/tianqibaike/" title="天气百科" target="_blank">天气百科</a>
			<a href="https://www.tianqi.com/video/shuma/" title="数码百科" target="_blank">数码百科</a>
			<a href="https://www.tianqi.com/video/shenghuo/" title="生活常识" target="_blank">生活常识</a>
			<a href="https://www.tianqi.com/video/meishi/" title="美食" target="_blank">美食</a>

			<a href="https://www.tianqi.com/video/techan/" title="特产" target="_blank">特产</a>
			<a href="https://www.tianqi.com/video/jiemeng/" title="解梦" target="_blank">解梦</a>
			<a href="https://www.tianqi.com/video/xingzuo/" title="星座" target="_blank">星座</a>
		</div>
	</div>
</div>
<div class="weatherbox">
	<div class="wrap1100" >
		<div class="left">
			<dl class="weather_info">
							<dt><img src="https://content.pic.tianqistatic.com/content/img/202106/29/a8776bfbfb6d44f8.jpg" alt="" class="weaone_a"></dt>
							<dd class="name"><h1>渭源天气</h1><i><a href="/chinacity.html" title="渭源天气预报">[切换城市]</a></i></dd>
			<dd class="week">2022年08月16日　星期二　壬寅年七月十九 </dd>
			<dd class="weather">
				<i><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png" ></i>
				<p class="now"><b>25</b><i>℃</i></p>
				<span><b>多云</b>16 ~ 27℃</span>
			</dd>
			<dd class="shidu"><b>湿度：53%</b><b>风向：东南风 1级</b><b>紫外线：强</b></dd>
			<dd class="kongqi" ><h5 style="background-color:#79b800;">空气质量：优</h5><h6>PM: 9</h6><span>日出: 06:23<br />日落: 19:51</span></dd>
		<dl>
		</div>
		<div class="right">
    <div class="top">
                    <span class="choose_hour_week"><a class="active" href="/weiyuan/today/" title="渭源24小时天气预报"><h3>24小时天气</h3></a><a href="/weiyuan/7/" title="渭源一周天气预报"><h3>渭源一周天气</h3></a></span>
            <span><a href="/weiyuan/15/" title="渭源15天天气预报"><h3>渭源15天天气</h3></a><a href="/weiyuan/30/" title="渭源30天天气预报"><h3>渭源30天天气</h3></a></span>
        
    </div>
    <div>
        <div class="twty_hour">
            <div>
                <div class="day7">
                    <ul class="week">
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                            </ul>
                    <ul class="txt txt2">
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">阴</li>
                                            </ul>
                    <div class="zxt_shuju1" style="display: none;">
                        <ul>
                                                                <li class="w95"><span>25</span></li>
                                                                <li class="w95"><span>26</span></li>
                                                                <li class="w95"><span>26</span></li>
                                                                <li class="w95"><span>27</span></li>
                                                                <li class="w95"><span>25</span></li>
                                                                <li class="w95"><span>24</span></li>
                                                    </ul>
                    </div>
                    <canvas id="canvas_hour1"></canvas>
                    <ul class="txt">
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                            </ul>
                    <ul class="txt">
                                                        <li class="w95 mgtop5">1级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">4级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                            </ul>
                    <ul class="txt canvas_hour">
                                                        <li class="w95">14时</li>
                                                        <li class="w95">15时</li>
                                                        <li class="w95">16时</li>
                                                        <li class="w95">17时</li>
                                                        <li class="w95">18时</li>
                                                        <li class="w95">19时</li>
                                            </ul>
                </div>
                <div class="day7 hide">
                    <ul class="week">
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                            </ul>
                    <ul class="txt txt2">
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                            </ul>
                    <div class="zxt_shuju2" style="display: none;">
                        <ul>
                                                                <li class="w95"><span>24</span></li>
                                                                <li class="w95"><span>23</span></li>
                                                                <li class="w95"><span>22</span></li>
                                                                <li class="w95"><span>20</span></li>
                                                                <li class="w95"><span>18</span></li>
                                                                <li class="w95"><span>17</span></li>
                                                    </ul>
                    </div>
                    <canvas id="canvas_hour2"></canvas>
                    <ul class="txt">
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                            </ul>
                    <ul class="txt">
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">3级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                            </ul>
                    <ul class="txt canvas_hour">
                                                        <li class="w95">20时</li>
                                                        <li class="w95">21时</li>
                                                        <li class="w95">22时</li>
                                                        <li class="w95">23时</li>
                                                        <li class="w95">00时</li>
                                                        <li class="w95">01时</li>
                                            </ul>
                </div>
                <div class="day7 hide">
                    <ul class="week">
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                            </ul>
                    <ul class="txt txt2">
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                            </ul>
                    <div class="zxt_shuju3" style="display: none;">
                        <ul>
                                                                <li class="w95"><span>16</span></li>
                                                                <li class="w95"><span>15</span></li>
                                                                <li class="w95"><span>14</span></li>
                                                                <li class="w95"><span>14</span></li>
                                                                <li class="w95"><span>15</span></li>
                                                                <li class="w95"><span>15</span></li>
                                                    </ul>
                    </div>
                    <canvas id="canvas_hour3"></canvas>
                    <ul class="txt">
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                            </ul>
                    <ul class="txt">
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">1级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                            </ul>
                    <ul class="txt canvas_hour">
                                                        <li class="w95">02时</li>
                                                        <li class="w95">03时</li>
                                                        <li class="w95">04时</li>
                                                        <li class="w95">05时</li>
                                                        <li class="w95">06时</li>
                                                        <li class="w95">07时</li>
                                            </ul>
                </div>
                <div class="day7 hide">
                    <ul class="week">
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                                        <li class="w95"><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                            </ul>
                    <ul class="txt txt2">
                                                        <li class="w95">阴</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">多云</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                                        <li class="w95">阴</li>
                                            </ul>
                    <div class="zxt_shuju4" style="display: none;">
                        <ul>
                                                                <li class="w95"><span>13</span></li>
                                                                <li class="w95"><span>17</span></li>
                                                                <li class="w95"><span>18</span></li>
                                                                <li class="w95"><span>19</span></li>
                                                                <li class="w95"><span>20</span></li>
                                                                <li class="w95"><span>22</span></li>
                                                    </ul>
                    </div>
                    <canvas id="canvas_hour4"></canvas>
                    <ul class="txt">
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东南风</li>
                                                        <li class="w95">东风</li>
                                                        <li class="w95">东风</li>
                                                        <li class="w95">东风</li>
                                            </ul>
                    <ul class="txt">
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                                        <li class="w95 mgtop5">2级</li>
                                            </ul>
                    <ul class="txt canvas_hour">
                                                        <li class="w95">08时</li>
                                                        <li class="w95">09时</li>
                                                        <li class="w95">10时</li>
                                                        <li class="w95">11时</li>
                                                        <li class="w95">12时</li>
                                                        <li class="w95">13时</li>
                                            </ul>
                </div>
            </div>

            <img onclick="nextHour()" src="//static.tianqistatic.com/static/tianqi2021/img/arrowleft.png" alt="">
            <img onclick="nextHour('right')" src="//static.tianqistatic.com/static/tianqi2021/img/arrowright.png" alt="">
        </div>
        <div class="day7 hide twty_hour">
            <ul class="week">
                                        <li><b>08月16日</b><span>星期二</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                            <li><b>08月17日</b><span>星期三</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b7.png"></li>
                                            <li><b>08月18日</b><span>星期四</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b7.png"></li>
                                            <li><b>08月19日</b><span>星期五</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b2.png"></li>
                                            <li><b>08月20日</b><span>星期六</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b1.png"></li>
                                            <li><b>08月21日</b><span>星期日</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b7.png"></li>
                                            <li><b>08月22日</b><span>星期一</span><img src="//static.tianqistatic.com/static/wap2018/ico1/b8.png"></li>
                                </ul>
            <ul class="txt txt2">
                                        <li>多云</li>
                                            <li>小雨</li>
                                            <li>小雨</li>
                                            <li>阴</li>
                                            <li>多云</li>
                                            <li>小雨</li>
                                            <li>小雨转阴</li>
                                </ul>
            <div class="zxt_shuju" style="display: none;">
                <ul>
                                                <li><span>27</span><b>16</b></li>
                                                    <li><span>28</span><b>13</b></li>
                                                    <li><span>26</span><b>13</b></li>
                                                    <li><span>24</span><b>16</b></li>
                                                    <li><span>26</span><b>15</b></li>
                                                    <li><span>20</span><b>14</b></li>
                                                    <li><span>21</span><b>13</b></li>
                                        </ul>
            </div>
            <canvas id="canvas"></canvas>
            <script type="text/javascript" src="//static.tianqistatic.com/static/js/canvas.js"></script>
            <ul class="txt">
                                        <li>东南风</li>
                                            <li>东风</li>
                                            <li>西北风</li>
                                            <li>北风</li>
                                            <li>东南风</li>
                                            <li>东风</li>
                                            <li>西北风</li>
                                </ul>
        </div>
    </div>
</div>
	</div>
</div>
<div class="wrap1100 zhishubox">
	<div class="city_topbanner">
		<div class="wrapbox banner_top" style="width: 1024px; padding-top: 10px;">
			<script>toutiaotophenpin()</script>
		</div>
	</div>
</div>
<div class="clear15"></div>
<div class="wrap1100 mainbox">
	<div class="left">
				<div class="racitybox">
			<div class="tit02"><h2>渭源主要地区天气预报</h2></div>
			<div class="mainWeather">
				<ul class="raweather760">
												<li>
								<a href="/anding/" title="安定天气预报：小雨 16~32℃">
									<h5>安定</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b7.png"></i>
									<p><b>小雨</b>16 ~ <em>32</em>℃</p></a>
								<a href="/anding/15/" title="安定天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/tongwei/" title="通渭天气预报：多云 16~30℃">
									<h5>通渭</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i>
									<p><b>多云</b>16 ~ <em>30</em>℃</p></a>
								<a href="/tongwei/15/" title="通渭天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/longxi/" title="陇西天气预报：多云 18~31℃">
									<h5>陇西</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i>
									<p><b>多云</b>18 ~ <em>31</em>℃</p></a>
								<a href="/longxi/15/" title="陇西天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/weiyuan/" title="渭源天气预报：多云 19~28℃">
									<h5>渭源</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i>
									<p><b>多云</b>19 ~ <em>28</em>℃</p></a>
								<a href="/weiyuan/15/" title="渭源天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/lintao/" title="临洮天气预报：小雨 15~32℃">
									<h5>临洮</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b7.png"></i>
									<p><b>小雨</b>15 ~ <em>32</em>℃</p></a>
								<a href="/lintao/15/" title="临洮天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/zhangxian/" title="漳县天气预报：多云 24~32℃">
									<h5>漳县</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i>
									<p><b>多云</b>24 ~ <em>32</em>℃</p></a>
								<a href="/zhangxian/15/" title="漳县天气预报15天" class="d15" target="_blank">></a>
							</li>
														<li>
								<a href="/minxian/" title="岷县天气预报：多云 14~28℃">
									<h5>岷县</h5>
									<i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i>
									<p><b>多云</b>14 ~ <em>28</em>℃</p></a>
								<a href="/minxian/15/" title="岷县天气预报15天" class="d15" target="_blank">></a>
							</li>
												<li class="button_display">
						<div class="open_button">
							<div>展开<img src="//static.tianqistatic.com/static/tianqi2018/css/open.png"/></div>
						</div>
						<div class="take_upButton">
							<div>
								收起<img src="//static.tianqistatic.com/static/tianqi2018/css/close.png"/>
							</div>
						</div>
					</li>
				</ul>
			</div>
		</div>
			<div class="banner760 b760_page"><script type="text/javascript">read_760_page_01();</script></div>
					<div class="racitybox">
				<div class="tit02"><h2>渭源下辖乡镇天气预报</h2></div>
				<ul class="raweather760">
											<li><a href="/gansu-qiaoyuzhen/36447/" title="锹峪镇天气预报"><h5>锹峪镇</h5></a><a href="/gansu-qiaoyuzhen/36447/" title="锹峪镇天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-beizhaizhen/36448/" title="北寨镇天气预报"><h5>北寨镇</h5></a><a href="/gansu-beizhaizhen/36448/" title="北寨镇天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-lianfengzhen/36449/" title="莲峰镇天气预报"><h5>莲峰镇</h5></a><a href="/gansu-lianfengzhen/36449/" title="莲峰镇天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-wuzhuzhen/36450/" title="五竹镇天气预报"><h5>五竹镇</h5></a><a href="/gansu-wuzhuzhen/36450/" title="五竹镇天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-luyuanzhen/36451/" title="路园镇天气预报"><h5>路园镇</h5></a><a href="/gansu-luyuanzhen/36451/" title="路园镇天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-daanxiang/36452/" title="大安乡天气预报"><h5>大安乡</h5></a><a href="/gansu-daanxiang/36452/" title="大安乡天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-tianjiahexiang/36453/" title="田家河乡天气预报"><h5>田家河乡</h5></a><a href="/gansu-tianjiahexiang/36453/" title="田家河乡天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-qinqixiang/36454/" title="秦祁乡天气预报"><h5>秦祁乡</h5></a><a href="/gansu-qinqixiang/36454/" title="秦祁乡天气预报" class="d15" target="_blank">></a></li>
											<li><a href="/gansu-qingyuanzhen/36455/" title="清源镇天气预报"><h5>清源镇</h5></a><a href="/gansu-qingyuanzhen/36455/" title="清源镇天气预报" class="d15" target="_blank">></a></li>
										<li class="button_display">
						<div class="open_button">
							<div>展开<img src="//static.tianqistatic.com/static/tianqi2018/css/open.png"/></div>
						</div>
						<div class="take_upButton">
							<div>
								收起<img src="//static.tianqistatic.com/static/tianqi2018/css/close.png"/>
							</div>
						</div>
					</li>
				</ul>
			</div>
				<div class="clear5"></div>
				<!--<div class="clear5"></div>-->
		<div class="racitybox">
			<div class="tit02"><h2>渭源周边市县天气预报</h2></div>
			<ul class="raweather760">
				                        <li><a href="/dingxi/" title="定西天气预报：多云转阴 17~31℃"><h5>定西</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b2.png"></i><p><b>多云转阴</b>17 ~ <em>31</em>℃</p></a><a href="/dingxi/15/" title="定西天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/linxia/" title="临夏天气预报：多云 17~28℃"><h5>临夏</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>17 ~ <em>28</em>℃</p></a><a href="/linxia/15/" title="临夏天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/lanzhou/" title="兰州天气预报：多云 18~29℃"><h5>兰州</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>18 ~ <em>29</em>℃</p></a><a href="/lanzhou/15/" title="兰州天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/kezhou/" title="克州天气预报：多云转阴 21~33℃"><h5>克州</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b2.png"></i><p><b>多云转阴</b>21 ~ <em>33</em>℃</p></a><a href="/kezhou/15/" title="克州天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/gannan/" title="甘南天气预报：小雨 11~25℃"><h5>甘南</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b7.png"></i><p><b>小雨</b>11 ~ <em>25</em>℃</p></a><a href="/gannan/15/" title="甘南天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/tianshui/" title="天水天气预报：多云 22~32℃"><h5>天水</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>22 ~ <em>32</em>℃</p></a><a href="/tianshui/15/" title="天水天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/baiyin/" title="白银天气预报：晴 17~30℃"><h5>白银</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b0.png"></i><p><b>晴</b>17 ~ <em>30</em>℃</p></a><a href="/baiyin/15/" title="白银天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/longnan1/" title="陇南天气预报：多云 22~36℃"><h5>陇南</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>22 ~ <em>36</em>℃</p></a><a href="/longnan1/15/" title="陇南天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/huangnan/" title="黄南天气预报：小雨转阴 16~26℃"><h5>黄南</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b8.png"></i><p><b>小雨转阴</b>16 ~ <em>26</em>℃</p></a><a href="/huangnan/15/" title="黄南天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/guyuanguyuan/" title="固原天气预报：多云 18~27℃"><h5>固原</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>18 ~ <em>27</em>℃</p></a><a href="/guyuanguyuan/15/" title="固原天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/pingliang/" title="平凉天气预报：多云 19~31℃"><h5>平凉</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>19 ~ <em>31</em>℃</p></a><a href="/pingliang/15/" title="平凉天气预报15天" class="d15" target="_blank">></a></li>
				                        <li><a href="/haidong/" title="海东天气预报：晴 12~25℃"><h5>海东</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b0.png"></i><p><b>晴</b>12 ~ <em>25</em>℃</p></a><a href="/haidong/15/" title="海东天气预报15天" class="d15" target="_blank">></a></li>
								<li class="button_display">
					<div class="open_button">
						<div>展开<img src="//static.tianqistatic.com/static/tianqi2018/css/open.png"/></div>
					</div>
					<div class="take_upButton">
						<div>
							收起<img src="//static.tianqistatic.com/static/tianqi2018/css/close.png"/>
						</div>
					</div>
				</li>
			</ul>
		</div>
				<div class="clear5"></div>
					<div class="clear5"></div>
			<div class="racitybox ">
				<div class="tit02"><h2>甘肃主要城市天气预报</h2></div>
				<ul class="raweather760">
											<li><a href="/lanzhou/" title="兰州天气预报：多云 16~29℃"><h5>兰州</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>16 ~ <em>29</em>℃</p></a><a href="/lanzhou/15/" title="兰州天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/dingxi/" title="定西天气预报：多云转阴 17~31℃"><h5>定西</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b2.png"></i><p><b>多云转阴</b>17 ~ <em>31</em>℃</p></a><a href="/dingxi/15/" title="定西天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/pingliang/" title="平凉天气预报：多云 19~31℃"><h5>平凉</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>19 ~ <em>31</em>℃</p></a><a href="/pingliang/15/" title="平凉天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/qingyang/" title="庆阳天气预报：多云 21~27℃"><h5>庆阳</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>21 ~ <em>27</em>℃</p></a><a href="/qingyang/15/" title="庆阳天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/wuwei/" title="武威天气预报：晴 19~30℃"><h5>武威</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b0.png"></i><p><b>晴</b>19 ~ <em>30</em>℃</p></a><a href="/wuwei/15/" title="武威天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/jinchang/" title="金昌天气预报：多云 17~30℃"><h5>金昌</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>17 ~ <em>30</em>℃</p></a><a href="/jinchang/15/" title="金昌天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/zhangye/" title="张掖天气预报：多云 18~30℃"><h5>张掖</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>18 ~ <em>30</em>℃</p></a><a href="/zhangye/15/" title="张掖天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/jiuquan/" title="酒泉天气预报：多云 13~29℃"><h5>酒泉</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>13 ~ <em>29</em>℃</p></a><a href="/jiuquan/15/" title="酒泉天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/tianshui/" title="天水天气预报：多云 22~32℃"><h5>天水</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>22 ~ <em>32</em>℃</p></a><a href="/tianshui/15/" title="天水天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/longnan1/" title="陇南天气预报：多云 22~36℃"><h5>陇南</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>22 ~ <em>36</em>℃</p></a><a href="/longnan1/15/" title="陇南天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/linxia/" title="临夏天气预报：多云 15~29℃"><h5>临夏</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>15 ~ <em>29</em>℃</p></a><a href="/linxia/15/" title="临夏天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/gannan/" title="甘南天气预报：小雨 11~25℃"><h5>甘南</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b7.png"></i><p><b>小雨</b>11 ~ <em>25</em>℃</p></a><a href="/gannan/15/" title="甘南天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/baiyin/" title="白银天气预报：晴 17~30℃"><h5>白银</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b0.png"></i><p><b>晴</b>17 ~ <em>30</em>℃</p></a><a href="/baiyin/15/" title="白银天气预报15天" class="d15" target="_blank">></a></li>
												<li><a href="/jiayuguan/" title="嘉峪关天气预报：多云 14~29℃"><h5>嘉峪关</h5><i><img src="//static.tianqistatic.com/static/tianqi2018/ico2/b1.png"></i><p><b>多云</b>14 ~ <em>29</em>℃</p></a><a href="/jiayuguan/15/" title="嘉峪关天气预报15天" class="d15" target="_blank">></a></li>
											<li class="button_display">
						<div class="open_button">
							<div>展开<img src="//static.tianqistatic.com/static/tianqi2018/css/open.png"/></div>
						</div>
						<div class="take_upButton">
							<div>
								收起<img src="//static.tianqistatic.com/static/tianqi2018/css/close.png"/>
							</div>
						</div>
					</li>
				</ul>
			</div>
				<div class="clear5"></div>
		<div class="banner760 b760_04"><script>banner_760_04();</script></div>
		<div class="clear20"></div>
		<div class="hhxCulture clearfix">
			<div class="tit02line paddnone" data-type ="life">
				<h2>天气生活</h2>
				<div class="min_tit new_wea_life_title">
					<ul>
						<li><a>精选</a></li>
						<li><a href="https://www.cnys.com/article/list_1_1.html">养生</a></li>
						<li><a href="/toutiao/shenghuo/">生活</a></li>
						<li><a href="/toutiao/meishi/">美食</a></li>
						<li><a href="/toutiao/lvyou/">旅游</a></li>
						<li><a href="/toutiao/keji/">科技</a></li>
						<li><a href="/toutiao/jujia/">居家</a></li>
						<li><a href="http://ask.tianqi.com/pc/">问答</a></li>
						<li><a href="/toutiao/haowu/">好物</a></li>
						<li><a href="/toutiao/techan/">特产</a></li>
					</ul>
				</div>
				<a class="Newmore" href="/toutiao/" target="_blank" >更多 <font>>></font></a>
			</div>

			<!-- 天气生活的内容s -->
			<div class="weaLife_Content">
				<!--生活-->
					<div class="culList weaLife_Content_m select-content">
					<ul>
						<script type="text/javascript">toutiaolist();</script>
						<script type="text/javascript">toutiaolist();</script></if>
													<li>
								<a href="/toutiao/read/87001.html" target="_blank" class="clearfix" title="丽江最佳旅游时间 丽江适合什么时候去">
								<span><img class="fl" src="http://content.pic.tianqistatic.com/content/toutiao/lvyou/img/201910/30/5abba24778a14ddc.jpg" alt="丽江最佳旅游时间 丽江适合什么时候去" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>丽江最佳旅游时间 丽江适合什么时候去</h3>
									<p>2022-08-12 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/read/190174.html" target="_blank" class="clearfix" title="流浪伤感的句子 流浪街头的伤感说说">
								<span><img class="fl" src="http://content.pic.tianqistatic.com/content/images/202206/22/c4d51b88482c8c96.jpg" alt="流浪伤感的句子 流浪街头的伤感说说" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>流浪伤感的句子 流浪街头的伤感说说</h3>
									<p>2022-08-15 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/meishi/68653.html" target="_blank" class="clearfix" title="鲍鱼怎么做好吃 鲍鱼的家常做法">
								<span><img class="fl" src="https://content.pic.tianqistatic.com/content/toutiao/meishi/img/202004/29/38c8d582f8e47b25.jpg" alt="鲍鱼怎么做好吃 鲍鱼的家常做法" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>鲍鱼怎么做好吃 鲍鱼的家常做法</h3>
									<p>2022-08-10 </p>
								</div>
								</a>
							</li>
							<script type="text/javascript">toutiaolist();</script>							<li>
								<a href="https://www.cnys.com/article/79067.html?rf=tq" target="_blank" class="clearfix" title="维生素c的作用和功效 吃维生素c有什么好处">
								<span><img class="fl" src="http://pic.cnys.com/content/20210428/858eb968164e5debf6095a257541c2a4.jpg" alt="维生素c的作用和功效 吃维生素c有什么好处" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>维生素c的作用和功效 吃维生素c有什么好处</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/keji/49457.html" target="_blank" class="clearfix" title="如何破解wifi密码 wifi密码怎么简单破解">
								<span><img class="fl" src="https://content.pic.tianqistatic.com/content/20190410/0fa94469406d2a6f0ae15ae0325d7739.jpg" alt="如何破解wifi密码 wifi密码怎么简单破解" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>如何破解wifi密码 wifi密码怎么简单破解</h3>
									<p>2022-08-09 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="https://www.cnys.com/yangshengzixun/6961.html?rf=tq" target="_blank" class="clearfix" title="发物有哪些食物 发物是指哪些食物">
								<span><img class="fl" src="http://pic.cnys.com/content/20210428/3e4d86526d8e096bc676209c482a30f5.jpg" alt="发物有哪些食物 发物是指哪些食物" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>发物有哪些食物 发物是指哪些食物</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
							<script type="text/javascript">toutiaolist();</script>							<li>
								<a href="https://www.cnys.com/zhuanjiawenzhang/31401.html?rf=tq" target="_blank" class="clearfix" title="接种新冠疫苗后的注意事项及禁忌">
								<span><img class="fl" src="http://pic.cnys.com/content/20210428/b0a74cb4ee5cd79b8b20d253c2745000.jpg" alt="接种新冠疫苗后的注意事项及禁忌" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>接种新冠疫苗后的注意事项及禁忌</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/read/190177.html" target="_blank" class="clearfix" title="来一句特别励志的句子 励志语录经典短句">
								<span><img class="fl" src="http://tqjimg.tianqistatic.com/toutiao/shenghuo/img/202205/26/0d2adf6fbe810d8a.jpg" alt="来一句特别励志的句子 励志语录经典短句" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>来一句特别励志的句子 励志语录经典短句</h3>
									<p>2022-08-15 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/read/190231.html" target="_blank" class="clearfix" title="广东大叶青属于什么茶 大叶青茶相关介绍">
								<span><img class="fl" src="http://picview.iituku.com/bqtuku/202208/15/0d41cb63a1d390bf.jpg" alt="广东大叶青属于什么茶 大叶青茶相关介绍" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>广东大叶青属于什么茶 大叶青茶相关介绍</h3>
									<p>2022-08-15 </p>
								</div>
								</a>
							</li>
							<script type="text/javascript">toutiaolist();</script>							<li>
								<a href="/toutiao/meishi/62763.html" target="_blank" class="clearfix" title="毛豆煮多久 毛豆煮多长时间">
								<span><img class="fl" src="https://content.pic.tianqistatic.com/content/toutiao/meishi/img/201911/28/3b57ffff9777ce39.jpg" alt="毛豆煮多久 毛豆煮多长时间" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>毛豆煮多久 毛豆煮多长时间</h3>
									<p>2022-08-09 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/keji/60452.html" target="_blank" class="clearfix" title="cpu是什么 cpu功能是什么">
								<span><img class="fl" src="https://content.pic.tianqistatic.com/content/toutiao/keji/img/201910/25/e4d0998c5c8b2742.jpg" alt="cpu是什么 cpu功能是什么" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>cpu是什么 cpu功能是什么</h3>
									<p>2022-06-07 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/read/74186.html" target="_blank" class="clearfix" title="峨眉山看云海什么时候最佳 峨眉山什么时候适合看云海">
								<span><img class="fl" src="http://content.pic.tianqistatic.com/content/toutiao/shenghuo/images/202004/27/017672062ab0f8d6.jpg" alt="峨眉山看云海什么时候最佳 峨眉山什么时候适合看云海" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>峨眉山看云海什么时候最佳 峨眉山什么时候适合看云海</h3>
									<p>2022-08-10 </p>
								</div>
								</a>
							</li>
							<script type="text/javascript">toutiaolist();</script>							<li>
								<a href="https://www.cnys.com/yangshengzixun/18705.html?rf=tq" target="_blank" class="clearfix" title="怀孕前三个月禁忌食物 怀孕前三个月饮食禁忌">
								<span><img class="fl" src="http://pic.cnys.com/content/20210428/219d514b8fccea6cf7b8af8973b9c3bb.jpg" alt="怀孕前三个月禁忌食物 怀孕前三个月饮食禁忌" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>怀孕前三个月禁忌食物 怀孕前三个月饮食禁忌</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="/toutiao/read/166704.html" target="_blank" class="clearfix" title="农历是阴历还是阳历 农历是指阴历还是阳历">
								<span><img class="fl" src="http://tqjimg.tianqistatic.com/toutiao/img/202105/29/dde4c817469c2d6e.jpg" alt="农历是阴历还是阳历 农历是指阴历还是阳历" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>农历是阴历还是阳历 农历是指阴历还是阳历</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
														<li>
								<a href="https://www.cnys.com/article/86675.html?rf=tq" target="_blank" class="clearfix" title="馒头的热量 馒头的热量是多少大卡">
								<span><img class="fl" src="http://pic.cnys.com/content/20210428/97a19319ba2003c3be426bbbbbaccc1e.jpg" alt="馒头的热量 馒头的热量是多少大卡" onerror="nofind(this)" /></span>
								<div class="fr">
									<h3>馒头的热量 馒头的热量是多少大卡</h3>
									<p>2022-08-16 </p>
								</div>
								</a>
							</li>
							<script type="text/javascript">toutiaolist();</script>					</ul>
			</div>
		</div>
		<!--推荐-->
	</div>
	<div class="clear10"></div>
	<div class="banner760"><script type="text/javascript">read_760_01();</script></div>
	<div class="clear5"></div>
					<div class="racitybox">
			<div class="tit02"><h2>城市文化</h2><a class="Newmore" href="/toutiao/wenhua_weiyuan/" target="_blank">更多 <font>&gt;&gt;</font></a></div>
			<div class="city_culture">
				<ul>
											<li><a href="/toutiao/wenhua/11695.html" target="_blank" title="崆峒山在哪里">崆峒山在哪里</a></li>
											<li><a href="/toutiao/wenhua/11694.html" target="_blank" title="平凉市属于哪个省">平凉市属于哪个省</a></li>
											<li><a href="/toutiao/wenhua/11687.html" target="_blank" title="嘉峪关门票多少钱一张">嘉峪关门票多少钱一张</a></li>
											<li><a href="/toutiao/wenhua/11686.html" target="_blank" title="嘉峪关旅游景点介绍">嘉峪关旅游景点介绍</a></li>
											<li><a href="/toutiao/wenhua/11678.html" target="_blank" title="甘肃陇南有什么特产">甘肃陇南有什么特产</a></li>
											<li><a href="/toutiao/wenhua/11677.html" target="_blank" title="陇南旅游景区有哪些">陇南旅游景区有哪些</a></li>
											<li><a href="/toutiao/wenhua/11676.html" target="_blank" title="陇南是哪个省的城市">陇南是哪个省的城市</a></li>
											<li><a href="/toutiao/wenhua/11669.html" target="_blank" title="天水旅游必去景点">天水旅游必去景点</a></li>
											<li><a href="/toutiao/wenhua/11668.html" target="_blank" title="南郭寺在哪里">南郭寺在哪里</a></li>
											<li><a href="/toutiao/wenhua/11667.html" target="_blank" title="天水是哪个省的城市">天水是哪个省的城市</a></li>
									</ul>
			</div>
		</div>
					<div class="clear5"></div>

		<div class="racitybox">
			<div class="tit02"><h3>渭源周边资讯</h3></div>
			<div class="banner760 b760_04"><script>banner_760_04();</script></div>
			<ul class="toutiao760b">
				<li><a href="/toutiao/read/87967.html" title="定西有哪些可以带走的特产 甘肃定西特产" target="_blank">定西有哪些可以带走的特产 甘肃定西特产</a></li><li><a href="/toutiao/read/87461.html" title="定西有哪些特产 甘肃定西特产" target="_blank">定西有哪些特产 甘肃定西特产</a></li><li><a href="/toutiao/read/87456.html" title="通渭有哪些特产 甘肃通渭特产" target="_blank">通渭有哪些特产 甘肃通渭特产</a></li><li><a href="/toutiao/read/83815.html" title="定西特产有哪些 定西有哪些特产" target="_blank">定西特产有哪些 定西有哪些特产</a></li><li><a href="/toutiao/read/83807.html" title="通渭特产有哪些 通渭有哪些特产" target="_blank">通渭特产有哪些 通渭有哪些特产</a></li><li><a href="/toutiao/read/60218.html" title="定西特色小吃有哪些 甘肃定西特产" target="_blank">定西特色小吃有哪些 甘肃定西特产</a></li><li><a href="/toutiao/read/60211.html" title="通渭特色小吃有哪些 甘肃通渭特产" target="_blank">通渭特色小吃有哪些 甘肃通渭特产</a></li><li><a href="/toutiao/read/190265.html" title="重庆电子护照办理常见问题 重庆电子护照办理常见问题有哪些" target="_blank">重庆电子护照办理常见问题 重庆电子护照办理常见问题有哪些</a></li><div class="clear5"></div><li><a href="/toutiao/read/190264.html" title="外地户口在重庆办理护照需要哪些材料 外地户口在重庆办理护照需要的材料" target="_blank">外地户口在重庆办理护照需要哪些材料 外地户口在重庆办理护照需要的材料</a></li><li><a href="/toutiao/read/190263.html" title="重庆养老保险怎么查 重庆养老保险查询方法有哪些" target="_blank">重庆养老保险怎么查 重庆养老保险查询方法有哪些</a></li><li><a href="/toutiao/read/190262.html" title="重庆南坪在哪里办护照 重庆南坪护照办理地点" target="_blank">重庆南坪在哪里办护照 重庆南坪护照办理地点</a></li><li><a href="/toutiao/read/190261.html" title="养老保险有几种 养老保险缴满15年就不用再缴了吗" target="_blank">养老保险有几种 养老保险缴满15年就不用再缴了吗</a></li><li><a href="/toutiao/read/190260.html" title="重庆居住证持有人办理护照申请指南 重庆居住证持有人办理护照申请材料" target="_blank">重庆居住证持有人办理护照申请指南 重庆居住证持有人办理护照申请材料</a></li><li><a href="/toutiao/read/190259.html" title="在重庆没工作一次性买15年养老保险可以吗 重庆城乡居民养老保险必须交15年吗" target="_blank">在重庆没工作一次性买15年养老保险可以吗 重庆城乡居民养老保险必须交15年吗</a></li><li><a href="/toutiao/read/190258.html" title="重庆办护照需要现金吗 重庆办护照需不需要现金" target="_blank">重庆办护照需要现金吗 重庆办护照需不需要现金</a></li><li><a href="/toutiao/read/190257.html" title="重庆主城护照办理所需资料 重庆主城护照办理所需资料有哪些" target="_blank">重庆主城护照办理所需资料 重庆主城护照办理所需资料有哪些</a></li><div class="clear5"></div><div class="clear5"></div>			</ul>
		</div>
		<div class="clear5"></div>
	<div class="racitybox">
		<div class="tit02line" data-type="life"><h2>渭源天气预报资讯</h2><a class="Newmore" href="/tianqi/weiyuan/" target="_blank">更多 <font>&gt;&gt;</font></a></div>
		<div class="banner760 b760_04"><script>banner_760_04();</script></div>
		<ul class="toutiao760b">
						<li><a href="/tianqi/weiyuan/202208.html" title="2022年08月 渭源天气" target="_blank">2022年08月 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220816.html" title="2022年08月16日 渭源天气" target="_blank">2022年08月16日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220815.html" title="2022年08月15日 渭源天气" target="_blank">2022年08月15日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220814.html" title="2022年08月14日 渭源天气" target="_blank">2022年08月14日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220813.html" title="2022年08月13日 渭源天气" target="_blank">2022年08月13日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220812.html" title="2022年08月12日 渭源天气" target="_blank">2022年08月12日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220811.html" title="2022年08月11日 渭源天气" target="_blank">2022年08月11日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220810.html" title="2022年08月10日 渭源天气" target="_blank">2022年08月10日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220809.html" title="2022年08月09日 渭源天气" target="_blank">2022年08月09日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220808.html" title="2022年08月08日 渭源天气" target="_blank">2022年08月08日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220807.html" title="2022年08月07日 渭源天气" target="_blank">2022年08月07日 渭源天气</a></li>
							<li><a href="/tianqi/weiyuan/20220806.html" title="2022年08月06日 渭源天气" target="_blank">2022年08月06日 渭源天气</a></li>
					</ul>
	</div>
		</div>
	<div class="right">
		<div class="clear40"></div>
		<!-- 精选问答 -->
				<!--热门排行 -->
		<div class="banner300" id="dsp_box" style="border: 1px solid #eeeeee;"><script>banner_300_0902();</script></div>
		<div class="tit03"><span><a href="/weiyuan/life.html">更多+</a></span><h3>渭源今日生活指数</h3></div>
		<div class="clear2"></div>
		<div class="weather_life300">				<ul>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_yu.png"></i><b>带伞</b><a href="/weiyuan/life.html"><p>无需</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_xc.png"></i><b>洗车</b><a href="/weiyuan/life.html"><p>较不适宜</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_uv.png"></i><b>紫外线</b><a href="/weiyuan/life.html"><p>弱</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_ag.png"></i><b>过敏</b><a href="/weiyuan/life.html"><p>极易发</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_dy.png"></i><b>钓鱼</b><a href="/weiyuan/life.html"><p>一般般</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index.png"></i><b>穿衣</b><a href="/weiyuan/life.html"><p>热</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_tr.png"></i><b>旅行</b><a href="/weiyuan/life.html"><p>不适宜</p></a></li>
							<li><i><img src="//static.tianqistatic.com/static/wap2018/images/cai_index_ls.png"></i><b>晾晒</b><a href="/weiyuan/life.html"><p>不适宜</p></a></li>
					</ul>
		</div>

		<!-- 邮编查询 -->
				<div class="clear10"></div>
		<div class="banner300 b300_02"><script>banner_300_02();</script></div>
		<div class="clear20"></div>
		<!-- 精选问答 -->
		<div class="box300">
			<div class="all_r300box clearfix">
				<div class="tit05"><h3>精选问答</h3><a class="Newmore" href="https://ask.tianqi.com/p/" target="_blank" >更多 <font>>></font></a></div>
				<div class="clear5"></div>
				<ul class="news_listinfo">
											<li><a href="https://ask.tianqi.com/p-jinrong/fXzmgWaWk.html?rf=tq" title="农业银行房贷多久放款" target="_blank"><h3 class="diandian"><span>• </span>农业银行房贷多久放款</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fxxQgUjWP.html?rf=tq" title="央行LPR是什么意思" target="_blank"><h3 class="diandian"><span>• </span>央行LPR是什么意思</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fxJzgUWae.html?rf=tq" title="创业板核准制和注册制的区别" target="_blank"><h3 class="diandian"><span>• </span>创业板核准制和注册制的区别</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fxNSgPajj.html?rf=tq" title="花呗收钱要手续费吗" target="_blank"><h3 class="diandian"><span>• </span>花呗收钱要手续费吗</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fXXigeqkW.html?rf=tq" title="外汇交易平台的区别和种类是什么" target="_blank"><h3 class="diandian"><span>• </span>外汇交易平台的区别和种类是什么</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fmxigqWUV.html?rf=tq" title="慢性肾炎能不能投保重疾险" target="_blank"><h3 class="diandian"><span>• </span>慢性肾炎能不能投保重疾险</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fQyNgWWVg.html?rf=tq" title="基金赎回怎么算收益" target="_blank"><h3 class="diandian"><span>• </span>基金赎回怎么算收益</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fNSyggWej.html?rf=tq" title="我来贷查征信吗" target="_blank"><h3 class="diandian"><span>• </span>我来贷查征信吗</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fSxNgPjea.html?rf=tq" title="股票代码有个融字是什么意思" target="_blank"><h3 class="diandian"><span>• </span>股票代码有个融字是什么意思</h3></a></li>
												<li><a href="https://ask.tianqi.com/p-jinrong/fmNmggqje.html?rf=tq" title="在借呗借钱影响买房吗" target="_blank"><h3 class="diandian"><span>• </span>在借呗借钱影响买房吗</h3></a></li>
										</ul>
			</div>
		</div>




		<div class="clear10"></div>
		<!-- _day_right-->
		<div class="banner300 b300_01"><script>banner_300_01();</script></div>
		<div class="banner300 b300_03"><script>banner_300_03();</script></div>
		<div class="banner300 b300_04"><script>banner_300_04();</script></div>
		<div class="banner300 b300_10"><script>banner_300_11();</script></div>
		<div class="clear5"></div>
		<div class="banner300 b300_07"><script>banner_300_07();</script></div>
		<div class="banner300 b300_08"><script>banner_300_08();</script></div>
		<div class="banner300 b300_09"><script>banner_300_09();</script></div>
		<div class="clear10"></div>

        <!-- 养生食谱 -->
         <div class="yangsheng_shipu_right">
              <div class="same_right_title"><span>养生食谱</span> <a href="https://www.renrenshipu.com/caipu/index_1001.html">更多>></a></div>
			  <div class="yangsheng_shipu_list">
				  					  <a class="hottuijian" href="https://www.renrenshipu.com/caipu/video/5169.html?rf=tq" title="啤酒鸭" target="_blank">
						  <img src="http://videos.renrenshipu.com/caipu/20210408/203b63aa45da98fb.jpg?x-oss-process=style/shipu_250" alt="啤酒鸭">
						  <p class="tuijiantitle">啤酒鸭</p>
					  </a>
				  					  <a class="hottuijian" href="https://www.renrenshipu.com/caipu/video/4896.html?rf=tq" title="椒盐手工豆腐" target="_blank">
						  <img src="http://videos.renrenshipu.com/caipu/20210408/0bcbedafd4a9fa5f.jpg?x-oss-process=style/shipu_250" alt="椒盐手工豆腐">
						  <p class="tuijiantitle">椒盐手工豆腐</p>
					  </a>
				  					  <a class="hottuijian" href="https://www.renrenshipu.com/caipu/video/849.html?rf=tq" title="芹菜金针菇" target="_blank">
						  <img src="http://videos.renrenshipu.com/caipu/20210408/66938a31f0e26c19.jpg?x-oss-process=style/shipu_250" alt="芹菜金针菇">
						  <p class="tuijiantitle">芹菜金针菇</p>
					  </a>
				  					  <a class="hottuijian" href="https://www.renrenshipu.com/caipu/video/4086.html?rf=tq" title="花菜炒肉" target="_blank">
						  <img src="http://videos.renrenshipu.com/caipu/20210409/67132ec8c87512fc.jpg?x-oss-process=style/shipu_250" alt="花菜炒肉">
						  <p class="tuijiantitle">花菜炒肉</p>
					  </a>
				  			</div>
		 </div>
		 <div class="clear10"></div>
		 <!-- 十大景点天气 -->
				 <div class="box300">
			<div class="all_r300box clearfix">
				<div class="tit05"><h3>渭源十大景点天气</h3></div>
				<div class="clear5"></div>
				<ul class="news_listinfo">
											<li><a href="/weiyuan/jingdian/8450.html" title="七一冰川" target="_blank"><h3 class="diandian"><span>• </span>七一冰川</h3></a></li>
											<li><a href="/weiyuan/jingdian/8451.html" title="西部明珠气象塔" target="_blank"><h3 class="diandian"><span>• </span>西部明珠气象塔</h3></a></li>
											<li><a href="/weiyuan/jingdian/17574.html" title="长城博物馆" target="_blank"><h3 class="diandian"><span>• </span>长城博物馆</h3></a></li>
											<li><a href="/weiyuan/jingdian/17596.html" title="魏晋壁画墓" target="_blank"><h3 class="diandian"><span>• </span>魏晋壁画墓</h3></a></li>
											<li><a href="/weiyuan/jingdian/17613.html" title="“七一”冰川" target="_blank"><h3 class="diandian"><span>• </span>“七一”冰川</h3></a></li>
											<li><a href="/weiyuan/jingdian/17646.html" title="悬壁长城" target="_blank"><h3 class="diandian"><span>• </span>悬壁长城</h3></a></li>
											<li><a href="/weiyuan/jingdian/23185.html" title="城楼" target="_blank"><h3 class="diandian"><span>• </span>城楼</h3></a></li>
											<li><a href="/weiyuan/jingdian/23186.html" title="关城" target="_blank"><h3 class="diandian"><span>• </span>关城</h3></a></li>
											<li><a href="/weiyuan/jingdian/23187.html" title="新城魏晋壁画墓" target="_blank"><h3 class="diandian"><span>• </span>新城魏晋壁画墓</h3></a></li>
											<li><a href="/weiyuan/jingdian/23189.html" title="紫轩葡萄酒庄园" target="_blank"><h3 class="diandian"><span>• </span>紫轩葡萄酒庄园</h3></a></li>
									</ul>
			</div>
		</div>
				<div class="clear10"></div>
		<!-- 十大美食 -->
				<div class="box300">
			<div class="all_r300box clearfix">
				<div class="tit05"><h3>渭源十大美食排行</h3></div>
				<div class="clear5"></div>
				<ul class="news_listinfo paihang_good_food">
											<li><a href="/meishi/2725.html" title="靖远羊羔肉" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">1</span>靖远羊羔肉</h3></a></li>
											<li><a href="/meishi/408.html" title="藏包子" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">2</span>藏包子</h3></a></li>
											<li><a href="/meishi/2729.html" title="河州面片" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">3</span>河州面片</h3></a></li>
											<li><a href="/meishi/2727.html" title="呱呱" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">4</span>呱呱</h3></a></li>
											<li><a href="/meishi/2715.html" title="羊杂碎汤" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">5</span>羊杂碎汤</h3></a></li>
											<li><a href="/meishi/1360.html" title="臊子面" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">6</span>臊子面</h3></a></li>
											<li><a href="/meishi/3258.html" title="荞剁面" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">7</span>荞剁面</h3></a></li>
											<li><a href="/meishi/2730.html" title="泾川罐罐蒸馍" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">8</span>泾川罐罐蒸馍</h3></a></li>
											<li><a href="/meishi/2718.html" title="麻腐包" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">9</span>麻腐包</h3></a></li>
											<li><a href="/meishi/2720.html" title="糖酥饼" target="_blank"><h3 class="diandian"><span class="paihang_xuhao">10</span>糖酥饼</h3></a></li>
									</ul>
			</div>
		</div>
				<div class="clear10"></div>
		<div class="box300">
			<div class="all_r300box clearfix">
				<div class="tit05"><h3>最新天气资讯</h3><a class="Newmore" href="//www.tianqi.com/news/" target="_blank" >更多 <font>>></font></a></div>
				<div class="clear5"></div>
				<ul class="news_listinfo new_news_zixun">
												<li >
							<a class="left_img_style" href="/news/314680.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/6D9Rrfrajc5Ou3Yfhk6gDHBB.jpg" alt="">
								<div>
									<h3>西藏那曲市安多县接连发生两次地震 最强4.3级地震</h3>
									<p class="duodiandian">据中国地震台网发布地震最新消息，今天（16日）上午西藏那曲市安多县接连发生两次地震，最强4.3级地震。具体情况为10时16分的3.0级地震和10时22分的4.3级地震，震源深度均是10千米。实际上，昨天（15日）西藏那曲市安多县发生过一次发生4.1级地震。</p>
								</div>
							</a>
							<a href="/news/314680.html" title="西藏那曲市安多县接连发生两次地震 最强4.3级地震" target="_blank"><h3>西藏那曲市安多县接连发生两次地震 最强4.3级地震</h3></a>
						</li>
													<li class="active">
							<a class="left_img_style" href="/news/314679.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/Dll0HYGIUI05iBJp94m2rT8W.jpg" alt="">
								<div>
									<h3>今江西高温依然 南昌干旱橙色预警生效中</h3>
									<p class="duodiandian">据最新预报显示，今江西高温依然，尤其北部和中部，最高气温可达40℃，南部最高气温达38℃，而不管是哪里，天气都非常炎热，大家要注意防暑降温。值得注意的是，因为高温加上降雨少，江西部分地区干旱明显，其中，目前省会南昌干旱橙色预警生效中。</p>
								</div>
							</a>
							<a href="/news/314679.html" title="今江西高温依然 南昌干旱橙色预警生效中" target="_blank"><h3>今江西高温依然 南昌干旱橙色预警生效中</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314678.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/ZTXEnMZL1BtcFXhSeuXf0M08.jpg" alt="">
								<div>
									<h3>河南黄河以南大部有降雨 郑州多云最高气温31℃</h3>
									<p class="duodiandian">河南这两天既有降雨也不乏高温天气，这样一来，体感上就会比较闷热。据最新预报显示，预计河南黄河以南大部有降雨，局部地区降雨量可达暴雨级别，并且伴有雷暴、大风等强对流天气，大家注意防范。气温方面，西部最高气温31℃，其他地方最高气温34℃。城市中，郑州多云，最高气温31℃。</p>
								</div>
							</a>
							<a href="/news/314678.html" title="河南黄河以南大部有降雨 郑州多云最高气温31℃" target="_blank"><h3>河南黄河以南大部有降雨 郑州多云最高气温31℃</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314677.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/yFtQ7uyb1RYjV9eZoFUKrHkW.jpg" alt="">
								<div>
									<h3>浙江今部分地区午后有雷雨高温依旧 杭州继续高温红色预警</h3>
									<p class="duodiandian">据最新预报显示，浙江今部分地区午后有雷雨，不过，这样的雨并不能让高温却步，即今各地高温依旧，局部地区可达41℃以上。城市中，今杭州继续高温红色预警，预计部分地区最高气温可达40℃！请一定要谨防热射病，如出现中暑情况，要及时才措施或就医。</p>
								</div>
							</a>
							<a href="/news/314677.html" title="浙江今部分地区午后有雷雨高温依旧 杭州继续高温红色预警" target="_blank"><h3>浙江今部分地区午后有雷雨高温依旧 杭州继续高温红色预警</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314676.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/gj687bk53GfqLgwaoiXzYUNz.jpg" alt="">
								<div>
									<h3>今北京继续晴好 明后天迎降水</h3>
									<p class="duodiandian">据北京最新预报显示，今北京继续晴好天气，不过，气温上比昨天（15日）低了一些，即最高气温30℃，体感上舒适一些。这样的舒适明后还会继续，因为预计明后天迎降水，尤其后天最高气温将降至28℃，体感会凉快许多。不过，预计周五晴好回归，气温又会上升。</p>
								</div>
							</a>
							<a href="/news/314676.html" title="今北京继续晴好 明后天迎降水" target="_blank"><h3>今北京继续晴好 明后天迎降水</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314675.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/y6pDvzYetVSmwDMAMlU6bcAS.jpg" alt="">
								<div>
									<h3>广东今明维持“南雨北热”格局 广州雷雨活跃最高气温35℃</h3>
									<p class="duodiandian">广东这两天炎热与降水各自分布，即广东今明维持“南雨北热”格局。就今天来说，今南部有明显降雨，局部降雨量可达暴雨级别，而且还会伴随强对流天气，注意防范。受降水影响，南部的气温会稍微低一些，其他地方则会达到高温标准。城市中，广州雷雨活跃，最高气温35℃。</p>
								</div>
							</a>
							<a href="/news/314675.html" title="广东今明维持“南雨北热”格局 广州雷雨活跃最高气温35℃" target="_blank"><h3>广东今明维持“南雨北热”格局 广州雷雨活跃最高气温35℃</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314674.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/cWIPayICSmoIeOv9NiIqGP63.jpg" alt="">
								<div>
									<h3>2022全国交通天气最新预报：8月16日高速路况最新实时查询</h3>
									<p class="duodiandian">据2022全国交通天气最新预报显示，今河南、安徽、江苏、湖北、广东、海南、云南以及西藏等部分地区有明显降雨，尤其河南、安徽、江苏等一些地方降雨量可达暴雨级，大家出行注意安全。雷暴情况，青海、宁夏、江苏、浙江、福建、两广以及海南部分地区有雷暴出没，注意防范。能见度方面，辽宁、山东、贵州、云南、浙江、福建、湖南、两广等局部有雾侵扰，行车小心。具体情况一起来看看下面的8月16日高速路况最新实时查询。</p>
								</div>
							</a>
							<a href="/news/314674.html" title="2022全国交通天气最新预报：8月16日高速路况最新实时查询" target="_blank"><h3>2022全国交通天气最新预报：8月16日高速路况最新实时查询</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314673.html">
								<img src="https://oimg.tianqistatic.com/content/20220816/y9LP0755fEcGPHMVPE8dCcAk.jpg" alt="">
								<div>
									<h3>四川重庆浙江等最高温仍可超40℃ 豫苏皖等有强对流侵袭</h3>
									<p class="duodiandian">南方的高温还在持续，今天（16日）早上6点中央气象台继续发布高温红色预警，其中，四川、重庆、浙江等最高温仍可超40℃，请一定要注意防暑降温，谨防热射病。其他天气情况，预计今豫苏皖等有强对流侵袭，部分地区还将伴有短时强降水，注意防范。</p>
								</div>
							</a>
							<a href="/news/314673.html" title="四川重庆浙江等最高温仍可超40℃ 豫苏皖等有强对流侵袭" target="_blank"><h3>四川重庆浙江等最高温仍可超40℃ 豫苏皖等有强对流侵袭</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314650.html">
								<img src="https://oimg.tianqistatic.com/content/20220815/8q122H5DKbGAwQA89WWcSmzA.jpg" alt="">
								<div>
									<h3>2022处暑后还热吗 处暑节气过后是不是就凉快了</h3>
									<p class="duodiandian">还热。2022年处暑在8月23日，根据最新预报显示，预计未来10天（8月15日-8月25日），江淮、江汉、江南、四川盆地及陕西南部等地将出现持续高温天气，累计高温日数可达7～10天。</p>
								</div>
							</a>
							<a href="/news/314650.html" title="2022处暑后还热吗 处暑节气过后是不是就凉快了" target="_blank"><h3>2022处暑后还热吗 处暑节气过后是不是就凉快了</h3></a>
						</li>
													<li >
							<a class="left_img_style" href="/news/314647.html">
								<img src="https://oimg.tianqistatic.com/content/20220815/hgOuWdGlXZVhKC6SFfXPsawZ.jpg" alt="">
								<div>
									<h3>8月15日国外天气预报：西亚欧洲美国等部分地区高温仍持续</h3>
									<p class="duodiandian">不仅是我国，这个夏天，全球很多地方都在经历高温酷暑，尤其部分地区的极端高温天气持续不断。据最新8月15日国外天气预报显示，预计未来三天，西亚、欧洲、美国等部分地区高温仍持续，局部地区最高气温可达42℃以上。降水方面，中南半岛、印度北部、西非、中非北部、英国北部等均有明显降雨，尤其南半岛西部、西非北部等降雨量可达大暴雨级别，并伴随强对流天气。</p>
								</div>
							</a>
							<a href="/news/314647.html" title="8月15日国外天气预报：西亚欧洲美国等部分地区高温仍持续" target="_blank"><h3>8月15日国外天气预报：西亚欧洲美国等部分地区高温仍持续</h3></a>
						</li>
										</ul>
			</div>
		</div>
	</div>
	<div style="clear: both"></div>
	<div class="hhx_newB_kindTit">
	<em>天气分类</em>
	<ul class="hhx_newB_kindTit_ul">
		<li class="hhx_newB_on">热门天气</li><li>国内天气</li><li>城市天气</li><li>区县天气</li><li>景点天气</li><li>空气质量</li><li>国际天气</li>
	</ul>
</div>
<!-- 天气分类对应的内容 -->
<div class="hhx_newB_kindCon" style="margin-bottom: 56px;">
	<div>
					<a href="http://www.tianqi.com/beijing/" title="北京天气" target="_blank">北京天气</a>
					<a href="http://www.tianqi.com/shanghai/" title="上海天气" target="_blank">上海天气</a>
					<a href="http://www.tianqi.com/chongqing/" title="重庆天气" target="_blank">重庆天气</a>
					<a href="http://www.tianqi.com/tianjin/" title="天津天气" target="_blank">天津天气</a>
					<a href="http://www.tianqi.com/guangzhou/" title="广州天气" target="_blank">广州天气</a>
					<a href="http://www.tianqi.com/shenzhen/" title="深圳天气" target="_blank">深圳天气</a>
					<a href="http://www.tianqi.com/hangzhou/" title="杭州天气" target="_blank">杭州天气</a>
					<a href="http://www.tianqi.com/zhengzhou/" title="郑州天气" target="_blank">郑州天气</a>
					<a href="http://www.tianqi.com/fuzhou/" title="福州天气" target="_blank">福州天气</a>
					<a href="http://www.tianqi.com/haikou/" title="海口天气" target="_blank">海口天气</a>
					<a href="http://www.tianqi.com/wuhan/" title="武汉天气" target="_blank">武汉天气</a>
					<a href="http://www.tianqi.com/changsha/" title="长沙天气" target="_blank">长沙天气</a>
					<a href="http://www.tianqi.com/nanjing/" title="南京天气" target="_blank">南京天气</a>
					<a href="http://www.tianqi.com/chengdu/" title="成都天气" target="_blank">成都天气</a>
					<a href="http://www.tianqi.com/guiyang1/" title="贵阳天气" target="_blank">贵阳天气</a>
					<a href="http://www.tianqi.com/kunming/" title="昆明天气" target="_blank">昆明天气</a>
					<a href="http://www.tianqi.com/xian/" title="西安天气" target="_blank">西安天气</a>
					<a href="http://www.tianqi.com/taiyuan/" title="太原天气" target="_blank">太原天气</a>
					<a href="http://www.tianqi.com/jinan/" title="济南天气" target="_blank">济南天气</a>
					<a href="http://www.tianqi.com/hefei/" title="合肥天气" target="_blank">合肥天气</a>
					<a href="http://www.tianqi.com/nanchang/" title="南昌天气" target="_blank">南昌天气</a>
					<a href="http://www.tianqi.com/nanning/" title="南宁天气" target="_blank">南宁天气</a>
					<a href="http://www.tianqi.com/lasa/" title="拉萨天气" target="_blank">拉萨天气</a>
					<a href="http://www.tianqi.com/xining/" title="西宁天气" target="_blank">西宁天气</a>
					<a href="http://www.tianqi.com/lanzhou/" title="兰州天气" target="_blank">兰州天气</a>
					<a href="http://www.tianqi.com/yinchuan/" title="银川天气" target="_blank">银川天气</a>
					<a href="http://www.tianqi.com/shenyang/" title="沈阳天气" target="_blank">沈阳天气</a>
					<a href="http://www.tianqi.com/changchun/" title="长春天气" target="_blank">长春天气</a>
					<a href="http://www.tianqi.com/haerbin/" title="哈尔滨天气" target="_blank">哈尔滨天气</a>
					<a href="http://www.tianqi.com/shijiazhuang/" title="石家庄天气" target="_blank">石家庄天气</a>
					<a href="http://www.tianqi.com/huhehaote/" title="呼和浩特天气" target="_blank">呼和浩特天气</a>
					<a href="http://www.tianqi.com/wulumuqi/" title="乌鲁木齐天气" target="_blank">乌鲁木齐天气</a>
			</div>
	<div style="display: none;">
					<a href="http://www.tianqi.com/province/beijing/" title="北京天气" target="_blank">北京天气</a>
					<a href="http://www.tianqi.com/province/tianjin/" title="天津天气" target="_blank">天津天气</a>
					<a href="http://www.tianqi.com/province/chongqing/" title="重庆天气" target="_blank">重庆天气</a>
					<a href="http://www.tianqi.com/province/shanghai/" title="上海天气" target="_blank">上海天气</a>
					<a href="http://www.tianqi.com/province/zhejiang/" title="浙江天气" target="_blank">浙江天气</a>
					<a href="http://www.tianqi.com/province/jiangsu/" title="江苏天气" target="_blank">江苏天气</a>
					<a href="http://www.tianqi.com/province/fujian/" title="福建天气" target="_blank">福建天气</a>
					<a href="http://www.tianqi.com/province/jiangxi/" title="江西天气" target="_blank">江西天气</a>
					<a href="http://www.tianqi.com/province/anhui/" title="安徽天气" target="_blank">安徽天气</a>
					<a href="http://www.tianqi.com/province/liaoning/" title="辽宁天气" target="_blank">辽宁天气</a>
					<a href="http://www.tianqi.com/province/jilin/" title="吉林天气" target="_blank">吉林天气</a>
					<a href="http://www.tianqi.com/province/heilongjiang/" title="黑龙江天气" target="_blank">黑龙江天气</a>
					<a href="http://www.tianqi.com/province/hainan/" title="海南天气" target="_blank">海南天气</a>
					<a href="http://www.tianqi.com/province/guangdong/" title="广东天气" target="_blank">广东天气</a>
					<a href="http://www.tianqi.com/province/guangxi/" title="广西天气" target="_blank">广西天气</a>
					<a href="http://www.tianqi.com/province/shandong/" title="山东天气" target="_blank">山东天气</a>
					<a href="http://www.tianqi.com/province/shanxi/" title="山西天气" target="_blank">山西天气</a>
					<a href="http://www.tianqi.com/province/hunan/" title="湖南天气" target="_blank">湖南天气</a>
					<a href="http://www.tianqi.com/province/hubei/" title="湖北天气" target="_blank">湖北天气</a>
					<a href="http://www.tianqi.com/province/henan/" title="河南天气" target="_blank">河南天气</a>
					<a href="http://www.tianqi.com/province/hebei/" title="河北天气" target="_blank">河北天气</a>
					<a href="http://www.tianqi.com/province/xinjiang/" title="新疆天气" target="_blank">新疆天气</a>
					<a href="http://www.tianqi.com/province/xizang/" title="西藏天气" target="_blank">西藏天气</a>
					<a href="http://www.tianqi.com/province/neimenggu/" title="内蒙古天气" target="_blank">内蒙古天气</a>
					<a href="http://www.tianqi.com/province/sichuan/" title="四川天气" target="_blank">四川天气</a>
					<a href="http://www.tianqi.com/province/yunnan/" title="云南天气" target="_blank">云南天气</a>
					<a href="http://www.tianqi.com/province/guizhou/" title="贵州天气" target="_blank">贵州天气</a>
					<a href="http://www.tianqi.com/province/shanxi1/" title="陕西天气" target="_blank">陕西天气</a>
					<a href="http://www.tianqi.com/province/qinghai/" title="青海天气" target="_blank">青海天气</a>
					<a href="http://www.tianqi.com/province/ningxia/" title="宁夏天气" target="_blank">宁夏天气</a>
					<a href="http://www.tianqi.com/province/gansu/" title="甘肃天气" target="_blank">甘肃天气</a>
					<a href="http://www.tianqi.com/province/hongkong/" title="香港天气" target="_blank">香港天气</a>
					<a href="http://www.tianqi.com/province/aomen/" title="澳门天气" target="_blank">澳门天气</a>
					<a href="http://www.tianqi.com/province/taiwan/" title="台湾天气" target="_blank">台湾天气</a>
			</div>
	<div style="display: none;">
					<a href="http://www.tianqi.com/linzhi/" title="林芝天气" target="_blank">林芝天气</a>
					<a href="http://www.tianqi.com/xiamen/" title="厦门市天气" target="_blank">厦门市天气</a>
					<a href="http://www.tianqi.com/shantou/" title="汕头市天气" target="_blank">汕头市天气</a>
					<a href="http://www.tianqi.com/shanwei/" title="汕尾市天气" target="_blank">汕尾市天气</a>
					<a href="http://www.tianqi.com/sanya/" title="三亚市天气" target="_blank">三亚市天气</a>
					<a href="http://www.tianqi.com/jiangmen/" title="江门市天气" target="_blank">江门市天气</a>
					<a href="http://www.tianqi.com/erlianhaote/" title="二连浩特市天气" target="_blank">二连浩特市天气</a>
					<a href="http://www.tianqi.com/mudanjiang/" title="牡丹江市天气" target="_blank">牡丹江市天气</a>
					<a href="http://www.tianqi.com/zhoushan/" title="舟山市天气" target="_blank">舟山市天气</a>
					<a href="http://www.tianqi.com/rikaze/" title="日喀则天气" target="_blank">日喀则天气</a>
					<a href="http://www.tianqi.com/jieyang/" title="揭阳市天气" target="_blank">揭阳市天气</a>
					<a href="http://www.tianqi.com/xianggelila/" title="香格里拉天气" target="_blank">香格里拉天气</a>
					<a href="http://www.tianqi.com/zhuhai/" title="珠海市天气" target="_blank">珠海市天气</a>
					<a href="http://www.tianqi.com/haikou/" title="海口市天气" target="_blank">海口市天气</a>
					<a href="http://www.tianqi.com/zhangzhou/" title="漳州市天气" target="_blank">漳州市天气</a>
					<a href="http://www.tianqi.com/xishuangbanna/" title="西双版纳天气" target="_blank">西双版纳天气</a>
					<a href="http://www.tianqi.com/shannan/" title="山南天气" target="_blank">山南天气</a>
					<a href="http://www.tianqi.com/alidiqu/" title="阿里天气" target="_blank">阿里天气</a>
					<a href="http://www.tianqi.com/fuxin/" title="阜新市天气" target="_blank">阜新市天气</a>
					<a href="http://www.tianqi.com/lujiang/" title="怒江傈天气" target="_blank">怒江傈天气</a>
					<a href="http://www.tianqi.com/hongkong/" title="香港特别行政区天气" target="_blank">香港特别行政区天气</a>
					<a href="http://www.tianqi.com/tongliao/" title="通辽市天气" target="_blank">通辽市天气</a>
					<a href="http://www.tianqi.com/fushun/" title="抚顺市天气" target="_blank">抚顺市天气</a>
					<a href="http://www.tianqi.com/meizhou/" title="梅州市天气" target="_blank">梅州市天气</a>
					<a href="http://www.tianqi.com/chaohushi/" title="巢湖市天气" target="_blank">巢湖市天气</a>
					<a href="http://www.tianqi.com/chuxiong/" title="楚雄天气" target="_blank">楚雄天气</a>
					<a href="http://www.tianqi.com/changdu/" title="昌都天气" target="_blank">昌都天气</a>
					<a href="http://www.tianqi.com/baoshan/" title="保山市天气" target="_blank">保山市天气</a>
					<a href="http://www.tianqi.com/chaoyang/" title="朝阳市天气" target="_blank">朝阳市天气</a>
					<a href="http://www.tianqi.com/yangjiang/" title="阳江市天气" target="_blank">阳江市天气</a>
					<a href="http://www.tianqi.com/quanzhou/" title="泉州市天气" target="_blank">泉州市天气</a>
					<a href="http://www.tianqi.com/heyuan/" title="河源市天气" target="_blank">河源市天气</a>
					<a href="http://www.tianqi.com/naqu/" title="那曲天气" target="_blank">那曲天气</a>
					<a href="http://www.tianqi.com/honghe/" title="红河哈尼族天气" target="_blank">红河哈尼族天气</a>
					<a href="http://www.tianqi.com/tieling/" title="铁岭市天气" target="_blank">铁岭市天气</a>
					<a href="http://www.tianqi.com/panjin/" title="盘锦市天气" target="_blank">盘锦市天气</a>
					<a href="http://www.tianqi.com/jinzhou/" title="锦州市天气" target="_blank">锦州市天气</a>
					<a href="http://www.tianqi.com/dandong/" title="丹东市天气" target="_blank">丹东市天气</a>
					<a href="http://www.tianqi.com/suizhou/" title="随州市天气" target="_blank">随州市天气</a>
					<a href="http://www.tianqi.com/guilin/" title="桂林市天气" target="_blank">桂林市天气</a>
					<a href="http://www.tianqi.com/foshan/" title="佛山市天气" target="_blank">佛山市天气</a>
					<a href="http://www.tianqi.com/wenshan/" title="文山天气" target="_blank">文山天气</a>
					<a href="http://www.tianqi.com/lasa/" title="拉萨市天气" target="_blank">拉萨市天气</a>
					<a href="http://www.tianqi.com/huludao/" title="葫芦岛市天气" target="_blank">葫芦岛市天气</a>
					<a href="http://www.tianqi.com/benxi/" title="本溪市天气" target="_blank">本溪市天气</a>
					<a href="http://www.tianqi.com/shenzhen/" title="深圳市天气" target="_blank">深圳市天气</a>
					<a href="http://www.tianqi.com/huizhou/" title="惠州市天气" target="_blank">惠州市天气</a>
					<a href="http://www.tianqi.com/zhongshan/" title="中山市天气" target="_blank">中山市天气</a>
					<a href="http://www.tianqi.com/dali/" title="大理天气" target="_blank">大理天气</a>
					<a href="http://www.tianqi.com/chifeng/" title="赤峰市天气" target="_blank">赤峰市天气</a>
					<a href="http://www.tianqi.com/shenyang/" title="沈阳市天气" target="_blank">沈阳市天气</a>
					<a href="http://www.tianqi.com/haerbin/" title="哈尔滨市天气" target="_blank">哈尔滨市天气</a>
					<a href="http://www.tianqi.com/daqing/" title="大庆市天气" target="_blank">大庆市天气</a>
					<a href="http://www.tianqi.com/changchun/" title="长春市天气" target="_blank">长春市天气</a>
					<a href="http://www.tianqi.com/pingxiang/" title="萍乡市天气" target="_blank">萍乡市天气</a>
					<a href="http://www.tianqi.com/taizhoushi/" title="泰州市天气" target="_blank">泰州市天气</a>
					<a href="http://www.tianqi.com/beijing/" title="北京市天气" target="_blank">北京市天气</a>
					<a href="http://www.tianqi.com/chengde/" title="承德市天气" target="_blank">承德市天气</a>
					<a href="http://www.tianqi.com/linfen/" title="临汾市天气" target="_blank">临汾市天气</a>
					<a href="http://www.tianqi.com/liaoyang/" title="辽阳市天气" target="_blank">辽阳市天气</a>
					<a href="http://www.tianqi.com/taizhou/" title="台州市天气" target="_blank">台州市天气</a>
					<a href="http://www.tianqi.com/qinhuangdao/" title="秦皇岛市天气" target="_blank">秦皇岛市天气</a>
					<a href="http://www.tianqi.com/xingan/" title="兴安盟天气" target="_blank">兴安盟天气</a>
					<a href="http://www.tianqi.com/hulunbeier/" title="呼伦贝尔市天气" target="_blank">呼伦贝尔市天气</a>
					<a href="http://www.tianqi.com/qiqihaer/" title="齐齐哈尔市天气" target="_blank">齐齐哈尔市天气</a>
					<a href="http://www.tianqi.com/zhanjiang/" title="湛江市天气" target="_blank">湛江市天气</a>
					<a href="http://www.tianqi.com/changde/" title="常德市天气" target="_blank">常德市天气</a>
					<a href="http://www.tianqi.com/bengpu/" title="蚌埠市天气" target="_blank">蚌埠市天气</a>
					<a href="http://www.tianqi.com/dehong/" title="德宏天气" target="_blank">德宏天气</a>
					<a href="http://www.tianqi.com/anba/" title="阿坝天气" target="_blank">阿坝天气</a>
					<a href="http://www.tianqi.com/yangzhou/" title="扬州市天气" target="_blank">扬州市天气</a>
					<a href="http://www.tianqi.com/yancheng/" title="盐城市天气" target="_blank">盐城市天气</a>
					<a href="http://www.tianqi.com/xiligule/" title="锡林郭勒盟天气" target="_blank">锡林郭勒盟天气</a>
					<a href="http://www.tianqi.com/yingkou/" title="营口市天气" target="_blank">营口市天气</a>
					<a href="http://www.tianqi.com/anshan/" title="鞍山市天气" target="_blank">鞍山市天气</a>
					<a href="http://www.tianqi.com/yiyang/" title="益阳市天气" target="_blank">益阳市天气</a>
					<a href="http://www.tianqi.com/jilin/" title="吉林市天气" target="_blank">吉林市天气</a>
					<a href="http://www.tianqi.com/liuzhou/" title="柳州市天气" target="_blank">柳州市天气</a>
					<a href="http://www.tianqi.com/huainan/" title="淮南市天气" target="_blank">淮南市天气</a>
					<a href="http://www.tianqi.com/yuxi/" title="玉溪市天气" target="_blank">玉溪市天气</a>
					<a href="http://www.tianqi.com/lijiang/" title="丽江市天气" target="_blank">丽江市天气</a>
					<a href="http://www.tianqi.com/kunming/" title="昆明市天气" target="_blank">昆明市天气</a>
					<a href="http://www.tianqi.com/dalian/" title="大连市天气" target="_blank">大连市天气</a>
					<a href="http://www.tianqi.com/zhaoqing/" title="肇庆市天气" target="_blank">肇庆市天气</a>
					<a href="http://www.tianqi.com/xianning/" title="咸宁市天气" target="_blank">咸宁市天气</a>
					<a href="http://www.tianqi.com/ningbo/" title="宁波市天气" target="_blank">宁波市天气</a>
					<a href="http://www.tianqi.com/guangzhou/" title="广州市天气" target="_blank">广州市天气</a>
					<a href="http://www.tianqi.com/guiyang/" title="贵阳市天气" target="_blank">贵阳市天气</a>
					<a href="http://www.tianqi.com/zhenjiang/" title="镇江市天气" target="_blank">镇江市天气</a>
					<a href="http://www.tianqi.com/zhangjiakou/" title="张家口市天气" target="_blank">张家口市天气</a>
					<a href="http://www.tianqi.com/datong/" title="大同市天气" target="_blank">大同市天气</a>
					<a href="http://www.tianqi.com/yingtan/" title="鹰潭市天气" target="_blank">鹰潭市天气</a>
					<a href="http://www.tianqi.com/xinyang/" title="信阳市天气" target="_blank">信阳市天气</a>
					<a href="http://www.tianqi.com/sanmenxia/" title="三门峡市天气" target="_blank">三门峡市天气</a>
					<a href="http://www.tianqi.com/rizhao/" title="日照市天气" target="_blank">日照市天气</a>
					<a href="http://www.tianqi.com/maoming/" title="茂名市天气" target="_blank">茂名市天气</a>
					<a href="http://www.tianqi.com/dongying/" title="东营市天气" target="_blank">东营市天气</a>
					<a href="http://www.tianqi.com/binzhou/" title="滨州市天气" target="_blank">滨州市天气</a>
					<a href="http://www.tianqi.com/beihai/" title="北海市天气" target="_blank">北海市天气</a>
					<a href="http://www.tianqi.com/dazhou/" title="达州市天气" target="_blank">达州市天气</a>
					<a href="http://www.tianqi.com/tianjin/" title="天津市天气" target="_blank">天津市天气</a>
					<a href="http://www.tianqi.com/xingtai/" title="邢台市天气" target="_blank">邢台市天气</a>
					<a href="http://www.tianqi.com/cangzhou/" title="沧州市天气" target="_blank">沧州市天气</a>
					<a href="http://www.tianqi.com/yongzhou/" title="永州市天气" target="_blank">永州市天气</a>
					<a href="http://www.tianqi.com/nanning/" title="南宁市天气" target="_blank">南宁市天气</a>
					<a href="http://www.tianqi.com/huangshan/" title="黄山市天气" target="_blank">黄山市天气</a>
					<a href="http://www.tianqi.com/fuzhoushi/" title="抚州市天气" target="_blank">抚州市天气</a>
					<a href="http://www.tianqi.com/bozhou/" title="亳州市天气" target="_blank">亳州市天气</a>
					<a href="http://www.tianqi.com/zunyi/" title="遵义市天气" target="_blank">遵义市天气</a>
					<a href="http://www.tianqi.com/diqing/" title="迪庆天气" target="_blank">迪庆天气</a>
					<a href="http://www.tianqi.com/lianyungang/" title="连云港市天气" target="_blank">连云港市天气</a>
					<a href="http://www.tianqi.com/huaian/" title="淮安市天气" target="_blank">淮安市天气</a>
					<a href="http://www.tianqi.com/zhangjiajie/" title="张家界市天气" target="_blank">张家界市天气</a>
					<a href="http://www.tianqi.com/yunfu/" title="云浮市天气" target="_blank">云浮市天气</a>
					<a href="http://www.tianqi.com/xuancheng/" title="宣城市天气" target="_blank">宣城市天气</a>
					<a href="http://www.tianqi.com/xiangtan/" title="湘潭市天气" target="_blank">湘潭市天气</a>
					<a href="http://www.tianqi.com/mianyang/" title="绵阳市天气" target="_blank">绵阳市天气</a>
					<a href="http://www.tianqi.com/bazhong/" title="巴中市天气" target="_blank">巴中市天气</a>
					<a href="http://www.tianqi.com/tangshan/" title="唐山市天气" target="_blank">唐山市天气</a>
					<a href="http://www.tianqi.com/handan/" title="邯郸市天气" target="_blank">邯郸市天气</a>
					<a href="http://www.tianqi.com/baoding/" title="保定市天气" target="_blank">保定市天气</a>
					<a href="http://www.tianqi.com/huhehaote/" title="呼和浩特市天气" target="_blank">呼和浩特市天气</a>
					<a href="http://www.tianqi.com/weihai/" title="威海市天气" target="_blank">威海市天气</a>
					<a href="http://www.tianqi.com/putian/" title="莆田市天气" target="_blank">莆田市天气</a>
					<a href="http://www.tianqi.com/ganzhou/" title="赣州市天气" target="_blank">赣州市天气</a>
					<a href="http://www.tianqi.com/enshi/" title="恩施天气" target="_blank">恩施天气</a>
					<a href="http://www.tianqi.com/qujing/" title="曲靖市天气" target="_blank">曲靖市天气</a>
					<a href="http://www.tianqi.com/kelamayi/" title="克拉玛依市天气" target="_blank">克拉玛依市天气</a>
					<a href="http://www.tianqi.com/shijiazhuang/" title="石家庄市天气" target="_blank">石家庄市天气</a>
					<a href="http://www.tianqi.com/jincheng/" title="晋城市天气" target="_blank">晋城市天气</a>
					<a href="http://www.tianqi.com/weifang/" title="潍坊市天气" target="_blank">潍坊市天气</a>
					<a href="http://www.tianqi.com/suzhoushi/" title="宿州市天气" target="_blank">宿州市天气</a>
					<a href="http://www.tianqi.com/qingdao/" title="青岛市天气" target="_blank">青岛市天气</a>
					<a href="http://www.tianqi.com/fuyang/" title="阜阳市天气" target="_blank">阜阳市天气</a>
					<a href="http://www.tianqi.com/chuzhou/" title="滁州市天气" target="_blank">滁州市天气</a>
					<a href="http://www.tianqi.com/yanan/" title="延安市天气" target="_blank">延安市天气</a>
					<a href="http://www.tianqi.com/ganzi/" title="甘孜天气" target="_blank">甘孜天气</a>
					<a href="http://www.tianqi.com/yuncheng/" title="运城市天气" target="_blank">运城市天气</a>
					<a href="http://www.tianqi.com/baotou/" title="包头市天气" target="_blank">包头市天气</a>
					<a href="http://www.tianqi.com/shaoyang/" title="邵阳市天气" target="_blank">邵阳市天气</a>
					<a href="http://www.tianqi.com/longyan/" title="龙岩市天气" target="_blank">龙岩市天气</a>
					<a href="http://www.tianqi.com/huaibei/" title="淮北市天气" target="_blank">淮北市天气</a>
					<a href="http://www.tianqi.com/yaan/" title="雅安市天气" target="_blank">雅安市天气</a>
					<a href="http://www.tianqi.com/xiangyan/" title="襄阳市天气" target="_blank">襄阳市天气</a>
					<a href="http://www.tianqi.com/langfang/" title="廊坊市天气" target="_blank">廊坊市天气</a>
					<a href="http://www.tianqi.com/shiyan/" title="十堰市天气" target="_blank">十堰市天气</a>
					<a href="http://www.tianqi.com/shaotong/" title="昭通市天气" target="_blank">昭通市天气</a>
					<a href="http://www.tianqi.com/wulumuqi/" title="乌鲁木齐市天气" target="_blank">乌鲁木齐市天气</a>
					<a href="http://www.tianqi.com/shizuishan/" title="石嘴山市天气" target="_blank">石嘴山市天气</a>
					<a href="http://www.tianqi.com/guangyuan/" title="广元市天气" target="_blank">广元市天气</a>
					<a href="http://www.tianqi.com/nanping/" title="南平市天气" target="_blank">南平市天气</a>
					<a href="http://www.tianqi.com/liuan/" title="六安市天气" target="_blank">六安市天气</a>
					<a href="http://www.tianqi.com/chaozhou/" title="潮州市天气" target="_blank">潮州市天气</a>
					<a href="http://www.tianqi.com/tongchuan/" title="铜川市天气" target="_blank">铜川市天气</a>
					<a href="http://www.tianqi.com/yangquan/" title="阳泉市天气" target="_blank">阳泉市天气</a>
					<a href="http://www.tianqi.com/zhuzhou/" title="株洲市天气" target="_blank">株洲市天气</a>
					<a href="http://www.tianqi.com/qingyuan/" title="清远市天气" target="_blank">清远市天气</a>
					<a href="http://www.tianqi.com/loudi/" title="娄底市天气" target="_blank">娄底市天气</a>
					<a href="http://www.tianqi.com/panzhihua/" title="攀枝花市天气" target="_blank">攀枝花市天气</a>
					<a href="http://www.tianqi.com/jiayuguan/" title="嘉峪关市天气" target="_blank">嘉峪关市天气</a>
					<a href="http://www.tianqi.com/jinzhong/" title="晋中市天气" target="_blank">晋中市天气</a>
					<a href="http://www.tianqi.com/changzhi/" title="长治市天气" target="_blank">长治市天气</a>
					<a href="http://www.tianqi.com/yichang/" title="宜昌市天气" target="_blank">宜昌市天气</a>
					<a href="http://www.tianqi.com/jingzhou/" title="荆州市天气" target="_blank">荆州市天气</a>
					<a href="http://www.tianqi.com/hengyang/" title="衡阳市天气" target="_blank">衡阳市天气</a>
					<a href="http://www.tianqi.com/lincang/" title="临沧市天气" target="_blank">临沧市天气</a>
					<a href="http://www.tianqi.com/baoji/" title="宝鸡市天气" target="_blank">宝鸡市天气</a>
					<a href="http://www.tianqi.com/taiyuan/" title="太原市天气" target="_blank">太原市天气</a>
					<a href="http://www.tianqi.com/sanming/" title="三明市天气" target="_blank">三明市天气</a>
					<a href="http://www.tianqi.com/shaoxing/" title="绍兴市天气" target="_blank">绍兴市天气</a>
					<a href="http://www.tianqi.com/fuzhou/" title="福州市天气" target="_blank">福州市天气</a>
					<a href="http://www.tianqi.com/deyang/" title="德阳市天气" target="_blank">德阳市天气</a>
					<a href="http://www.tianqi.com/shangqiu/" title="商丘市天气" target="_blank">商丘市天气</a>
					<a href="http://www.tianqi.com/chongqing/" title="重庆市天气" target="_blank">重庆市天气</a>
					<a href="http://www.tianqi.com/wenzhou/" title="温州市天气" target="_blank">温州市天气</a>
					<a href="http://www.tianqi.com/quzhou/" title="衢州市天气" target="_blank">衢州市天气</a>
					<a href="http://www.tianqi.com/jiujiang/" title="九江市天气" target="_blank">九江市天气</a>
					<a href="http://www.tianqi.com/dongguan/" title="东莞市天气" target="_blank">东莞市天气</a>
					<a href="http://www.tianqi.com/chengdu/" title="成都市天气" target="_blank">成都市天气</a>
					<a href="http://www.tianqi.com/hengshui/" title="衡水市天气" target="_blank">衡水市天气</a>
					<a href="http://www.tianqi.com/shuozhou/" title="朔州市天气" target="_blank">朔州市天气</a>
					<a href="http://www.tianqi.com/alashanmeng/" title="阿拉善盟天气" target="_blank">阿拉善盟天气</a>
					<a href="http://www.tianqi.com/yueyang/" title="岳阳市天气" target="_blank">岳阳市天气</a>
					<a href="http://www.tianqi.com/tongling/" title="铜陵市天气" target="_blank">铜陵市天气</a>
					<a href="http://www.tianqi.com/taian/" title="泰安市天气" target="_blank">泰安市天气</a>
					<a href="http://www.tianqi.com/nanchang/" title="南昌市天气" target="_blank">南昌市天气</a>
					<a href="http://www.tianqi.com/luzhou/" title="泸州市天气" target="_blank">泸州市天气</a>
					<a href="http://www.tianqi.com/liangshan/" title="凉山天气" target="_blank">凉山天气</a>
					<a href="http://www.tianqi.com/suqian/" title="宿迁市天气" target="_blank">宿迁市天气</a>
					<a href="http://www.tianqi.com/eerduozi/" title="鄂尔多斯市天气" target="_blank">鄂尔多斯市天气</a>
					<a href="http://www.tianqi.com/xinyu/" title="新余市天气" target="_blank">新余市天气</a>
					<a href="http://www.tianqi.com/puyang/" title="濮阳市天气" target="_blank">濮阳市天气</a>
					<a href="http://www.tianqi.com/nanyang/" title="南阳市天气" target="_blank">南阳市天气</a>
					<a href="http://www.tianqi.com/jingmen/" title="荆门市天气" target="_blank">荆门市天气</a>
					<a href="http://www.tianqi.com/jiaxing/" title="嘉兴市天气" target="_blank">嘉兴市天气</a>
					<a href="http://www.tianqi.com/jian/" title="吉安市天气" target="_blank">吉安市天气</a>
					<a href="http://www.tianqi.com/huzhou/" title="湖州市天气" target="_blank">湖州市天气</a>
					<a href="http://www.tianqi.com/chizhou/" title="池州市天气" target="_blank">池州市天气</a>
					<a href="http://www.tianqi.com/nanjing/" title="南京市天气" target="_blank">南京市天气</a>
					<a href="http://www.tianqi.com/lishui/" title="丽水市天气" target="_blank">丽水市天气</a>
					<a href="http://www.tianqi.com/jiaozuo/" title="焦作市天气" target="_blank">焦作市天气</a>
					<a href="http://www.tianqi.com/heze/" title="菏泽市天气" target="_blank">菏泽市天气</a>
					<a href="http://www.tianqi.com/hefei/" title="合肥市天气" target="_blank">合肥市天气</a>
					<a href="http://www.tianqi.com/qizhou/" title="忻州市天气" target="_blank">忻州市天气</a>
					<a href="http://www.tianqi.com/zhumadian/" title="驻马店市天气" target="_blank">驻马店市天气</a>
					<a href="http://www.tianqi.com/xiaogan/" title="孝感市天气" target="_blank">孝感市天气</a>
					<a href="http://www.tianqi.com/zhuzhoushi/" title="郴州市天气" target="_blank">郴州市天气</a>
					<a href="http://www.tianqi.com/anyang/" title="安阳市天气" target="_blank">安阳市天气</a>
					<a href="http://www.tianqi.com/weinan/" title="渭南市天气" target="_blank">渭南市天气</a>
					<a href="http://www.tianqi.com/xuzhou/" title="徐州市天气" target="_blank">徐州市天气</a>
					<a href="http://www.tianqi.com/wuhan/" title="武汉市天气" target="_blank">武汉市天气</a>
					<a href="http://www.tianqi.com/shangrao/" title="上饶市天气" target="_blank">上饶市天气</a>
					<a href="http://www.tianqi.com/meishan/" title="眉山市天气" target="_blank">眉山市天气</a>
					<a href="http://www.tianqi.com/shennongjia/" title="神农架天气" target="_blank">神农架天气</a>
					<a href="http://www.tianqi.com/suzhou/" title="苏州市天气" target="_blank">苏州市天气</a>
					<a href="http://www.tianqi.com/zibo/" title="淄博市天气" target="_blank">淄博市天气</a>
					<a href="http://www.tianqi.com/wuhu/" title="芜湖市天气" target="_blank">芜湖市天气</a>
					<a href="http://www.tianqi.com/linyi/" title="临沂市天气" target="_blank">临沂市天气</a>
					<a href="http://www.tianqi.com/hebi/" title="鹤壁市天气" target="_blank">鹤壁市天气</a>
					<a href="http://www.tianqi.com/yinchuan/" title="银川市天气" target="_blank">银川市天气</a>
					<a href="http://www.tianqi.com/xining/" title="西宁市天气" target="_blank">西宁市天气</a>
					<a href="http://www.tianqi.com/yichun/" title="宜春市天气" target="_blank">宜春市天气</a>
					<a href="http://www.tianqi.com/pingdingshan/" title="平顶山市天气" target="_blank">平顶山市天气</a>
					<a href="http://www.tianqi.com/jingdezhen/" title="景德镇市天气" target="_blank">景德镇市天气</a>
					<a href="http://www.tianqi.com/shaoguan/" title="韶关市天气" target="_blank">韶关市天气</a>
					<a href="http://www.tianqi.com/zhengzhou/" title="郑州市天气" target="_blank">郑州市天气</a>
					<a href="http://www.tianqi.com/jinhua/" title="金华市天气" target="_blank">金华市天气</a>
					<a href="http://www.tianqi.com/maanshan/" title="马鞍山市天气" target="_blank">马鞍山市天气</a>
					<a href="http://www.tianqi.com/dezhou/" title="德州市天气" target="_blank">德州市天气</a>
					<a href="http://www.tianqi.com/changsha/" title="长沙市天气" target="_blank">长沙市天气</a>
					<a href="http://www.tianqi.com/lanzhou/" title="兰州市天气" target="_blank">兰州市天气</a>
					<a href="http://www.tianqi.com/luliang/" title="吕梁市天气" target="_blank">吕梁市天气</a>
					<a href="http://www.tianqi.com/luoyang/" title="洛阳市天气" target="_blank">洛阳市天气</a>
					<a href="http://www.tianqi.com/liaocheng/" title="聊城市天气" target="_blank">聊城市天气</a>
					<a href="http://www.tianqi.com/hangzhou/" title="杭州市天气" target="_blank">杭州市天气</a>
					<a href="http://www.tianqi.com/anqing/" title="安庆市天气" target="_blank">安庆市天气</a>
					<a href="http://www.tianqi.com/guangan/" title="广安市天气" target="_blank">广安市天气</a>
					<a href="http://www.tianqi.com/kaifeng/" title="开封市天气" target="_blank">开封市天气</a>
					<a href="http://www.tianqi.com/xianyang/" title="咸阳市天气" target="_blank">咸阳市天气</a>
					<a href="http://www.tianqi.com/leshan/" title="乐山市天气" target="_blank">乐山市天气</a>
					<a href="http://www.tianqi.com/jinchang/" title="金昌市天气" target="_blank">金昌市天气</a>
					<a href="http://www.tianqi.com/xinxiang/" title="新乡天气" target="_blank">新乡天气</a>
					<a href="http://www.tianqi.com/luohe/" title="漯河市天气" target="_blank">漯河市天气</a>
					<a href="http://www.tianqi.com/bayanchuoer/" title="巴彦淖尔市天气" target="_blank">巴彦淖尔市天气</a>
					<a href="http://www.tianqi.com/ziyang/" title="资阳市天气" target="_blank">资阳市天气</a>
					<a href="http://www.tianqi.com/zhoukou/" title="周口市天气" target="_blank">周口市天气</a>
					<a href="http://www.tianqi.com/xuchang/" title="许昌市天气" target="_blank">许昌市天气</a>
					<a href="http://www.tianqi.com/huangshi/" title="黄石市天气" target="_blank">黄石市天气</a>
					<a href="http://www.tianqi.com/nanchong/" title="南充市天气" target="_blank">南充市天气</a>
					<a href="http://www.tianqi.com/xian/" title="西安市天气" target="_blank">西安市天气</a>
					<a href="http://www.tianqi.com/wuxi/" title="无锡市天气" target="_blank">无锡市天气</a>
					<a href="http://www.tianqi.com/jining/" title="济宁市天气" target="_blank">济宁市天气</a>
					<a href="http://www.tianqi.com/ezhou/" title="鄂州市天气" target="_blank">鄂州市天气</a>
					<a href="http://www.tianqi.com/changzhou/" title="常州市天气" target="_blank">常州市天气</a>
					<a href="http://www.tianqi.com/wuhai/" title="乌海市天气" target="_blank">乌海市天气</a>
					<a href="http://www.tianqi.com/yibin/" title="宜宾市天气" target="_blank">宜宾市天气</a>
					<a href="http://www.tianqi.com/jinan/" title="济南市天气" target="_blank">济南市天气</a>
					<a href="http://www.tianqi.com/xiantao/" title="仙桃天气" target="_blank">仙桃天气</a>
					<a href="http://www.tianqi.com/zaozhuang/" title="枣庄市天气" target="_blank">枣庄市天气</a>
					<a href="http://www.tianqi.com/huanggan/" title="黄冈市天气" target="_blank">黄冈市天气</a>
					<a href="http://www.tianqi.com/shanghai/" title="上海市天气" target="_blank">上海市天气</a>
					<a href="http://www.tianqi.com/kuerle/" title="库尔勒天气" target="_blank">库尔勒天气</a>
					<a href="http://www.tianqi.com/macau/" title="澳门天气" target="_blank">澳门天气</a>
					<a href="http://www.tianqi.com/suiing/" title="遂宁市天气" target="_blank">遂宁市天气</a>
					<a href="http://www.tianqi.com/qianjiang/" title="潜江天气" target="_blank">潜江天气</a>
					<a href="http://www.tianqi.com/neijing/" title="内江市天气" target="_blank">内江市天气</a>
					<a href="http://www.tianqi.com/zigong/" title="自贡市天气" target="_blank">自贡市天气</a>
					<a href="http://www.tianqi.com/nantong/" title="南通市天气" target="_blank">南通市天气</a>
			</div>
	<div style="display: none;">
		<a href="http://www.tianqi.com/shalu/" title="沙鹿天气" target="_blank">沙鹿天气</a>
		<a href="http://www.tianqi.com/taizhongqingshui/" title="清水天气" target="_blank">清水天气</a>
		<a href="http://www.tianqi.com/dajia/" title="大甲天气预报" target="_blank">大甲天气</a>
		<a href="http://www.tianqi.com/dongshi/" title="东势天气" target="_blank">东势天气</a>
		<a href="http://www.tianqi.com/taiping/" title="太平天气" target="_blank">太平天气</a>
		<a href="http://www.tianqi.com/taizhongdali/" title="大里天气" target="_blank">大里天气</a>
		<a href="http://www.tianqi.com/fengyuan/" title="丰原天气" target="_blank">丰原天气</a>
		<a href="http://www.tianqi.com/beitun/" title="北屯天气" target="_blank">北屯天气</a>
		<a href="http://www.tianqi.com/nantun/" title="南屯天气" target="_blank">南屯天气</a>
		<a href="http://www.tianqi.com/xitun/" title="西屯天气" target="_blank">西屯天气</a>
		<a href="http://www.tianqi.com/beiqu/" title="北区天气" target="_blank">北区天气</a>
		<a href="http://www.tianqi.com/taizhongnanqu/" title="南区天气" target="_blank">南区天气</a>
		<a href="http://www.tianqi.com/taizhongxiqu/" title="西区天气" target="_blank">西区天气</a>
		<a href="http://www.tianqi.com/taizhongdongqu/" title="东区天气" target="_blank">东区天气</a>
		<a href="http://www.tianqi.com/zhongqu/" title="中区天气" target="_blank">中区天气</a>
		<a href="http://www.tianqi.com/taizhong/" title="台中天气" target="_blank">台中天气</a>
		<a href="http://www.tianqi.com/tianliao/" title="田寮天气" target="_blank">田寮天气</a>
		<a href="http://www.tianqi.com/namaxia/" title="那玛夏天气" target="_blank">那玛夏天气</a>
		<a href="http://www.tianqi.com/gaoxiongtaoyuan/" title="桃源天气" target="_blank">桃源天气</a>
		<a href="http://www.tianqi.com/maolin/" title="茂林天气" target="_blank">茂林天气</a>
		<a href="http://www.tianqi.com/liugui/" title="六龟天气" target="_blank">六龟天气</a>
		<a href="http://www.tianqi.com/gaoxiongjiaxian/" title="甲仙天气" target="_blank">甲仙天气</a>
		<a href="http://www.tianqi.com/shanlin/" title="杉林天气" target="_blank">杉林天气</a>
		<a href="http://www.tianqi.com/neimen/" title="内门天气" target="_blank">内门天气</a>
		<a href="http://www.tianqi.com/meinong/" title="美浓天气" target="_blank">美浓天气</a>
		<a href="http://www.tianqi.com/gaoxiongqishan/" title="旗山天气" target="_blank">旗山天气</a>
		<a href="http://www.tianqi.com/hunei/" title="湖内天气" target="_blank">湖内天气</a>
		<a href="http://www.tianqi.com/qieding/" title="茄萣天气" target="_blank">茄萣天气</a>
		<a href="http://www.tianqi.com/alian/" title="阿莲天气" target="_blank">阿莲天气</a>
		<a href="http://www.tianqi.com/yanchao/" title="燕巢天气" target="_blank">燕巢天气</a>
		<a href="http://www.tianqi.com/yunyang/" title="云阳天气" target="_blank">云阳天气</a>
		<a href="http://www.tianqi.com/dongli/" title="东丽天气" target="_blank">东丽天气</a>
		<a href="http://www.tianqi.com/jinning/" title="晋宁天气" target="_blank">晋宁天气</a>
		<a href="http://www.tianqi.com/pudong/" title="浦东天气" target="_blank">浦东天气</a>
		<a href="http://www.tianqi.com/fengdu/" title="丰都天气" target="_blank">丰都天气</a>
		<a href="http://www.tianqi.com/jiangning/" title="江宁天气" target="_blank">江宁天气</a>
		<a href="http://www.tianqi.com/jixian/" title="蓟县天气" target="_blank">蓟县天气</a>
		<a href="http://www.tianqi.com/dujiangyan/" title="都江堰天气" target="_blank">都江堰天气</a>
		<a href="http://www.tianqi.com/jinjiangqu/" title="锦江区天气" target="_blank">锦江区天气</a>
		<a href="http://www.tianqi.com/xiaoshan/" title="萧山天气" target="_blank">萧山天气</a>
	</div>
	<div style="display: none;">
		<a href="http://www.tianqi.com/beijingjingdian/4168/" title="八达岭长城天气" target="_blank">八达岭长城天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16132/" title="北京欢乐谷天气" target="_blank">北京欢乐谷天气</a>
		<a href="//beihai.tianqi.com/" title="北海天气" target="_blank">北海天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/4193/" title="百花山天气" target="_blank">百花山天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16156/" title="北普陀影视城天气" target="_blank">北普陀影视城天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16155/" title="北宫国家森林公园天气" target="_blank">北宫国家森林公园天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16168/" title="地坛天气" target="_blank">地坛天气</a>
		<a href="http://www.tianqi.com/anhuijingdian/1551/" title="东岳庙天气" target="_blank">东岳庙天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16171/" title="蟹岛度假村天气" target="_blank">蟹岛度假村天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16176/" title="大钟寺天气" target="_blank">大钟寺天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16177/" title="都城隍庙天气" target="_blank">都城隍庙天气</a>
		<a href="http://www.tianqi.com/shandongjingdian/2765/" title="凤凰岭天气" target="_blank">凤凰岭天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/4163/" title="红螺寺天气" target="_blank">红螺寺天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16192/" title="后海天气" target="_blank">后海天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16203/" title="京东大峡谷天气" target="_blank">京东大峡谷天气</a>
		<a href="http://www.tianqi.com/beijingjingdian/16202/" title="居庸关天气" target="_blank">居庸关天气</a>
		<a href="http://www.tianqi.com/shanghaijingdian/16373/" title="横沙岛天气" target="_blank">横沙岛天气</a>
		<a href="http://www.tianqi.com/shanghaijingdian/16387/" title="上海城隍庙天气" target="_blank">上海城隍庙天气</a>
		<a href="http://www.tianqi.com/shanghaijingdian/16393/" title="佘山天天气" target="_blank">佘山天气</a>
		<a href="http://www.tianqi.com/shanghaijingdian/4203/" title="外滩天气" target="_blank">外滩天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/6143/" title="宝华山天气" target="_blank">宝华山天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/6201/" title="凤凰岛天气" target="_blank">凤凰岛天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/6111/" title="夫子庙天气" target="_blank">夫子庙天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16550/" title="虎丘山天气" target="_blank">虎丘山天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/6155/" title="寒山寺天气" target="_blank">寒山寺天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16558/" title="洪泽湖天气" target="_blank">洪泽湖天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16559/" title="花果山天气" target="_blank">花果山天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16565/" title="灵山大佛天气" target="_blank">灵山大佛天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/6142/" title="茅山天气" target="_blank">茅山天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16577/" title="太湖天气" target="_blank">太湖天气</a>
		<a href="http://www.tianqi.com/jiangsujingdian/16580/" title="天目湖天气" target="_blank">天目湖天气</a>
		<a href="http://www.tianqi.com/fujianjingdian/18699/" title="鼓山天气" target="_blank">鼓山天气天气</a>
		<a href="http://www.tianqi.com/fujianjingdian/18715/" title="南靖土楼天气" target="_blank">南靖土楼天气</a>
		<a href="http://www.tianqi.com/fujianjingdian/18731/" title="武夷山天气" target="_blank">武夷山天气</a>
		<a href="http://www.tianqi.com/fujianjingdian/6920/" title="湄洲岛天气" target="_blank">湄洲岛天气</a>
		<a href="http://www.tianqi.com/henanjingdian/2286/" title="白云山天气" target="_blank">白云山天气</a>
		<a href="http://www.tianqi.com/guangdongjingdian/19143/" title="丹霞山天气" target="_blank">丹霞山天气</a>
		<a href="http://www.tianqi.com/guangdongjingdian/19150/" title="东澳岛天气" target="_blank">东澳岛天气</a>
		<a href="http://www.tianqi.com/guangdongjingdian/19158/" title="大亚湾天气" target="_blank">大亚湾天气</a>
		<a href="http://www.tianqi.com/guangdongjingdian/19246/" title="华林寺天气" target="_blank">华林寺天气</a>
		<a href="http://www.tianqi.com/guangdongjingdian/19273/" title="葫芦山天气" target="_blank">葫芦山天气</a>
		<a href="http://www.tianqi.com/chongqingjingdian/16422/" title="朝天门天气" target="_blank">朝天门天气</a>
		<a href="http://www.tianqi.com/chongqingjingdian/16431/" title="歌乐山天气" target="_blank">歌乐山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/5105/" title="宝塔山天气" target="_blank">宝塔山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/5059/" title="大雁塔天气" target="_blank">大雁塔天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/17791/" title="翠华山天气" target="_blank">翠华山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/17786/" title="宝鸡天台山天气" target="_blank">宝鸡天台山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/5153/" title="华山天气" target="_blank">华山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/5187/" title="南宫山天气" target="_blank">南宫山天气</a>
		<a href="http://www.tianqi.com/shanxi1jingdian/5067/" title="骊山天气" target="_blank">骊山天气</a>
		<a href="http://www.tianqi.com/zhejiangjingdian/1779/" title="太白山天气" target="_blank">太白山天气</a>
	</div>
	<div style="display: none;">
	<a href="http://www.tianqi.com/air/beijing.html" target="_blank" title="北京空气质量">北京空气质量</a>
	<a href="http://www.tianqi.com/air/tianjin.html" target="_blank" title="天津空气质量">天津空气质量</a>
	<a href="http://www.tianqi.com/air/chongqing.html" target="_blank" title="重庆空气质量">重庆空气质量</a>
	<a href="http://www.tianqi.com/air/shanghai.html" target="_blank" title="上海空气质量">上海空气质量</a>
	<a href="http://www.tianqi.com/air/shijiazhuang.html" target="_blank" title="石家庄空气质量">石家庄空气质量</a>
	<a href="http://www.tianqi.com/air/suzhou.html" target="_blank" title="苏州空气质量">苏州空气质量</a></a>
	<a href="http://www.tianqi.com/air/hefei.html" target="_blank" title="合肥空气质量">合肥空气质量</a>
	<a href="http://www.tianqi.com/air/xian.html" target="_blank" title="西安空气质量">西安空气质量</a>
	<a href="http://www.tianqi.com/air/xiamen.html" target="_blank" title="厦门空气质量">厦门空气质量</a>
	<a href="http://www.tianqi.com/air/wuxi1.html" target="_blank" title="无锡空气质量">无锡空气质量</a>
	<a href="http://www.tianqi.com/air/lanzhou.html" target="_blank" title="兰州空气质量">兰州空气质量</a>
	<a href="http://www.tianqi.com/air/haerbin.html" target="_blank" title="哈尔滨空气质量">哈尔滨空气质量</a>
	<a href="http://www.tianqi.com/air/zhuhai.html" target="_blank" title="珠海空气质量">珠海空气质量</a>
	<a href="http://www.tianqi.com/air/lianyungang.html" target="_blank" title="连云港空气质量">连云港空气质量</a>
	<a href="http://www.tianqi.com/air/shenzhen.html" target="_blank" title="深圳空气质量">深圳空气质量</a>
	<a href="http://www.tianqi.com/air/nanjing.html" target="_blank" title="南京空气质量">南京空气质量</a>
	<a href="http://www.tianqi.com/air/chengdu.html" target="_blank" title="成都空气质量">成都空气质量</a>
	<a href="http://www.tianqi.com/air/jining.html" target="_blank" title="济宁空气质量">济宁空气质量</a>
	<a href="http://www.tianqi.com/air/xuzhou.html" target="_blank" title="徐州空气质量">徐州空气质量</a>
	<a href="http://www.tianqi.com/air/qingdao.html" target="_blank" title="青岛空气质量">青岛空气质量</a>
	<a href="http://www.tianqi.com/air/guangzhou.html" target="_blank" title="广州空气质量">广州空气质量</a>
	<a href="http://www.tianqi.com/air/hangzhou.html" target="_blank" title="杭州空气质量">杭州空气质量</a>
	<a href="http://www.tianqi.com/air/zhengzhou.html" target="_blank" title="郑州空气质量">郑州空气质量</a>
	<a href="http://www.tianqi.com/air/wuhan.html" target="_blank" title="武汉空气质量">武汉空气质量</a>
	<a href="http://www.tianqi.com/air/neimenggu.html" target="_blank" title="内蒙古空气质量">内蒙古空气质量</a>
	<a href="http://www.tianqi.com/air/taiwan.html" target="_blank" title="台湾空气质量">台湾空气质量</a>
	<a href="http://www.tianqi.com/air/aomen.html" target="_blank" title="澳门空气质量">澳门空气质量</a>
	<a href="http://www.tianqi.com/air/hongkong.html" target="_blank" title="香港空气质量">香港空气质量</a>
	<a href="http://www.tianqi.com/air/hainan.html" target="_blank" title="海南空气质量">海南空气质量</a>
	<a href="http://www.tianqi.com/air/guangdong.html" target="_blank" title="广东空气质量">广东空气质量</a>
	<a href="http://www.tianqi.com/air/yunnan.html" target="_blank" title="云南空气质量">云南空气质量</a>
</div>
	<div style="display: none;">
		<a href="http://www.tianqi.com/103010100.html" title="东京天气" target="_blank">东京天气</a></li>
		<a href="http://www.tianqi.com/107020100.html" title="胡志明天气" target="_blank">胡志明天气</a></li>
		<a href="http://www.tianqi.com/1120019.html" title="济州岛天气" target="_blank">济州岛天气</a></li>
		<a href="http://www.tianqi.com/singapore/" title="新加坡天气" target="_blank">新加坡天气</a></li>
		<a href="http://www.tianqi.com/cambodia/" title="柬埔寨天气" target="_blank">柬埔寨天气</a></li>
		<a href="http://www.tianqi.com/japan/" title="日本天气" target="_blank">日本天气</a></li>
		<a href="http://www.tianqi.com/indonesia/" title="印尼天气" target="_blank">印尼天气</a></li>
		<a href="http://www.tianqi.com/103020100.html" title="大阪天气" target="_blank">大阪天气</a></li>
		<a href="http://www.tianqi.com/106010100.html" title="曼谷天气" target="_blank">曼谷天气</a></li>
		<a href="//taibei.tianqi.com/" title="台北天气" target="_blank">台北天气</a></li>
		<a href="http://www.tianqi.com/124020100.html" title="迪拜天气" target="_blank">迪拜天气</a></li>
		<a href="http://www.tianqi.com/202010100.html" title="巴黎天气" target="_blank">巴黎天气</a></li>
		<a href="http://www.tianqi.com/2390203.html" title="威尼斯天气" target="_blank">威尼斯天气</a></li>
		<a href="http://www.tianqi.com/2140027.html" title="莫斯科天气" target="_blank">莫斯科天气</a></li>
		<a href="http://www.tianqi.com/italy/" title="意大利天气" target="_blank">意大利天气</a></li>
		<a href="http://www.tianqi.com/turkey/" title="土耳其天气" target="_blank">土耳其天气</a></li>
		<a href="http://www.tianqi.com/greece/" title="希腊天气" target="_blank">希腊天气</a></li>
		<a href="http://www.tianqi.com/united-kingdom/" title="英国天气" target="_blank">英国天气</a></li>
		<a href="http://www.tianqi.com/401110101.html" title="纽约天气" target="_blank">纽约天气</a></li>
		<a href="http://www.tianqi.com/3250087.html" title="西雅图天气" target="_blank">西雅图天气</a></li>
		<a href="http://www.tianqi.com/302010100.html" title="开普敦天气" target="_blank">开普敦天气</a></li>
		<a href="http://www.tianqi.com/mexico/" title="墨西哥城天气" target="_blank">墨西哥城天气</a></li>
		<a href="http://www.tianqi.com/502250100.html" title="圣保罗天气" target="_blank">圣保罗天气</a></li>
		<a href="http://www.tianqi.com/416010100.html" title="加拉加斯天气" target="_blank">加拉加斯天气</a></li>
		<a href="http://www.tianqi.com/401040101.html" title="洛杉矶天气" target="_blank">洛杉矶天气</a></li>
		<a href="http://www.tianqi.com/australia/" title="澳大利亚天气" target="_blank">澳大利亚天气</a></li>
		<a href="http://www.tianqi.com/new-zealand/" title="新西兰天气" target="_blank">新西兰天气</a></li>
		<a href="http://www.tianqi.com/fiji/" title="斐济天气" target="_blank">斐济天气</a></li>
		<a href="http://www.tianqi.com/canada/" title="加拿大天气" target="_blank">加拿大天气</a></li>
		<a href="http://www.tianqi.com/united-states/" title="美国天气" target="_blank">美国天气</a></li>
		<a href="http://www.tianqi.com/mexico/" title="墨西哥天气" target="_blank">墨西哥天气</a></li>
	</div>
</div>
<script type="text/javascript">
   
    $(document).ready(function(){
    	var idx;
		var _len = $('.hhx_newB_kindCon>div').length;
    	$('.hhx_newB_kindTit_ul li').click(function(e){
	        idx = $(this).index();
	        $(this).addClass('hhx_newB_on').siblings().removeClass('hhx_newB_on');
	        for(var i = 0;i<_len;i++){
	            if( i==idx ){
	                $('.hhx_newB_kindCon').find('div').eq(i).show().siblings().hide();
	            }
	        }
	    })
    })
</script>
</div>
<div class="clear10"></div>
<div id="links">
	<div class="links-content" style="padding-bottom: 35px;">
		<div class="href-title" id="myTop">
			<ul>
				<li class="hover" style="margin-right: 50px;">友情链接</li>
			</ul>

		</div>
		<div class="href-content" id="myCont">
				<div>
					<ul class="bt">
												<li><a href="http://time.tianqi.com/" target="_blank">北京时间</a></li>
												<li><a href="https://www.wenshu.com/" target="_blank">文书网</a></li>
											</ul>
				</div>
		</div>
		<div class="clear"></div>
	</div>
</div>
<div class="app_erweima" style="position: fixed;right: 100px;bottom: 80px;z-index: 9999;"><img src="/static/tianqi2021/img/app.png" alt=""></div>
<div style="width:100%;background:#f6f6f6;float:left;margin-top: 30px;">
    <div style="CLEAR: both"></div>

    <div id="footer">
       
            <div>
                <div class="hhx_footer_box">
                    <div class="hhx_fontfff16">导航网址：</div>
                    <div class="hhx_flexaBox">
                        <div class="hhx_flex_a clearfix" id="newindex_b1">
                            <a href="https://www.tianqi.com/chinacity.html" target="_blank">全国天气</a>
                            <a href="https://www.tianqi.com/beijingjingdian/" target="_blank">旅游天气</a>
                            <a href="https://www.tianqi.com/worldcity.html" target="_blank">国际天气</a>
                            <a href="https://lishi.tianqi.com" target="_blank">历史天气</a>
                            <a href="https://www.tianqi.com/news/" target="_blank">天气新闻</a>
                            <a href="https://www.tianqi.com/changshi/" target="_blank">天气常识</a>
                            <a href="https://www.tianqi.com/toutiao/" target="_blank">天气生活</a>
                        </div>
                        <div class="hhx_flex_a clearfix" id="newindex_b2">
                        	<a href="https://www.tianqi.com/toutiao/meishi/" target="_blank">城市美食</a>
                            <a href="https://www.tianqi.com/toutiao/techan/" target="_blank">城市特产</a>
                            <a href="https://www.tianqi.com/toutiao/lvyou/" target="_blank">城市景点</a>
                             <a href="https://www.tianqi.com/zhuanti/" target="_blank">最新专题</a>
                            <a href="https://www.tianqi.com/latest/" target="_blank">最近更新</a>
                            <a href="https://www.tianqi.com/air/" target="_blank">空气质量</a>
                            <a href="https://wannianli.tianqi.com" target="_blank">万年历查询</a>
                            <a href="https://wannianli.tianqi.com/jiemeng/" target="_blank">周公解梦</a>
                            
                        </div>
                    </div>
                </div>
              
                <div class="newIndex_load">
                	<div>客户端下载</div>
                	<img src="//static.tianqistatic.com/static/wap2018/ico1/erweimaCode.png"/>
                    <div class="large-img">
                        <img src="//static.tianqistatic.com/static/wap2018/ico1/erweimaCode.png"/>
                    </div>
                </div>
                <div class="newIndex_load">
                    <div>天气网公众号</div>
                    <img src="//static.tianqistatic.com/static/wap2018/ico1/wxerweima.jpg"/>
                    <div class="large-img">
                        <img src="//static.tianqistatic.com/static/wap2018/ico1/wxerweima.jpg"/>
                    </div>
                </div>

                <div class="newIndex_sugg">
                	<img src="//static.tianqistatic.com/static/wap2018/ico1/newIndex_sugg.png"/>
                	<a style="display: inline-block;" href="https://www.tianqi.com/fankui.html" target="_blank" title="意见反馈" rel="nofollow">
                		<div>意见反馈</div>
                		<div>举报邮箱:kf@tianqi.com</div> 
                	</a>
                </div>
                <div style="clear: both;"></div>
               </div>
            </div>
    </div>

    <div id="hhx_footer">
        <div class="hhx_footer_mid">
            Copyright &copy; 2009-2022            <a href="https://www.tianqi.com" target="_blank">www.tianqi.com 天气网</a>
            . All Rights Reserved. <a href="http://beian.miit.gov.cn" target="_blank">渝ICP备18012671号-2</a>
            <p style="margin: 16px 0 18px 0;text-align: center;">
            	温馨提示：数据来源中国气象局，仅供参考
            </p>
			 
			<p style="margin: 16px 0 18px 0;text-align: center;">
				<text style="color:#666;white-space: nowrap;magin-bottom:10px">本站部分文字内容、图片选取自网络，如侵权请联系删除，<a style="color:#fff" href="https://www.tianqi.com/fankui.html" target="_blank" title="意见反馈" rel="nofollow">联系邮箱:kf@tianqi.com</a></text>
			</p>
            <a href="http://www.12377.cn/node_552908.htm" target="_blank" title="举报链接" style="width:110px;height:32px;border: 1px solid #636363;display:inline-block;background:url('//static.tianqistatic.com/static/wap2018/ico1/index_jubao.png') no-repeat center center;">
            </a>
			<div style="width:300px;margin:0 auto; padding: 0 0 20px 0;">
				<img src="//static.tianqistatic.com/static/tianqi2018/images/beian.png" />
				<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=50010302002269" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img src="" style="float:left;"/><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">渝公网安备 50010302002269号</p></a>
			</div>
        </div>
    </div>
</div>


<script language="javascript">
    // $(function(){
    //     $(".newIndex_load > img").mouseover(function(){
    //         $(this).siblings('.large-img').css('display','block');
    //     });
    //     $(".newIndex_load > img").mouseout(function(){
    //         $(this).siblings('.large-img').css('display','none');
    //     });
    // });
    var _hmt = _hmt || [];
    (function() {
        var hm = document.createElement("script");
        hm.src = "https://hm.baidu.com/hm.js?ab6a683aa97a52202eab5b3a9042a8d2";
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(hm, s);
    })();
	//document.onselectstart = new Function("event.returnValue=false");

</script>
<div style="display: none;">
    <script src="https://s96.cnzz.com/z_stat.php?id=1275796416&web_id=1275796416" language="JavaScript"></script>
</div>
<script src="//static.tianqistatic.com/static/common/js/headerCommon.js"></script>

<script>
    (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
    // 禁用f12及复制
    //document.onselectstart=function(){return false;};
      //    window.oncontextmenu=function(){return false;}
        //   window.onkeydown = window.onkeyup = window.onkeypress = function (event) { 
        //  if(event.code == 'F12'){
        //    window.event.returnValue = false; 
        //     return false;
        //   }
        //  } 
</script>
<!--<script src="//static.tianqistatic.com/static/dist/js/search.3e996.js"></script>-->
<script src="//static.tianqistatic.com/static/tianqi2018/js/search.js"></script>
<div class="tongji" style="display:none;">
	<script type="text/javascript" src="https://s5.cnzz.com/z_stat.php?id=1277722738&web_id=1277722738"></script>
</div>
	<script>
        $(document).ready(function () {
            $(".showall").click(function () {
                $(this).hide();
                $(".youbian").css("height", "auto");
            });
        });
	</script>
<script>
	$('.new_news_zixun li').mouseover(function(){
		$(this).addClass('active').siblings().removeClass('active')
	})

    function setCity(el) {
		var cityid=$(el).val();
		$.ajax({
			type: "GET",
			url:`https://youbian.tianqi.com/ajaxyburl?c=quhao&a=ajax&provid=${cityid}&tp=yb`,
			dataType: "jsonp",
		    success: function(data){
				var str='<option value="">选择城市</option>';
				data.map(i=>{
					str+=`<option value=${i.id}>${i.name}</option>`
				})
                $('#cityid').html(str)
			}
		})
	}
	function setArea(el) {
		var cityid=$(el).val();
		$.ajax({
			type: "GET",
			url:`https://youbian.tianqi.com/ajaxyburl?c=quhao&a=ajax&cityid=${cityid}`,
			dataType: "jsonp",
		    success: function(data){
				var str='<option value="">选择区县</option>';
				data.map(i=>{
					str+=`<option value=${i.id}>${i.name}</option>`
				})
                $('#areaid').html(str)
			}
		})
	}
	function JumpCity() {
		var pid=$('#provid').val(),cityid=$('#cityid').val(),aid=$('#areaid').val();
		window.location.href=`https://youbian.tianqi.com/searchCity?c=quhao&a=ajaxyburl&cityid=${cityid}&provid=${pid}&areaid=${aid}`
	}
</script>

</body>
</html>

""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
