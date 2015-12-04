<link rel="stylesheet" href="/static/style.css">

<h1>
	@{{user['_id']}} profile
</h1>

<p>
	<a href="/{{user['_id']}}/edit">
		Edit profile
	</a>
</p>

%for i in user:
	<p> {{i}}: {{user[i]}}</p>
% end