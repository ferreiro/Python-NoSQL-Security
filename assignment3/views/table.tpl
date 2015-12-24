<h1>Hi! I'm a table</h1>

<style type="text/css">
	
.entry {
	width: 100%;
	border-bottom:1px dashed #cecece;
}
.column {
	display:  inline-block;
	padding-right: 10px;
	margin-right: 10px;
	border-right:1px dashed #cecece;
	padding:10px 0;
}

</style>

<h3>
	<strong>{{totalResults}}</strong> results found
</h3>


% for c in userList:
	
	<div class="entry">
	% for d in c:
		<div class="column">
			% if d == 'likes':
				% for like in c[d]:
 					{{like}}
				% end
			% else:
				{{c[d]}}
			%end
		</div>
	%end
	</div>
	
% end