<template>
	<div>
		<span v-html="marked(title)"></span>
		<span v-html="marked(msg)"></span>
	</div>
</template>

<script>
var marked = require('marked');

export default {
	name: 'ConclusionPage',
	data: function() {
		return {
			title: '# Assessment',
			msg: '## Hello World'
		};
	},
	methods: {
		marked: function(markdown) {
			return marked(markdown);
		}
	}
}
</script>

<style scoped>
h3 {
	margin: 40px 0 0;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}
</style>
