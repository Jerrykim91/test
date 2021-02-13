
```html
<!-- extends from base.html -->
{% extends 'blog/base.html'%}

<!-- title -->
{% block title %}Link List{% endblock %}

{% load static %}


<!-- contents -->
{% block content %}

<div id="main">
    <header class="major">
        <h1>book mark</h1>
    </header>

    <section class="posts">

        {% for Link in object_list %}
        <article>
            <header>
                <!--<span class="date">April 24, 2017</span>-->
                <h2><a href="{% url 'linkList:link_detail' Link.id %}">{{ Link.title }}</a></h2>
            </header>

            <div>
                <a href="{{ Link.url }}" class="image fit">
                    <!-- <img src="{% static 'images/pic02.jpg' %}" alt="" /> -->
                </a>
                <p>{{ Link.content }}</p>
                <!-- <p id="txt" hidden>{{ Link.url }}</p> -->
            </div>

            <!-- https://ko.grabz.it/api/python/image-capture-options/ -->
            <!--테스트 란 만들기-->
            <!-- <input value="{{ Link.url }}" placeholder="이곳에 ctrl+v로 붙여넣기 테스트" type="text" > -->
            <br />

            <!--복사할 텍스트 만들기-->
            <p id="text1">텍스트 복사에 성공 하였습니다. </p>

            <!--// 버튼 만들기-->
            

            <!--input 란 만들기-->
            <br /><br /><input placeholder="이곳에 ctrl+v로 붙여넣기 테스트" type="text">

            <!--// 버튼 만들기-->
            <ul class="actions special">
                <button onclick="copyToClipboard('text1')">텍스트 복사하기</button>
                <!-- <li><button onclick="copyToClipboard('txt')"> 링크 복사[X] </button></li> -->
                <li><a href="{{Link.url}}" class="button" target="_blank"> 링크로 이동 </a></li>
            </ul>
        </article>
        {% endfor %}
    </section>

    <!-- pagination -->
    <footer>
        <div class="pagination">
            <!-- Prev page setting -->
            {% if page_obj.has_previous %}
            <a href="?page={{ page_obj.previous_page_number }}" class="previous">Prev</a>
            {% endif %}

            <!--  main : page pagination   -->
            {% for page_number in page_obj.paginator.page_range %}
            <!-- pagination lv control  -->
            {% if page_number >= page_obj.number|add:-5 and page_number <= page_obj.number|add:5 %} <!-- page number
                match-->
                {% if page_number == page_obj.number %}
                <li class="page-item active">
                    <a class="page" href="?page={{ page_number }}">{{ page_number }}</a>
                </li>
                {% else %}
                <li class="page-item">
                    <a class="page" href="?page={{ page_number }}">{{ page_number }}</a>
                </li>
                {% endif %}
                {% endif %}
                {% endfor %}

                <!-- next page setting -->
                {% if page_obj.has_next %}
                <!-- 마지막 page -->
                <a href="?page={{ page_obj.paginator.num_pages }}" class="page">{{ page_obj.paginator.num_pages }}</a>
                <!-- 바로 다음 page -->
                <a href="?page={{ page_obj.next_page_number }}" class="next">Next</a>
                {% endif %}
        </div>
    </footer>

    <br />
</div>

{% endblock %}
```

```html
<script>

// 클립보드로 복사하는 기능을 생성
function copyToClipboard(elementId) {

  // 글을 쓸 수 있는 란을 만든다.
  var aux = document.createElement("input");

  // 지정된 요소의 값을 할당 한다.
  aux.setAttribute("value", document.getElementById(elementId).innerHTML);

  // bdy에 추가한다.
  document.body.appendChild(aux);

  // 지정된 내용을 강조한다.
  aux.select();

  // 텍스트를 카피 하는 변수를 생성
  document.execCommand("copy");

  // body 로 부터 다시 반환 한다.
  document.body.removeChild(aux);

}
</script>


<!--복사할 텍스트 만들기-->
<p id="text1">텍스트 복사에 성공 하였습니다. </p>

  <!--// 버튼 만들기-->
<button onclick="copyToClipboard('text1')">텍스트 복사하기</button>

  <!--input 란 만들기-->
<br /><br /><input placeholder="이곳에 ctrl+v로 붙여넣기 테스트" type="text">

```



```html
    <!-- pagination -->
    <footer>
        <div class="pagination">
            {% if page_obj.has_previous %}
                <a href="?page={{ page_obj.previous_page_number }}" class="previous">Prev</a>
                <a href="?page=1" class="page active">1</a>
            {% endif %}
            <!-- <span>{{ post.num_pages }}</span> -->
            <span>{{ page_obj.number }}</span>
            <!-- <a href="#" class="page active">{{ page_obj.number }}</a> -->
            {% if page_obj.has_next %}
            <!-- 마지막 page -->
                <a href="?page={{ page_obj.paginator.num_pages }}" class="page">{{ page_obj.paginator.num_pages }}</a>
                <!-- 바로 다음 page -->
                <a href="?page={{ page_obj.next_page_number }}" class="next">Next</a>
            {% endif %}
        </div>
    </footer>
```




```html
 <!-- Errors -->
        {% if not form.errors %}
        <h4> Please enter your uername and password twice. </h4>
        {% else %}
        <h4>Wrong! Please, correct the error(s) below. Please try again.</h4>
        <div class="alert alert-danger right" role="alert">
            {{ form.errors }}
        </div>
        {% endif %}

```


```html

{% extends 'blog/base.html'%}

<!-- {% load static %} -->
{% load widget_tweaks %}
{% block title %} Login {% endblock %}

{% block content %}
<!-- Main -->
<div id="main">
    <article class="special">
        <h2>테스트 </h2>
        <h2> ID 와 PW를 입력해주세요. </h2>
        {% if form.errors %}
        <div class="alertalert-danger">
            <div> 아래의 에러를 확인하세요. </div>
            {{ form.errors }}
        </div>
        {% endif %}

        <form action="." method='post' class="card pt-3">{% csrf_token %}
            <div class="form-grop row">
                {{ form.username|add_label_class : "col-form-label col-sm-2 ml-3 font-weight-bold" }}
                <div class="col-sm-5">
                    {{ form.username|add_class : "form-control"|attr : "autofocus" }}
                </div>
            </div>

            <div class="form-grop row">
                {{ form.password|add_label_class : "col-form-label col-sm-2 ml-3 font-weight-bold" }}
                <div class="col-sm-5">
                    {{ form.password|add_class : "form-control" }}
                </div>
            </div>

            <div class="form-group">
                <div class="offset-sm-2 col-sm-5">
                    <input type="submit" value="Log in" class="button" />
                    <input type="hidden" name="next" value="{{ next }}" />
                </div>
            </div>
        </form>
    </article>

</div>
{% endblock %}

```


```py

# Post_all
<!-- <th>{% post.index %}</th> -->
{{ post.modify_dt|date:'N d, Y' }}
<h3><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h3>
<P> 요약 : {{ post.description }}</P>
<hr>
{% endfor %}


```



```html
<!-- 원본 -->
<div id="main">

    <!-- Post -->
    <section class="post">
        <header class="major">
            <!-- <h2>{{ meposts.title }}</h2> -->
            <!-- 다음글 -->

            <div class="image main"><img src="{% static 'images/pic01.jpg' %}" alt="" /></div>
            <!-- <p>{{ meposts.body|linebreaks }}</p> -->
        </header>
    </section>

</div>
```



```html




<!DOCTYPE HTML>
<html>
	<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>Suitcase Template</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="description" content="" />
	<meta name="keywords" content="" />
	<meta name="author" content="" />

  <!-- Facebook and Twitter integration -->
	<meta property="og:title" content=""/>
	<meta property="og:image" content=""/>
	<meta property="og:url" content=""/>
	<meta property="og:site_name" content=""/>
	<meta property="og:description" content=""/>
	<meta name="twitter:title" content="" />
	<meta name="twitter:image" content="" />
	<meta name="twitter:url" content="" />
	<meta name="twitter:card" content="" />

	<!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
	<link rel="shortcut icon" href="favicon.ico">

	<link href="https://fonts.googleapis.com/css?family=Inconsolata:400,700" rel="stylesheet">
	
	<!-- Animate.css -->
	<link rel="stylesheet" href="css/animate.css">
	<!-- Icomoon Icon Fonts-->
	<link rel="stylesheet" href="css/icomoon.css">
	<!-- Bootstrap  -->
	<link rel="stylesheet" href="css/bootstrap.css">
	<!-- Flexslider  -->
	<link rel="stylesheet" href="css/flexslider.css">
	<!-- Flexslider  -->
	<link rel="stylesheet" href="css/flexslider.css">
	<!-- Owl Carousel -->
	<link rel="stylesheet" href="css/owl.carousel.min.css">
	<link rel="stylesheet" href="css/owl.theme.default.min.css">

	<link rel="stylesheet" href="css/style.css">


	<!-- Modernizr JS -->
	<script src="js/modernizr-2.6.2.min.js"></script>
	<!-- FOR IE9 below -->
	<!--[if lt IE 9]>
	<script src="js/respond.min.js"></script>
	<![endif]-->

	</head>
	<body>

	<nav id="colorlib-main-nav" role="navigation">
		<a href="#" class="js-colorlib-nav-toggle colorlib-nav-toggle active"><i></i></a>
		<div class="js-fullheight colorlib-table">
			<div class="colorlib-table-cell js-fullheight">
				<ul>
					<li><a href="index.html">Home</a></li>
					<li><a href="work.html">Work</a></li>
					<li><a href="services.html">Services</a></li>
					<li><a href="blog.html">Case Studies</a></li>
					<li><a href="about.html">About</a></li>
					<li><a href="contact.html">Contact</a></li>
				</ul>
			</div>
		</div>
	</nav>
	
	<div id="colorlib-page">
		<header>
			<div class="container">
				<div class="row">
					<div class="col-md-12">
						<div class="colorlib-navbar-brand">
							<a class="colorlib-logo" href="index.html">Suitcase</a>
						</div>
						<a href="#" class="js-colorlib-nav-toggle colorlib-nav-toggle"><i></i></a>
					</div>
				</div>
			</div>
		</header>
		<aside id="colorlib-hero">
			<div class="flexslider">
				<ul class="slides">
			   	<li style="background-image: url(images/cover_img_2.jpg);">
			   		<div class="overlay"></div>
			   		<div class="container">
			   			<div class="row">
				   			<div class="col-md-8 col-sm-12 col-xs-12 col-md-offset-2 text-center slider-text">
				   				<div class="slider-text-inner">
				   					<h2>Know Me</h2>
				   					<h1>About Me</h1>
				   				</div>
				   			</div>
				   		</div>
			   		</div>
			   	</li>
			  	</ul>
		  	</div>
		</aside>

		<div id="colorlib-about">
			<div class="container">
				<div class="row">
					<div class="col-md-5 animate-box">
						<img class="img-responsive img-about" src="images/about-img.jpg" alt="author">
					</div>
					<div class="col-md-7 animate-box">
						<div class="about">
							<p class="intro">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>
							<p><a href="work.html">View My Works</a></p>
							<p class="colorlib-social-icons">
								<a href="#"><i class="icon-facebook4"></i></a>
								<a href="#"><i class="icon-twitter3"></i></a>
								<a href="#"><i class="icon-googleplus"></i></a>
								<a href="#"><i class="icon-dribbble2"></i></a>
							</p>
							<span>&mdash; Trish Gates, CEO, Founder</span>
						</div>
						<div class="row">
							<div class="col-md-6">
								<p><strong>Far far away, behind the word mountains</strong>, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean</p>
							</div>
							<div class="col-md-6">
								<p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="colorlib-counter" class="colorlib-counters">
			<div class="container">
				<div class="row">
					<div class="col-md-8 col-md-offset-2 text-center animate-box intro-heading">
						<h2>Fun Facts</h2>
						<p>A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.</p>
					</div>
				</div>
				<div class="row animate-box">
					<div class="col-md-10 col-md-offset-1">
						<div class="row">
							<div class="col-md-4 text-center">
								<span class="colorlib-counter js-counter" data-from="0" data-to="456" data-speed="5000" data-refresh-interval="50"></span>
								<span class="colorlib-counter-label">Coffee</span>
							</div>
							<div class="col-md-4 text-center">
								<span class="colorlib-counter js-counter" data-from="0" data-to="899" data-speed="5000" data-refresh-interval="50"></span>
								<span class="colorlib-counter-label">Done Projects</span>
							</div>
							<div class="col-md-4 text-center">
								<span class="colorlib-counter js-counter" data-from="0" data-to="2000" data-speed="5000" data-refresh-interval="50"></span>
								<span class="colorlib-counter-label">Subscribers</span>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="colorlib-testimony" class="colorlib-light-grey">
			<div class="container">
				<div class="row">
					<div class="col-md-8 col-md-offset-2 text-center animate-box intro-heading">
						<h2>Our Client Says:</h2>
					</div>
				</div>
				<div class="row">
					<div class="col-md-12">
						<div class="row animate-box">
							<div class="owl-carousel1">
								<div class="item">
									<div class="testimony-slide text-center active">
										<figure>
											<img src="images/person1.jpg" alt="user">
										</figure>
										<blockquote>
											<p><i class="icon-quotes-left"></i> Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>
											<span>Andrew Field, Blogger</span>
										</blockquote>
									</div>
								</div>
								<div class="item">
									<div class="testimony-slide text-center active">
										<figure>
											<img src="images/person2.jpg" alt="user">
										</figure>
										<blockquote>
											<p><i class="icon-quotes-left"></i> Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>
											<span>Mark Bubble, Web Designer</span>
										</blockquote>
									</div>
								</div>
								<div class="item">
									<div class="testimony-slide text-center active">
										<figure>
											<img src="images/person3.jpg" alt="user">
										</figure>
										<blockquote>
											<p><i class="icon-quotes-left"></i> Far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>
											<span>Adam Smith, Guest</span>
										</blockquote>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div id="colorlib-hire" class="colorlib-light-grey">
			<div class="container">
				<div class="row">
					<div class="col-md-10 col-md-offset-1 col-md-pull-1 animate-box">
						<h2 class="heading">Are you looking for a web designer?</h2>
						<p><a href="#" class="btn btn-primary btn-lg">Available for Hire!</a></p>
					</div>
				</div>
			</div>
		</div>

		<footer>
			<div id="footer">
				<div class="container">
					<div class="row">
						<div class="col-md-4 col-pb-sm">
							<div class="row">
								<div class="col-md-10">
									<h2>Suitcase</h2>
									<p>A small river named Duden flows by their place and supplies it with the necessary regelialia.</p>
									<div class="row">
										<div class="col-md-6">
											<p>From the countries Vokalia and Consonantia</p>
										</div>
										<div class="col-md-6">
											<p>Far far away, behind the word mountains</p>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col-md-4 col-pb-sm">
							<h2>Newsletter</h2>
							<p>A small river named Duden flows by their place and supplies it with the necessary regelialia</p>
							<div class="subscribe text-center">
								<div class="form-group">
									<input type="text" class="form-control text-center" placeholder="Enter Email address">
									<input type="submit" value="Subscribe" class="btn btn-primary btn-custom">
								</div>
							</div>
						</div>
						<div class="col-md-4 col-pb-sm right-display">
							<h2>Follow Us</h2>
							<p class="colorlib-social-icons colorlib-social-icons2">
								<a href="#"><i class="icon-facebook4"></i></a>
								<a href="#"><i class="icon-twitter3"></i></a>
								<a href="#"><i class="icon-googleplus"></i></a>
								<a href="#"><i class="icon-dribbble2"></i></a>
							</p>
							<p>
								<span class="block"><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="icon-heart2" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --><br></span> 
								<span class="block">Demo Images: <a href="http://nothingtochance.co/" target="_blank">nothingtochance.co</a> <a href="http://unsplash.co/" target="_blank">Unsplash</a></span>
							</p>
						</div>
					</div>
				</div>
			</div>
		</footer>
	
	</div>

	<!-- jQuery -->
	<script src="js/jquery.min.js"></script>
	<!-- jQuery Easing -->
	<script src="js/jquery.easing.1.3.js"></script>
	<!-- Bootstrap -->
	<script src="js/bootstrap.min.js"></script>
	<!-- Waypoints -->
	<script src="js/jquery.waypoints.min.js"></script>
	<!-- Flexslider -->
	<script src="js/jquery.flexslider-min.js"></script>
	<!-- Counters -->
	<script src="js/jquery.countTo.js"></script>
	<!-- Owl Carousel -->
	<script src="js/owl.carousel.min.js"></script>

	<!-- Main JS (Do not remove) -->
	<script src="js/main.js"></script>

	</body>
</html>


```