<template>
	<div>
		<span v-html="marked(title)"></span>
		<span v-html="marked(msg)"></span>
	</div>
</template>

<script>
var marked = require('marked');

export default {
	name: 'HomePage',
	data: function() {
		return {
			title: '# What, Then, is an American',
			msg: '## There is no place on earth that remain untouched from the influence of America. ' +
				'As one of the strongest countries in the world, it wields incredible powers and opportunities. ' +
				'But behind the superfluous exaggerations, there lies the true reason for which it has grown by. ' +
				'Benjamin Franklin started his career without a dime in his pocket, growing to unimaginable heights. ' +
				'George Washington went from a farmer to one of the most honorable men in America. ' +
				'Those achievements were inconceivable averywhere else in the world because of caste systems ' +
				'and royal families. Truth is, the only trait that matters is not the royal status, ' +
				'not the glaring accomplishments made by your ancestors, but your usefulness to society.'
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
