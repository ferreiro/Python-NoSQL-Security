
	<form action="/signup" method="POST">
		<p>
			<label for="name" class="uname" data-icon="u">Your name</label>
			<input  class="inputField" id="name" name="name" required="required" type="text" placeholder="Your name" />
		</p>
		<p> 
			<label for="username" class="username" data-icon="u">Your username</label>
			<input  class="inputField" id="username" name="username" required="required" type="text" placeholder="Username" />
		</p> 
		<p> 
			<label for="email" class="youmail" data-icon="e" > Your email</label>
			<input  class="inputField" id="email" name="email" required="required" type="email" placeholder="mysupermail@mail.com"/> 
		</p>
		<p> 
			<label for="password" class="youpasswd" data-icon="p">Your password </label> 
			<input  class="inputField" id="password" name="password" required="required" type="password" placeholder="eg. X8df!90EO"/>
		</p>
		<p> 
			<label for="password" class="youpasswd" data-icon="p">Retype the password </label> 
			<input  class="inputField" id="password2" name="password2" required="required" type="password" placeholder="eg. X8df!90EO"/>
		</p>
		<p class="signin button"> 
			<input  class="submitField" type="submit" value="Sign up"/>
			<p class="change_link">  
				Already a member ?
				<a href="/login" class="to_register"> Go and log in </a>
			</p>
		</p>
	</form>

