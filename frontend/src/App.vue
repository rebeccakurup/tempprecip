<template>
  <div id="app">
    <h1>Zurich Monthly Average Precipitation and Temperature</h1>
    <form @submit.prevent="submitYears">
      <br/>
      <label>Starting Year:</label>
      <input type="text" v-model="formData.start"/>
      <br/>
      <label>Ending Year:</label>
      <input type="text" v-model="formData.end"/>
      <br/>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
  import api from './api/index'
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      formData: {
        start: '',
        end: ''
      }
    }
  },
  methods: {
    submitYears () {
      api.fetchData('get', null, this.formData).then(res => {
          this.msg = 'Saved'
        }).catch((e) => {
          this.msg = e.response
      })
    }
  }
}
</script>

<style lang="scss">


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  max-width: 60%;
  margin: 0 auto;
  text-align: left;
}

h1, h2 {
  font-weight: bold;
  font-size: 3rem;
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
  input{
    width: 100%;
    display: block;
    padding: 6px 10px;
    border: 2px solid #ddd;
    border-radious: 4px;
    max-width: 200px;
  }

  label {
    margin-top: 15px;
    margin-bottom: 5px;
    display: block;
    font-size: 2rem;
  }

  button {
    margin-top: 3%;
    background: mediumaquamarine;
    color: #fff;
    border-radius: 3px;
    padding: 6px 10px;
    font-size: 2rem;

  }
</style>
