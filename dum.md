```py

# Post_all
<!-- <th>{% post.index %}</th> -->
{{ post.modify_dt|date:'N d, Y' }}
<h3><a href="{{ post.get_absolute_url }}">{{ post.title }}</a></h3>
<P> 요약 : {{ post.description }}</P>
<hr>
{% endfor %}


```