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
			msg: "## Nothing in the world is more valuable than hard work. If you dig deep down, the concept becomes simple."+
				"The more work put in, the better result pulled out. Part of the letters from an American farmer has pointed"+
				" out that “Here [In America] the rewards of his industry follow with equal steps the progress of his labour"+
				"; His labour is founded on the basis of nature, self-interest”. St.John De Crevecoeur emphasize on the equa"+
				"l repayment of one's labour to connect with the American motto of “Ubi panis ibi patria” which translated t"+
				"o “Where there is bread, there is a country”; this emphasizes on union through hard work, and how America i"+
				"s united through individual hard work that can later contribute to the entire community. And this is even m"+
				"ore impressive at the fact that St.John De Crevecoeur wrote this letter just after a few years of exposure "+
				"to the newly born America. In fact, the idea is even translated to America political foundation; for instan"+
				"ce, the failure to reward citizens with equal pay for their labour is a one of the core reasoning for seces"+
				"sion from Britain; the Congress of America stated out that the act of “Imposing on [Americans] without our "+
				"Consent” and “cutting off [Americans] Trade” as a worthwhile offence among other as the reason for their se"+
				"cession from Great Britain. This showed how far America is willing to go for their rights of an equal paid "+
				"off; even if it meant challenging the strongest monarch at the time. Furthermore, the idea of protecting Am"+
				"ericans hard-earned reward is also ingrained in the constitution of America; ruling such as one in article "+
				"1, section 9, clause 6 were made to ensure that “No Preference shall be given by any Regulation of Commerce"+
				"or Revenue to the Ports of one State over those of another: nor shall Vessels bound to, or from, one State,"+
				"be obliged to enter, clear or pay Duties in another”. This clause ensures that Congress can not show any fa"+
				"vouritism toward a particular state, and thus further encouraging citizen to work without the worry of heav"+
				"y taxation because of their politics, or beliefs. On the note of citizens rights, the founding father of Am"+
				"erica have also, on multiple occasion, shown great interest in the matter; as express by James Madison in h"+
				"is excerpt from the Federalist no.10, “enlightened statesmen will be able to adjust these clashing interest"+
				"s, and render them all subservient to the public good”. The idea that Congress (statesmen) cannot interfere"+
				"with the public good comes a long way to again encourage people to freely work with without the fear of an "+
				"oppressive government controlling what they can and can not do. But what gives? However glorious they are, "+
				"these are laws and statements made from 200 years ago. But probably the most impressive fact about the Amer"+
				"ican work ethic is that even after 200 years of change and turmoil the idea lives on. Bill Gates who start "+
				"up a multi-millionaire company and raise it to where it is through his sheer determination to bring an affo"+
				"rdable personal computer to the people. These stories of a countless self-made billionaire are a result of "+
				"a few lines written 200 years ago and you too can join them in the pedestal of success if you are willing t"+
				"o pour your heart and soul into your work.",
			videoComment: '## Ali Saifi is an successful entrepreneurs who brought subway to South Carolina through hard work and determination. Today he run 400 stores around the state and earn him 200 million dollars a year.'
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
