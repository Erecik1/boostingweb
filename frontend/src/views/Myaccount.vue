<template>
Hi {{ username }}!
</template>

<script>
import axios from "axios";

export default {
  name: "Myaccount",
  data(){
    return {
        username:'',
        id:'',
        email:'',
        error:[],
    }
  },
      beforeMount() {
        this.getMyData()
        document.title = 'MyAccount'
      },
  methods:{
    getMyData(){
      axios
      .get("api/v1/users/me/")
      .then(response=>{
        this.username = response.data.username
        this.id = response.data.id
        this.email = response.data.email
      })
      .catch(error =>{
        console.log(error)
      })
    }
  },
}
</script>

<style scoped>

</style>