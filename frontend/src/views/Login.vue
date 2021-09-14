<template>
    <div class="page-log-in">
        <div class="columns">
            <div class="column is-one-third is-offset-one-third">
                <h1 class="title">Log in</h1>
                <form @submit.prevent="submitForm" class="box">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="text" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password1">
                        </div>
                    </div>
                    
                    <div class="field">
                        <div class="control">
                            <button class="button is-dark">Log in</button>
                        </div>
                    </div>
                    Or <router-link to="/sign-up">click here </router-link> to sign up!
                </form>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name: 'Login',
    data(){
    }
}
</script>