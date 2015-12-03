<link rel="stylesheet" href="/static/style.css">

<form action="/change_email" method="POST">

	% for key in user:
		<div class="input">
			<legend id="{{ key }}">{{ key }}</legend>
			<input name="{{ key }}" type="text" value="{{user[key]}}" />
		</div>
	% end
	
	<input type="submit" value="Send me!">
</form>
