<link rel="stylesheet" href="/static/style.css">

<h1>
	Edit @{{user['_id']}} email
</h1>

<form action="/change_email" method="POST">

	% for key in user:
		% if key == "email":
			<div class="input">
				<legend id="{{ key }}">{{ key }}</legend>
				<input name="{{ key }}" type="text" value="{{user[key]}}" />
			</div>
		% elif key == "_id":
			<p> 
				{{key}}: {{user[key]}} 
				<b>(Id can not be changed)</b>
			</p>
		% else:
			<p> {{key}}: {{user[key]}}</p>
		% end
	% end
	
	<input type="submit" value="Send me!">
</form>
