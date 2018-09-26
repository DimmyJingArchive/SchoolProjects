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
				"; His labour is founded on the basis of nature, self-interest”. St.John De Crevecoeur focused on the equal "+
				"repayment of one's labour to connect with the American motto of “Ubi panis ibi patria” which translated t"+
				"o “Where there is bread, there is a country”; this emphasized on union through hard work, and how America i"+
				"s united through individuals that can contribute to the entire community. This is even more "+
				"impressive by the fact that St. John De Crevecoeur wrote this letter only after a few years of settlement i"+
				"n the newly born America. In fact, the idea was even translated to the America political foundation; for "+
				"instance, the failure to reward citizens with equal pay for their labour is a one of the core reasons for "+
				"secession from Britain; the Congress of America stated out that the act of “Imposing on [Americans] "+
				"without our Consent” and “cutting off [Americans] Trade” as a worthwhile offence among other as the "+
				"reason for their independence. This showed how far America is willing to go for their rights of equal pay"+
				", even if it meant challenging the strongest monarch of the time. Furthermore, the idea of protecting Am"+
				"erican's hard-earned rewards is also ingrained in the constitution of America; rulings such as one in artic"+
				"le 1, section 9, clause 6 were made to ensure that “No Preference shall be given by any Regulation of Commer"+
				"ce or Revenue to the Ports of one State over those of another: nor shall Vessels bound to, or from, one Sta"+
				"te, be obliged to enter, clear or pay Duties in another”. This clause prevents Congress from showing any fa"+
				"vouritism toward a particular state, further encouraging citizens to work without the worry of interfe"+
				"rence because of their political beliefs. On the note of citizens rights, the founding father of Am"+
				"erica have also, on multiple occasion, shown great interest in the matter; as express by James Madison in h"+
				"is excerpt from the Federalist no.10, “enlightened statesmen will be able to adjust these clashing interest"+
				"s, and render them all subservient to the public good”. The idea that Congress (statesmen) cannot interfere"+
				"with the public good comes a long way to again encourage people to freely work without the fear of an "+
				"oppressive government controlling their actions. But what gives? However glorious they are, "+
				"these are laws and statements made from 200 years ago. But probably the most impressive fact about the Amer"+
				"ican work ethic is that even after 200 years of turmoil, the idea lives on. Bill Gates started "+
				"up a company and raise it to where it is through his sheer determination to bring an affordable "+
				"personal computer to the people. Stories like this, of countless self-made billionaire, is a result "+
				"of the few lines written 200 years ago. In the same fashion, You too can join them in the pedestal of succe"+
				"ss if you are willing to pour your heart and soul into your work.",
			videoComment: '## Ali Saifi is a successful entrepreneur who brought subway to South Carolina through hard work and determination. Today he runs 400 stores around the state and earned 200 million dollars a year.'
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
