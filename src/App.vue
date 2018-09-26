<template>
	<div id="app" :class="background">
		<HomePage id="home" class="page"/>
		<FirstPage id="first" class="page"/>
		<SecondPage id="second" class="page"/>
		<ConclusionPage id="conclusion" class="page"/>
	</div>
</template>

<script>
import HomePage from './components/HomePage.vue'
import FirstPage from './components/FirstPage.vue'
import SecondPage from './components/SecondPage.vue'
import ConclusionPage from './components/ConclusionPage.vue'

export default {
	name: 'app',
	components: {
		HomePage,
		FirstPage,
		SecondPage,
		ConclusionPage
	},
	data: function() {
		return {
			background: {
				home: true,
				first: false,
				second: false,
				conclusion: false
			},
			elementPosition: {
				home: 0,
				first: 0,
				second: 0,
				third: 0
			},
			scrollPosition: null,
			lastScrollPosition: 0
		};
	},
	methods: {
		updateScroll() {
			this.scrollPosition = window.scrollY + screen.height / 2;
			var direction = (this.scrollPosition - this.lastScrollPosition) > 0;
			if (this.scrollPosition > this.elementPosition.conclusion && direction) {
				this.background.second = false;
				this.background.conclusion = true;
			}
			else if (this.scrollPosition > this.elementPosition.second && direction) {
				this.background.first = false;
				this.background.second = true;
			}
			else if (this.scrollPosition > this.elementPosition.first && direction) {
				this.background.home = false;
				this.background.first = true;
			}
			else if (this.scrollPosition < this.elementPosition.first && !direction) {
				this.background.first = false
				this.background.home = true;
			}
			else if (this.scrollPosition < this.elementPosition.second && !direction) {
				this.background.second = false;
				this.background.first = true;
			}
			else if (this.scrollPosition < this.elementPosition.conclusion && !direction) {
				this.background.conclusion = false;
				this.background.second = true;
			}
			this.lastScrollPosition = this.scrollPosition;
		}
	},
	mounted() {
		this.elementPosition.home = document.getElementById("home").offsetTop;
		this.elementPosition.first = document.getElementById("first").offsetTop;
		this.elementPosition.second = document.getElementById("second").offsetTop;
		this.elementPosition.conclusion = document.getElementById("conclusion").offsetTop;
		window.addEventListener('scroll', this.updateScroll);
	},
	destroy() {
		window.removeEventListener('scroll', this.updateScroll);
	}
}
</script>

<style>
#app {
	background-attachment: fixed;
	background-size: cover;
	background-position: center center;
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	padding-top: 60px;
	padding: 180px;
	transition: 1s;
}
.home {
	background-image: url("./assets/FlagEdited.jpg");
	color: #2c3e50;
	text-shadow: 0px 0px 8px #ffffff;
}
.first {
	background-image: url("./assets/FarmPhoto.jpg");
	color: #2c3e50;
	text-shadow: 0px 0px 8px #ffffff;
}
.second {
	background-image: url("./assets/DiversePop.jpg");
	color: #e2e2e2;
	text-shadow: 0px 0px 8px #000000;
}
.conclusion {
	background-image: url("./assets/Black.jpg");
	color: #e2e2e2;
	text-shadow: 0px 0px 8px #ffffff;
}
.page {
	padding-bottom: 500px;
}
</style>
