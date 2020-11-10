<template>
    <div class="product">
        <Navbar></Navbar>
        <div class="album py-5 bg-light">
            <div class="container">
                <div class="row">
                <div v-for="product in APIData" :key="product.id" class="col-md-4">
                    <div class="card mb-4 box-shadow">
                    <img class="card-img-top" v-bind:src="product.image" alt="Card image cap">
                    <!--<img class="card-img-top" src="https://via.placeholder.com/150x100" alt="Card image cap">-->
                    <div class="card-body">
                        <h4 class=""><a class="text-secondary" href="">{{product.name}}</a></h4>
                        <p class="card-text">{{product.price}}</p>
                        <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        <a href="" class="btn btn-sm btn-outline-primary" role="button" aria-pressed="true">-</a>
                        <a href="" class="btn btn-sm btn-outline-secondary" role="button" aria-pressed="true">+</a>
                        </div>
                        <small class="text-muted">9 mins</small>
                        </div>
                    </div>
                    </div>
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
        name: 'Product',
        data () {
            return {
                APIData: []
            }
        },
        components: {
            Navbar
        },
        created () {
            getAPI.get('/product/',)
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

<style scoped>

</style>