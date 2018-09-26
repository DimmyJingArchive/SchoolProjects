<template>
	<div>
		<span v-html="marked(title)"></span>
		<div style="display: flex">
			<span v-html="marked(msg)"></span>
			<img src="http://www.pngmart.com/files/4/Statue-of-Liberty-Transparent-Background.png" width="30%" height="50%"/>
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
				'a foundation of which free citizens are cheated is no better than a ' +
				'foundation of slaves being rob of their freedom. We American hold a unique identity, ' +
				'“Here individuals of all nations are melted into a new race of men”; the only trait ' +
				'that holds any importance in America is your usefulness toward society. ' +
				'Thus, in America, we put it as the top priority to ensure that “All men are equal”, ' +
				'as proclaimed in the Declaration of Independence. We trust that this proclamation shall ' +
				'act upon the interest of all citizen and create a country where every citizen will be ' +
				'treated equally regardless of their race, religion, or political belief. In doing so, ' +
				'we act as a beacon to welcome all immigrants alike to America, and most importantly ' +
				'create a balanced foundation for all citizen. Admitted by the founding fathers who ' +
				'“turned away from the traditional reliance upon religious sanction and engineered a ' +
				'new paradox, what could be called a secular revelation…[Abraham] Lincoln urged a cult ' +
				'of the Constitution, a worship of ‘the Constitution and its laws,’ as the only reliable ' +
				'mean to preserve the legacy of self-government.  ‘Let it become,’ he proclaimed, ‘the ' +
				'political religion of the nation”. This idea of a country separated from religion create ' +
				'a strong base by which no religious bias were envolved and all laws are solely based on ' +
				'the will of the people. Beyond that, we have also imprinted these ideologies in multiple ' +
				'foundational documents, such as ruling 1.3.7, which strip senators of their protection ' +
				'during office which reduce the risk that corrupted official will abuse their power, ' +
				'or the first amendment which secures the freedom of speech, religion, assembly, and position' +
				'. These are qualities that we practice daily today in America, which helps retain the balance ' +
				'that has helped countless others in our society to succeed. The most recognizable example is ' +
				'Barack Obama who became the 44th president of the United State, and also the first African ' +
				'American president; Barack Obama who surpasses his African American agenda is truly a testament ' +
				'to the core quality of Americans. We here in America hold a strong unshaken foundation ' +
				'of equality, but it is you who will decide how tall this house will be.'
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
