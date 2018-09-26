<template>
	<div>
		<span v-html="marked(title)"></span>
		<div style="display: flex">
			<span v-html="marked(msg)"></span>
			<img src="http://www.pngall.com/wp-content/uploads/2016/06/Statue-of-Liberty-PNG.png" width="30%" height="50%"/>
		</div>
	</div>
</template>

<script>
var marked = require('marked');

export default {
	name: 'SecondPage',
	data: function() {
		return {
			title: '# Equal Opportunities',
			msg: '## Hard work is meaningless if it bases off an uneven foundation; ' +
				'a foundation of which free citizens are cheated in is no better than a ' +
				'foundation of slaves being rob of their freedom. We Americans hold a unique identity, ' +
				'“Here individuals of all nations are melted into a new race of men”; the only trait ' +
				'that holds any importance in America is your usefulness toward society. ' +
				'Thus, in America, we put it as the top priority to ensure that “All men are equal”, ' +
				'as proclaimed in the Declaration of Independence. We trust that this proclamation shall ' +
				'act upon the interest of all citizen and create a country where every citizen will be ' +
				'treated equally regardless of their race, religion, or political belief. In doing so, ' +
				'we act as a beacon to welcome all immigrants alike to America, and most importantly ' +
				'create a balanced foundation for all citizens. Admitted by the founding fathers who ' +
				'“turned away from the traditional reliance upon religious sanction and engineered a ' +
				'new paradox, what could be called a secular revelation…[Abraham] Lincoln urged a cult ' +
				'of the Constitution, a worship of ‘the Constitution and its laws,’ as the only reliable ' +
				'mean to preserve the legacy of self-government.  ‘Let it become,’ he proclaimed, ‘the ' +
				'political religion of the nation”. This idea of a country separated from religion creates ' +
				'a strong basis by which no religious bias were envolved and all laws are solely based on ' +
				'logic and the will of the people. Beyond that, we have also imprinted these ideologies in multiple ' +
				'foundational documents, such as ruling 1.3.7, which strip senators of their protection ' +
				'during office, which reduces the risk that corrupted official will abuse their power, ' +
				'or the first amendment which secures the freedom of speech, religion, assembly, and position. ' +
				'These are laws that retains the balance which has helped countless others in our society to succeed. ' +
				'The most recognizable example of the equality provided in America is Barack Obama, who became the 44th ' +
				'president of the United State in 2008, and also the first African American president; With an African ' +
				'American agenda, Barack Obama reinforced the statement in all the preceding documents. America has held ' +
				'a strong, unshaken foundation of equality, but it is up to you to decide how tall to construct the building.'
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
