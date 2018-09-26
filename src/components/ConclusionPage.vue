<template>
	<div>
		<span v-html="marked(title)"></span>
		<span v-html="marked(msg)"/>
		<iframe :style="iframeStyle" src="https://stephaneginier.com/sculptgl/"/>
		<h2>Share Your Sculpture!</h2>
		<span>Click files &gt; Save .obj to save the file</span><br/><br/>
		<label for="sculptSubmit" id="sculptSubmitButton">Upload File</label>
		<input type="file" id="sculptSubmit" accept=".obj" style="display:none" @change="sendFile"/>
		<h2>Sculpture Gallery</h2>
		<div id="sculptShowcase">
			<model-obj :src="sculptSource" backgroundAlpha="0.01"/>
			<div id="switchBar">
				<b id="lastPage" @click="back">&lt;</b>
				<b id="nextPage" @click="next">&gt;</b>
			</div>
		</div>
	</div>
</template>

<script>
var marked = require('marked');
import {ModelObj} from 'vue-3d-model';

export default {
	name: 'ConclusionPage',
	data: function() {
		return {
			title: '# Assessment',
			msg: '## America is a country with great opportunities waiting to be claimed. ' +
				'So what do you want from America? The first step in your journey to achieve greatness ' +
				'is to set your goal. Thus, as an exercise, express your desired goal for your ' +
				'journey in America by sculpting the figure below',
			iframeStyle: {
				height: screen.height - 160 + 'px',
				width: screen.width - 40 + 'px',
				position: 'relative',
				left: '-160px'
			},
			sculptSource: 'https://s3.amazonaws.com/potatosfish/Thing.obj',
			sculptSources: ['https://s3.amazonaws.com/potatosfish/Thing.obj'],
			sculptIdx: 0
		};
	},
	methods: {
		marked: function(markdown) {
			return marked(markdown);
		},
		back: function() {
			this.sculptIdx++;
			if (this.sculptSources.length >= this.sculptIdx) {
				this.sculptIdx = 0;
			}
			this.sculptSource = this.sculptSources[this.sculptIdx];
		},
		next: function() {
			this.sculptIdx--;
			if (this.sculptIdx < 0) {
				this.sculptIdx = this.sculptSources.length - 1;
			}
			this.sculptSource = this.sculptSources[this.sculptIdx];
		},
		sendFile: function(e) {
			var reader = new FileReader();
			var file = e.target.files[0];
			var par = this;
			reader.onload = function() {
				// eslint-disable-next-line
				console.log(reader.result);
				par.sculptSources.push(reader.result);
				par.sculptSource = par.sculptSources[par.sculptSources.length - 1];
				par.sculptIdx = par.sculptSources.length - 1;
			}
			reader.readAsDataURL(file);
		}
	},
	components: {
		ModelObj
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
model-obj {
	border: 5px solid white;
}
#sculptSubmitButton {
	color: #0099CC;
	background: white;
	border: 2px solid #0099CC;
	border-radius: 6px;
	font: bold 64px Arial;
	padding: 16px 32px;
	text-align: center;
	display: inline-block;
	font-size: 16px;
	margin: 4px 2px;
	transition-duration: 0.4s;
	cursor: pointer;
	text-decoration: none;
	text-transform: uppercase;
}
#sculptSubmitButton:hover {
	background-color: #008CBA;
	color: white;
}
#sculptShowcase {
	position: relative;
}
#switchBar {
	position: absolute;
	width: 97%;
	bottom: 0;
	color: #ffffff;
	padding-right: 16px;
	padding-left: 16px;
	margin-top: 16px;
	margin-bottom: 16px;
	font-family: Verdana,sans-serif;
	font-size: 18px;
	line-height: 1.5;
}
#lastPage {
	cursor: pointer;
	float: left;
}
#nextPage {
	cursor: pointer;
	float: right;
}
</style>
