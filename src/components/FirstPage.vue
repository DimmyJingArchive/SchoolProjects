<template>
	<div>
		<span v-html="marked(title)"/>
		<span v-html="marked(msg)"/>
		<youtube :video-id="'XeG8z3SkxRk'"/>
		<span v-html="marked(videoComment)"/>
	</div>
</template>

<script>
var marked = require('marked');

export default {
	name: 'FirstPage',
	data: function() {
		return {
			title: '# Hard Work',
			msg: "## Nothing in the world is more valuable than hard work. If you dig deep down, the concept " +
				"becomes simple. The more work put in, the better result pulled out. Part of the letters " +
				"from an American farmer has pointed out that “Here [In America] the rewards of his industry " +
				"follow with equal steps the progress of his labour; His labour is founded on the basis of nature, " +
				"self-interest”. St. John De Crevecoeur focused on the equal repayment of one's labour to connect " +
				"with the American motto of “Ubi panis ibi patria” which translated to “Where there is bread, " +
				"there is a country”; this emphasized on union through hard work, and how America is created " +
				"through individuals that can contribute to the entire community. This is even more impressive " +
				"by the fact that St. John De Crevecoeur wrote this letter only after a few years of settlement in " +
				"the newly born America. In fact, the idea was even translated to the American political foundation; for " +
				"instance, the failure to reward citizens with equal pay for their labour is one of the core reasons " +
				"for secession from Britain; the Congress of America stated that the act of “Imposing on [Americans] " +
				"without our Consent” and “cutting off [Americans] Trade” as an offence among others for the " +
				"reason of their independence. This showed how far America is willing to go for economic equality" +
				"even if it meant challenging the strongest monarch of the time. Furthermore, the idea of " +
				"protecting Americans economically is also engrained in the constitution of America; " +
				"rulings such as one in article 1, section 9, clause 6 were made to ensure that “No Preference " +
				"shall be given by any Regulation of Commerce or Revenue to the Ports of one State over those " +
				"of another: nor shall Vessels bound to, or from, one State, be obliged to enter, clear or pay " +
				"Duties in another”. This clause prevents Congress from showing any favouritism toward a particular " +
				"state, further encouraging citizens to work without the worry of interference caused by their " +
				"political beliefs. On the note of citizens rights, the founding fathers of America have also, on " +
				"multiple occasion, shown great interest in the matter; as expressed by James Madison in his excerpt " +
				"from the Federalist no.10, “enlightened statesmen will be able to adjust these clashing interests, " +
				"and render them all subservient to the public good”. The idea that Congress (statesmen) " +
				"cannot interfere with the economy directly comes a long way to encourage people to freely work " +
				"without the fear of an oppressive government controlling their actions. Those documents were " +
				"revolutionary at the time, but what gives? However glorious they are, these are laws and statements " +
				"made 200 years ago. However, the most impressive fact about the American work ethic is that even " +
				"after 200 years of turmoil, the idea still lives on. Bill Gates started up a company and raise it " +
				"to where it is through his sheer determination to bring affordable personal computers to the common " +
				"market. Stories like this, of countless self-made billionaires, is a result of the few documents written " +
				"centuries years ago. In the same fashion, You too can join them in the pedestal of success if you are " +
				"willing to pour your heart and soul into your work.",
			videoComment: '## Ali Saifi is a successful entrepreneur who brought subway to South Carolina through ' +
						'hard work and determination. Today he runs 400 stores around the state and earned 200 ' +
						'million dollars a year.'
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
