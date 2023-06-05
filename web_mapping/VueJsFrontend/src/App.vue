<template>
  <div id="app">
    <Map/>
  </div>
</template>
<script>

// import Farmers from './components/FarmerIndex.vue'
import Map from './components/map.vue'

export default {
  name: 'App',
  components: {
    Map
  },
  data () {
    return {
      farmers: ['']
    }
  },
  methods: {
    async getData () {
      try {
        // fetch farmers
        const response = await this.$http.get('http://127.0.0.1:8000/api/v1/farmer/list/')
        this.farmers = response.data.farmers
      } catch (error) {
        // log the error
        console.log(error)
      }
    }
  },
  created () {
    // Fetch farmers on page load
    this.getData()
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 700px;
  width: 70%;
  position: relative;
}
</style>
