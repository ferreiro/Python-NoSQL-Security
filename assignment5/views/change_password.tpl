
	<form action="/change_password" method="POST">
		<p> 
			<label for="username" class="username" data-icon="u">Your username</label>
			<input  class="inputField" id="username" name="username" required="required" type="text" placeholder="Username" />
		</p> 
		<p> 
			<label for="oldpassword" class="youpasswd" data-icon="p">Old password </label> 
			<input  class="inputField" id="oldpassword" name="oldpassword" required="required" type="password" placeholder="Your password"/>
		</p>
		<p> 
			<label for="newpassword" class="youpasswd" data-icon="p">New password </label> 
			<input  class="inputField" id="newpassword" name="newpassword" required="required" type="password" placeholder="Your new password"/>
		</p>
		<p class="signin button"> 
			<input  class="submitField" type="submit" value="Sign up"/>
		</p>
	</form>

