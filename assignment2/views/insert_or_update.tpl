% include('header.tpl')

<a href="/delete_year">
	Delete by year
</a>

<form action="/insert_or_update" method="POST">
	<input name="_id" type="text" placeholder="Your name" />
	<input name="country" type="text" placeholder="Country" />
	<input name="zip" type="text" placeholder="Zip" />
	<input name="email" type="text" placeholder="Email" />
	<input name="gender" type="text" placeholder="Gender" />
	<input name="likes" type="text" placeholder="Likes" />
	<input name="password" type="text" placeholder="Password" />
	<input name="year" type="text" placeholder="Year" />

	<input type="submit" value="Send me!">
</form>
