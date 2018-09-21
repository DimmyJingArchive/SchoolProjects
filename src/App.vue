<template>
	<div id="app">
		<HomePage/>
	</div>
</template>

<script>
import HomePage from './components/HomePage.vue'

export default {
	name: 'app',
	components: {
		HomePage
	}
}
</script>

<style>
#app {
	background-image: url("./assets/FlagEdited.jpg");
	background-size: cover;
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	padding-top: 60px;
	padding: 120px;
}
</style>
