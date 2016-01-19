	
	<h1>Sign up TOTP</h1>

	% if signup:
	<form action="/signup_totp" method="POST">
	% else:
	<form action="/login_totp" method="POST">
	%end

		<p> 
			<label for="username" class="username" data-icon="u">Your username</label>
			<input  class="inputField" id="username" name="username" required="required" type="text" placeholder="Username" />
		</p>

		<p> 
			<label for="password" class="youpasswd" data-icon="p">Your password </label> 
			<input  class="inputField" id="password" name="password" required="required" type="password" placeholder="eg. X8df!90EO"/>
		</p>

		% if not signup:

			<p> 
				<label for="totpCode" class="youpasswd" data-icon="p">Your totp code</label> 
				<input  class="inputField" id="totpCode" name="totpCode" required="required" placeholder="eg. X8df!90EO"/>
			</p>

		% else:
			<p> 
				<label for="password" class="youpasswd" data-icon="p">Retype the password </label> 
				<input  class="inputField" id="password2" name="password2" required="required" type="password" placeholder="eg. X8df!90EO"/>
			</p>

			<p> 
				<label for="email" class="youmail" data-icon="e" >Your email</label>
				<input  class="inputField" id="email" name="email" required="required" type="email" placeholder="mysupermail@mail.com"/> 
			</p>
			
			<p>
				<label for="name" class="uname" data-icon="u">Your name</label>
				<input  class="inputField" id="name" name="name" required="required" type="text" placeholder="Your name" />
			</p>
			
			<p>
				<label for="country" class="ucountry" data-icon="u">Your country</label>
				<input  class="inputField" id="country" name="country" required="required" type="text" placeholder="Your country" />
			</p>

		% end

		<p class="signin button"> 
			<input  class="submitField" type="submit" value="Sign up"/>
		</p>

	</form>

	% if signup:
		<p class="change_link">  
			Already a member ?
			<a href="/login" class="to_register"> Go and log in </a>
		</p>
	% else:
		<p class="change_link">  
			Do you need an account?
			<a href="/signup" class="to_register"> Go and signup </a>
		</p>
	% end
