<template>
  <div class="home">
    <el-input v-model="count" placeholder="请输入内容" style="width:200px"></el-input>
    <el-button type="primary" @click="postCount">post</el-button>
    <el-button type="primary" @click="getCount">get</el-button>
    <p>{{ message }}</p>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  data() {
    return {
      count: 0,
      message: '',
    }
  },
  methods: {
    postCount: function() {
      this.axios
        .post('/count/', {
          count: this.count
        })
        .then(response => (this.message = response.status))
        .catch(error => (console.log(error)));
    }, 
    getCount: function() {
      this.axios
        .get('/count/')
        .then(response => (this.message = response.data))
        .catch(error => (console.log(error)));
    }, 
  }
}
</script>
