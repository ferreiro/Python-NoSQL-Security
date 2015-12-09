% include('header.tpl')

<h1>
	Delete user by username
</h1>

<form action="/delete" method="POST">

	<div class="input">
		<p>Username</p>
		<input name="_id" type="text" value="" placeholder="Username" />
	</div>

	<input type="submit" value="Send me!">
</form>
