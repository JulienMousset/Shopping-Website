<template>
    <div class="cart">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
            <div class="container">
                <div class="row">
                    <div v-for="product in APIData" :key="product.id" class="col-md-4">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { getAPI } from '../axios-api'
    import Navbar from '../components/Navbar'
    export default {
        methods: {
        },
        name: 'Cart',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/cart/',)
                .then(response => {
                    console.log('Post API has received data')
                    this.APIData = response.data
                })
                .catch(err => {
                    console.log(err)
                })
        }
    }
</script>