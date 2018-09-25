<template>
	<div>
		<span v-html="marked(title)"></span>
		<span v-html="marked(msg)"></span>
	</div>
</template>

<script>
var marked = require('marked');

export default {
	name: 'FirstPage',
	data: function() {
		return {
			title: '# Hard Work',
			msg: "## Nothing in the world is more valuable than hard work. If you dig deep down, the concept becomes simple. The more work put in, the better result pulled out. Part of the letters from an American farmer has pointed out that “Here [In America] the rewards of his industry follow with equal steps the progress of his labour; His labour is founded on the basis of nature, self-interest”(St.John De Crevecoeur ). St.John De Crevecoeur emphasize on the equal repayment of one's labour to connect with the american motto of “Ubi panis ibi patria” which translated to “Where there is bread, there is country”; this emphasize on union through hard work, and how America is united through individual hard work that can later contribute to the entire community. And this is even more impressive at the fact that St.John De Crevecoeur wrote this letter just after a few years of exposure to the newly born america. In fact, the idea is even translated to America political foundation; for instance, the failure to reward citizens with equal pay for their labour is a one of the core reasoning for secession from Britain; the Congress of America stated out that the act of “Imposing on [Americans] without our Consent” and “cutting off [Americans] Trade” as an worthwhile offense among other as the reason for their secession from the Great Britain. This shown how far America is willing to go for their rights of an equal paid off; even if it meant challenging the strongest monarch at the time. Furthermore, the idea of protecting Americans hard earn reward is also ingrain in the constitution of America; ruling such as one in article 1, section 9, clause 6 were made to ensure that “No Preference shall be given by any Regulation of Commerce or Revenue to the Ports of one State over those of another: nor shall Vessels bound to, or from, one State, be obliged to enter, clear or pay Duties in another”. This clause ensure that Congress can not show any favouritism toward a particular state, and thus further encouraging citizen to work without the worry of heavy taxation because of their politics, or believes. But what gives? However glorious they are, these are laws and statements made 200 years ago."
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
