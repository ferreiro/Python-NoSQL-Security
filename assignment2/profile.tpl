<link rel="stylesheet" href="/static/style.css">

<h1>
	@{{user['_id']}} profile
</h1>

<p>
	<a href="/{{user['_id']}}/edit">
		Change email
	</a>

	<form action="/delete" method="post">
	    <a href="javascript:;" onclick="parentNode.submit();">Delete user<%=n%></a>
	    <input type="hidden" name="_id" value="{{user['_id']}}"/>
	</form>
</p>

%for key in user:
	% if key == 'likes':
		<p>
			<b>Tags:</b>
			%for l in user[key]:
				<span class="tag">
					{{l}}
				</span>
			%end
		</p>
	% else:
		<p> {{key}}: {{user[key]}}</p>
	% end 
% end