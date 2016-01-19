
<h1>Welcome {{ user['name'] }}!!!</h1>
<p>Do you want to protect your account? Register your second factor authenticator!!!</p>

<img src="{{qrcode}}" />

{{qrcode}}

<p>
	More options on your account
</p>
<ul>
	<li>
		<a href="/change_password">Change password</a>
	</li>
</ul>
